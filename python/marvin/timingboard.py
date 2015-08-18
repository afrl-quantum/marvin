# vim: et:sw=2:ts=2:nowrap

from . import fpga

import numpy as np
import time

class NotATimingBoard(Exception):
  """
  This exception is raised when the requested board address does not appear to actually
  be a timing board.
  """
  pass

class TimingBoard(fpga.Board):
  """
  A Pythonic interface to our digital I/O timing card implemented on the Marvin
  GX3500 FPGA board.
  """

  def __init__(self, slot, bitstream_file=None, progress=None):
    """
    Bind a TimingBoard to a PCI/PXI slot, uploading a specific
    SVF bitstream file if specified.
    
    :param slot: the PCI bus/slot number
    :param bitstream_file: the path of the SVF file implementing the timing board,
                           or None if the card is already configured
    :param progress: the progress indicator for fpga.load_program()
    """
    super(TimingBoard, self).__init__(slot)
    
    if bitstream_file is not None:
      self.load_program(bitstream_file, target='volatile', progress=progress)
    
      # wait up to 15 seconds for the card to reset and identify as a timing board
      for i in xrange(15):
        try:
          self.version
          return
        except NotATimingBoard:
          time.sleep(1.0)

    # verify that it is a timing board
    self.version
    
  CONFIG_BITS = { 'TRIG_ENABLE':  0x0001,
                  'REFCLK_10MHz': 0x0002,
                  'AUTO_TRIGGER': 0x0008 }

  STATES = { 'SETUP':    0,
             'READY':    1,
             'RUN':      2,
             'PAUSED':   3,
             'ARMING':   4,
             'STOPPING': 5 }

  STATE_NAMES = ['SETUP', 'READY', 'RUN', 'PAUSED', 'ARMING', 'STOPPING']

  STATUS_BITS = { 'ERR_BAD_CMD':             0x0010,
                  'ERR_INAPPROPRIATE_STATE': 0x0020,
                  'ERR_BAD_DURATION':        0x0040,
                  'ERR_BAD_PCI_ACCESS':      0x0080,
                  'WARN_BAD_REFCLK':         0x0100,
                  'WARN_NO_PXI_CLOCK':       0x0200 }

  DEBUG_BITS = { 'Buffer_Empty':      0x0001,
                 'PCI_Allowed':       0x0002,
                 'Run_Timer':         0x0004,
                 'Load_Instructions': 0x0008,
                 'Dynamic_Output':    0x0010,
                 'System_FState': 0x007f8000,
                 'Core_FState':   0xff800000 }

  COMMANDS = { 'NOOP':    0,
               'ARM':     1,
               'TRIGGER': 2,
               'PAUSE':   3,
               'RESUME':  4,
               'STOP':    5 }

  REGS = { 'RESET_A':  0x0000,
           'RESET_B':  0x0004,
           'RESET_C':  0x0008,
           'RESET_D':  0x000c,
           'PXI_RT1':  0x0010,
           'PXI_RT2':  0x0014,
           'N_REPS':   0x0018,
           'CONFIG':   0x001c,
           'CMD':      0x0020,
           'STATUS':   0x0024,
           'STEP':     0x0028,
           'REPCNT':   0x002c,
           'OUTPUT_A': 0x0030,
           'OUTPUT_B': 0x0034,
           'OUTPUT_C': 0x0038,
           'OUTPUT_D': 0x003c,
           'TIME_HI':  0x0040,
           'TIME_LO':  0x0044,
           'DEBUG':    0x0078,
           'VERSION':  0x007c }

  def set_defaults(self, port_a=0, port_b=0, port_c=0, port_d=0):
    """
    Set the values that should appear on the ports when no sequence is running.
    
    :param port_a: the bit pattern for port A
    :param port_b: the bit pattern for port B
    :param port_c: the bit pattern for port C
    :param port_d: the bit pattern for port D
    """

    self.write('reg', self.REGS['RESET_A'], port_a)
    self.write('reg', self.REGS['RESET_B'], port_b)
    self.write('reg', self.REGS['RESET_C'], port_c)
    self.write('reg', self.REGS['RESET_D'], port_d)

  def set_pxi_routing(self, pxi0=None, pxi1=None, pxi2=None, pxi3=None, 
                            pxi4=None, pxi5=None, pxi6=None, pxi7=None):
    """
    Configure the routing from output pins to PXI triggers.
    
    :param pxi0: the pin number (0-127) to mirror on to PXI trigger 0, or None if no pin
                 should be connected
    :param pxi1: the pin number (0-127) to mirror on to PXI trigger 1, or None if no pin
                 should be connected
    :param pxi2: the pin number (0-127) to mirror on to PXI trigger 2, or None if no pin
                 should be connected
    :param pxi3: the pin number (0-127) to mirror on to PXI trigger 3, or None if no pin
                 should be connected
    :param pxi4: the pin number (0-127) to mirror on to PXI trigger 4, or None if no pin
                 should be connected
    :param pxi5: the pin number (0-127) to mirror on to PXI trigger 5, or None if no pin
                 should be connected
    :param pxi6: the pin number (0-127) to mirror on to PXI trigger 6, or None if no pin
                 should be connected
    :param pxi7: the pin number (0-127) to mirror on to PXI trigger 7, or None if no pin
                 should be connected
    """
    pxi30 = [ (0x80 | val) if val is not None else 0 for val in (pxi3, pxi2, pxi1, pxi0) ]
    pxi74 = [ (0x80 | val) if val is not None else 0 for val in (pxi7, pxi6, pxi5, pxi4) ]

    pxi_rt1 = reduce(lambda a, v: (a << 8) | v, pxi30)
    pxi_rt2 = reduce(lambda a, v: (a << 8) | v, pxi74)

    self.write('reg', self.REGS['PXI_RT1'], pxi_rt1)
    self.write('reg', self.REGS['PXI_RT2'], pxi_rt2)

  @property
  def state(self):
    """
    What state the card is in.
    :return: 'SETUP', 'READY', 'RUN', 'PAUSED', 'ARMING', 'STOPPING', or 'UNKNOWN'
    """
    s = self.read('reg', self.REGS['STATUS']).astype(np.uint32)
    v = (s & 0x07)
    if v < len(self.STATE_NAMES):
      return self.STATE_NAMES[v]
    return 'UNKNOWN'

  @property
  def errors(self):
    """
    What errors have been latched.
    
    :return: a list of strings
    """
    s = self.read('reg', self.REGS['STATUS']).astype(np.uint32)
    s &= ~0x000f # ignore state bits and PCI_PERMITTED

    errs = [ k for k, v in self.STATUS_BITS.viewitems() if (s & v) != 0 ]
    return errs

  def clear_errors(self, mask=None):
    """
    Clear latched errors.
    :param mask: None to clear all errors, or a list of error names to clear
    """
    if mask is not None:
      m = reduce(lambda a, v: a | v, [ self.STATUS_BITS[k] for k in mask ])
    else:
      m = ~0x000f
    
    self.write('reg', self.REGS['STATUS'], m)

  def command(self, cmd):
    """
    Tell the card to execute a command.
    
    :param cmd: one of 'NOOP', 'ARM', 'TRIGGER', 'PAUSE', 'RESUME', or 'STOP'
    :return: True if the command was accepted, False if an error bit was latched
    """
    if not cmd in self.COMMANDS:
      raise ValueError('bad command')

    # clear the command errors
    error_bits = self.STATUS_BITS['ERR_BAD_CMD'] | self.STATUS_BITS['ERR_INAPPROPRIATE_STATE']
    self.write('reg', self.REGS['STATUS'], error_bits)

    # write the command
    self.write('reg', self.REGS['CMD'], self.COMMANDS[cmd])
    
    # check the status register
    v = self.read('reg', self.REGS['STATUS']).astype(np.uint32)
    return ((v & error_bits) == 0)

  @property
  def version(self):
    """
    Read the VERSION register.
    
    :return: a tuple (major-version, minor-version)
    """
    ver = self.read('reg', self.REGS['VERSION']).astype(np.uint32)
    if (ver & 0xffff0000) != 0xafd00000:
      raise NotATimingBoard()

    return ((ver & 0xff00) >> 8, (ver & 0xff))

  @property
  def debug(self):
    """
    Reads the DEBUG register.
    
    :return: a dict of debug bit names and their boolean value (True or False)
    """
    d = self.read('reg', self.REGS['DEBUG']).astype(np.uint32)

    bits = dict([ (name, (d & bit) == bit) for (name, bit) in self.DEBUG_BITS.viewitems()])
    bits['System_FState'] = bin((d & self.DEBUG_BITS['System_FState']) >> 15)
    bits['Core_FState'] = bin(d >> 23)
    return bits

  def config(self, number_transitions, use_10_MHz=False, auto_trigger=False, external_trigger=False):
    """
    Sets the card configuration through the CONFIG register.
    
    :param number_transitions: the number of valid steps in the uploaded program
    :param use_10_MHz: True if the master timebase should be referenced from the PXI 10 MHz,
                       False if it should be referenced to the onboard 80 MHz oscillator
    :param auto_trigger: True if the card should automatically trigger itself when it is
                         ARMed, False if it should wait for a software or hardware trigger
                         before executing the sequence.
    :param external_trigger: True if the card should listen to the external trigger line,
                             False if it should only accept software triggers.
    """

    cval = number_transitions << 16

    if use_10_MHz:
      cval |= self.CONFIG_BITS['REFCLK_10MHZ']

    if auto_trigger:
      cval |= self.CONFIG_BITS['AUTO_TRIGGER']

    if external_trigger:
      cval |= self.CONFIG_BITS['TRIG_ENABLE']

    self.write('reg', self.REGS['CONFIG'], cval)

