# vim: et:sw=2:ts=2:nowrap

import ctypes
from ctypes import create_string_buffer, byref
import numpy as np
import os.path
import sys
import time

from .clib import GxFpga


class FpgaError(Exception):
  """
  The exception thrown when an error occurs in communicating with
  the FPGA board.
  """
  pass 

class Board(object):
  """A Pythonic interface to the Marvin Test GX3500 FPGA board"""
  
  def __init__(self, slot):
    """
    Create a binding to a given GX2500 board.
    
    :param slot: the PCI bus/slot number to bind against
    """

    handle = ctypes.c_short(0)
    self._call(GxFpga.GxFpgaInitialize, slot, byref(handle))
    self._handle = handle
  
  def _call(self, function, *args):
    """
    Call a libGxFpga function, automatically passing in a final argument
    byref(status), then raise an appropriate FpgaError if status != 0.
    
    :param function: the function in .clib.GxFpga to call
    :param *args: the first N-1 arguments taken by the function (argument N
                  is assumed to be byref(status)
    """
    status = ctypes.c_short(0)
    args = args + (byref(status), )
    function(*args)
    
    if status.value != 0:
      err_str = create_string_buffer('', size=256)
      GxFpga.GxFpgaGetErrorString(status, err_str, 256, byref(status))
      raise FpgaError(err_str.value)

  def reset(self):
    """
    Reset the board.
    """
    self._call(GxFpga.GxFpgaReset, self._handle)
  
  def _load_percentage(self):
    """Returns the percentage value from GxFpgaLoadStatus"""
    percentage = ctypes.c_short(0)
    self._call(GxFpga.GxFpgaLoadStatus, self._handle, byref(percentage))
    return percentage.value
  
  def summary(self):
    """
    Read the board self-identification summary.
    
    :return: the self-identification summary string
    """
    buf = create_string_buffer('', size=256)
    self._call(GxFpga.GxFpgaGetBoardSummary, self._handle, buf, 256)
    
    return buf.value
  
  def load_program(self, filename, target='volatile', progress=None):
    """
    Load a Serial Vector Format (.svf) bitstream file to the FPGA.
    
    :param filename: the path to the target .svf file
    :param target: which storage to load the bitstream into, either 'volatile' or 'eeprom'.
    :param progress: how to handle load progress notifications. May be None for 
                     silent, 'stdout' for a textual progress report on stdout, or
                     a callable progress(step, percent) where step is 'start', 'load',
                     or 'done', and percent is the percentage of the load that has
                     completed.
    """
    if target == 'volatile':
      lt = GxFpga.GXFPGA_LOAD_TARGET_VOLATILE
    elif target == 'eeprom':
      lt = GxFpga.GXFPGA_LOAD_TARGET_EEPROM
    else:
      raise ValueError('target must be either "volatile" or "eeprom"')

    if progress is None:
      progress = lambda step, percent: None
    elif progress == 'stdout':
      base = os.path.basename(filename)
      def progress(step, percent):
        if step == 'start':
          sys.stdout.write('Loading ' + base + ':   0%')
          sys.stdout.flush()
        elif step == 'load':
          sys.stdout.write('\b\b\b\b{0:3d}%'.format(percent))
          sys.stdout.flush()
        elif step == 'done':
          sys.stdout.write('\b\b\b\bDone.\n')
          sys.stdout.flush()

    try:
      progress('start', 0)
    except:
      raise ValueError("progress must be None, 'stdout', or a callable")
    
    self._call(GxFpga.GxFpgaLoad, self._handle, lt, filename, GxFpga.GXFPGA_LOAD_MODE_ASYNC)
    while True:
      p = self._load_percentage()
      progress('load', 0)
      if p == 10:
        break
      time.sleep(0.1)
    progress('done', 100)
  
  def read(self, location, addr, count=1):
    """
    Read a value from the FPGA.
    
    :param location: 'reg' (register space, BAR 1) or 'mem' (memory, BAR 2)
    :param addr: the address to read (must be a multiple of 4)
    :param count: the number of 32-bit dwords to read
    
    :return: the values read, as a numpy.ndarray
    """
    
    if location == 'reg':
      function = GxFpga.GxFpgaReadRegister
    elif location == 'mem':
      function = GxFpga.GxFpgaReadMemory
    else:
      raise ValueError("location must be 'reg' or 'mem'")
    
    val = np.zeros(() if count == 1 else (count,), dtype=np.int32)
    valptr = val.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))
    self._call(function, self._handle, addr, valptr, 4*count)
    
    return val
  
  def write(self, location, addr, values):
    """
    Write a value to the FPGA.
    
    :param location: 'reg' (register space, BAR 1) or 'mem' (memory, BAR 2)
    :param addr: the address to write (must be a multiple of 4)
    :param values: the 32-bit value(s) to write, as something coercable to a numpy.ndarray
    """
    
    vals = np.asarray(values, dtype=np.uint32)
    if vals.ndim == 0:
      size = 4
    elif vals.ndim == 1:
      size = 4 * len(vals)
    else:
      raise ValueError('cannot write arrays of greater than 1 dimension')
    
    if location == 'reg':
      function = GxFpga.GxFpgaWriteRegister
    elif location == 'mem':
      function = GxFpga.GxFpgaWriteMemory
    else:
      raise ValueError("location must be 'reg' or 'mem'")
    
    valptr = vals.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32))
    self._call(function, self._handle, addr, valptr, size)

  def _call_summary(self, fn, buflen=256):
    """
    Call a GxFpgaGet*Summary() function which takes a handle,
    a string buffer, and the buffer's length.

    :param fn: the GxFpga function to call
    :param buflen: the size of the string buffer to use
    :return: the fetched string
    """
    buf = ctypes.create_string_buffer(buflen)
    self._call(fn, self._handle, buf, buflen)
    return buf.value

  @property
  def eeprom_summary(self):
    """
    The EEPROM status string, as read from the board.
    """
    return self._call_summary(GxFpga.GxFpgaGetEepromSummary)

  def load_from_eeprom(self):
    """
    Load the FPGA bitstream stored in EEPROM on the board.
    """
    self._call(GxFpga.GxFpgaLoadFromEeprom, self._handle)

  @property
  def driver_summary(self):
    """
    The Marvin Test GxFpga driver info.

    :return: the driver information tuple(string, major_version, minor_version)
    """
    buflen = 256
    buf = ctypes.create_string_buffer(buflen)
    ver = ctypes.c_uint32()
    self._call(GxFpga.GxFpgaGetDriverSummary, buf, buflen, ctypes.byref(ver))

    return (buf.value, ver >> 16, ver & 0xffff)

  @property
  def board_summary(self):
    """
    The board summary information as a string.

    :return: the board summary string
    """
    return self._call_summary(GxFpga.GxFpgaGetBoardSummary)
