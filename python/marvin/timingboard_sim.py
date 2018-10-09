# vim: et:sw=2:ts=2:nowrap

import sys
if sys.version_info[0] == 3:
  long = int

import numpy as np
import time

class UnimplementedError(Exception):
  """
  Raised when an operation is requested that the simulator does not support.
  """
  pass

class TimingBoard(object):
  """
  A simulated version of the interface to the GX3500-based timing / digital I/O card.
  """
  
  def __init__(self, slot, bitstream_file=None, progress=None):
    self._mem = np.zeros((2**16,), dtype=np.uint32)
    self._state = 'SETUP'
    self._errors = []
    self._defaults = []
    self._auto_trigger = False
    self._nr_transitions = 0
    self._nr_repetitions = 0
    self._repetition = 0
    self._step = 0

  def set_defaults(self, port_a=0, port_b=0, port_c=0, port_d=0):
    """
    Set the static port values for when the sequence is not running.
    """
    self._defaults = [port_a, port_b, port_c, port_d]

  def set_pxi_routing(self, pxi0=None, pxi1=None, pxi2=None, pxi3=None, 
                            pxi4=None, pxi5=None, pxi6=None, pxi7=None):
    """
    Set the PXI trigger routing.
    """
    pass

  @property
  def state(self):
    """
    Returns the card state.
    
    :return: a state string
    """
    self._check_run_status()
    return self._state

  def _latch_error(self, err):
    """
    Pretend to latch a hardware error.
    """
    if err not in self._errors:
      self._errors.append(err)

  @property
  def errors(self):
    """
    The list of latched hardware errors.
    
    :return: a list of error names, as strings
    """
    return self._errors

  def clear_errors(self, mask=None):
    """
    Clear the latched errors.
    
    :param mask: the set of errors to clear, or None if all errors should be cleared.
    """
    if mask is None:
      self._errors = []
    else:
      self._errors = [e for e in self._errors if e not in mask]

  def _run(self):
    """
    Set up for a simulated run.
    """
    self._state = 'RUN'
    self._start_time = time.time()
    self._step = 0

  def _stop(self):
    """
    End a simulated run.
    """
    self._state = 'SETUP'
    self._repetition = 0
    self._step = 0

  def _check_run_status(self):
    """
    Called every time a status request is made. Updates the internal
    simulated run status.
    
    :return: True if the system is still 'running', False if it isn't
    """
    if self._state != 'RUN':
      return False

    self._step += self._nr_transitions // 10
    if self._step >= self._nr_transitions:
      self._repetition += 1
      if self._nr_repetitions == 0 or self._repetition < self._nr_repetitions:
        if self._auto_trigger:
          self._run()
        else:
          self._step = 0
          self._state = 'ARMED'
          return False
      else:
        self._stop()
        return False
    return True

  def command(self, cmd):
    """
    Send a user command to the simulated card.
    """
    self.clear_errors(['ERR_INAPPROPRIATE_STATE'])
    
    if cmd == 'STOP':
      self._stop()
    elif cmd == 'ARM':
      if self._state != 'SETUP':
        self._latch_error('ERR_INAPPROPRIATE_STATE')
        return False
      if self._auto_trigger:
        self._run()
      else:
        self._state = 'ARMED'
    elif cmd == 'TRIGGER':
      if self._state != 'ARMED':
        self._latch_error('ERR_INAPPROPRIATE_STATE')
        return False
      self._run()
    elif cmd == 'PAUSE':
      if self._state != 'RUN':
        self._latch_error('ERR_INAPPROPRIATE_STATE')
        return False
      self._state = 'PAUSED'
    elif cmd == 'RESUME':
      if self._state != 'PAUSED':
        self._latch_error('ERR_INAPPROPRIATE_STATE')
        return False
      self._state = 'RUN'
    elif cmd == 'NOOP':
      pass
    else:
      raise ValueError('bad command')
    
    return True

  @property
  def version(self):
    """
    The hardware revision of the card bitstream.
    
    :return: a tuple of (major, minor) version numbers
    """
    return (0, 255, 'deadbeef')

  @property
  def debug(self):
    """
    Hardware debugging information for the card.
    
    :return: a map of {item_name, value}
    """
    return {}

  def config(self, number_transitions, repetitions=0,
             use_10_MHz=False, auto_trigger=False,
             external_trigger=False, invert_external_trigger=False,
             external_trigger_type='edge', fifo_self_test=False):
    """
    Set the card configuration.
    """
    self._nr_transitions = number_transitions
    self._nr_repetitions = repetitions
    self._auto_trigger = auto_trigger

  def write(self, target, addr, vals):
    """
    Write to simulated card memory. Used for uploading sequences.
    """
    if target != 'mem':
      raise UnimplementedError('only memory writing is supported by the simulator')

    if (addr % 4) != 0:
      raise ValueError('only 32-bit aligned addresses are supported')

    v = np.asarray(vals, dtype=np.uint32)
    addr //= 4
    self._mem[addr:(addr+len(vals))] = v

  def read(self, target, addr, count=1):
    """
    Read from simulated card memory.
    """
    if target != 'mem':
      raise UnimplementedError('only memory reading is supported by the simulator')

    if (addr % 4) != 0:
      raise ValueError('only 32-bit aligned addresses are supported')

    addr //= 4
    return self._mem[addr:(addr+count)].astype(np.int32)

  @property
  def counter(self):
    """
    The current time stamp in the sequence, in units of 10 ns.
    
    :return: the time stamp
    """
    if not self._check_run_status():
      return 0
    dt = time.time() - self._start_time
    return long(dt * 1e8)

  @property
  def step(self):
    """
    The most recently completed step number in the running sequence.
    
    :return: the step number
    """
    if not self._check_run_status():
      return 0

    return self._step

  @property
  def repetition(self):
    """
    The number of times the sequence has been repeated without the card returning
    to SETUP.
    
    :return: the repetition count
    """
    if not self._check_run_status() and self.state != 'ARMED':
      return 0
    
    return self._repetition

