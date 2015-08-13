# vim: et:sw=2:ts=2:nowrap

from . import fpga

import numpy as np


class TimingBoard(fpga.Board):
  """
  A Pythonic interface to our digital I/O timing card implemented on the Marvin
  GX3500 FPGA board.
  """

  STATES = { 'SETUP':    0,
             'READY':    1,
             'RUN':      2,
             'PAUSED':   3,
             'ARMING':   4,
             'STOPPING': 5 }
  STATE_NAMES = ['SETUP', 'READY', 'RUN', 'PAUSED', 'ARMING', 'STOPPING']

  STATUS_BITS = { 'PCI_PERMITTED':           0x0008,
                  'ERR_BAD_CMD':             0x0010,
                  'ERR_INAPPROPRIATE_STATE': 0x0020,
                  'ERR_BAD_DURATION':        0x0040,
                  'ERR_BAD_PCI_ACCESS':      0x0080,
                  'WARN_BAD_REFCLK':         0x0100,
                  'WARN_NO_PXI_CLOCK':       0x0200 }

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

    errs = [ k for k, v in self.STATUS_BITS.items() if (s & v) != 0 ]
    return errs

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

