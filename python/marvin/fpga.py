# vim: et:sw=2:ts=2:nowrap

import ctypes
from ctypes import create_string_buffer, byref
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
      GxFpga.GxFpgaGetErrorString(status, byref(err_str), 256, byref(status))
      raise FpgaError(err_str.value)
  
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
  
  def load_program(self, filename, target='volatile'):
    """
    Load a Serial Vector Format (.svf) bitstream file to the FPGA.
    
    :param filename: the path to the target .svf file
    :param target: which storage to load the bitstream into, either 'volatile' or 'eeprom'.
    """
    if target == 'volatile':
      lt = GxFpga.GXFPGA_LOAD_TARGET_VOLATILE
    elif target == 'eeprom':
      lt = GxFpga.GXFPGA_LOAD_TARGET_EEPROM
    else:
      raise ValueError('target must be either "volatile" or "eeprom"')
    
    self._call(GxFpga.GxFpgaLoad, self._handle, lt, filename, GxFpga.GXFPGA_LOAD_MODE_ASYNC)
    while self._load_percentage() != 100:
      time.sleep(0.1)
  
  def read(self, location, addr, size=4):
    """
    Read a value from the FPGA.
    
    :param location: 'reg' (register space, BAR 1) or 'mem' (memory, BAR 2)
    :param addr: the address to read
    :param size: the access size in bytes (1, 2, or 4)
    
    :return: the value read
    """
    if size == 1:
      val = ctypes.c_byte(0)
    elif size == 2:
      val = ctypes.c_int16(0)
    elif size == 4:
      val = ctypes.c_int32(0)
    else:
      raise ValueError('register access size must be 1, 2, or 4')
    
    if location == 'reg':
      function = GxFpga.GxFpgaReadRegister
    elif location == 'mem':
      function_name = GxFpga.GxFpgaReadMemory
      
    self._call(function, self._handle, addr, byref(val), size)
    return val.value
  
  def write(self, location, addr, value, size=4):
    """
    Write a value to the FPGA.
    
    :param location: 'reg' (register space, BAR 1) or 'mem' (memory, BAR 2)
    :param addr: the address to write
    :param value: the value to write
    :param size: the access size in bytes (1, 2, or 4)
    """
    if size == 1:
      val = ctypes.c_byte(value)
    elif size == 2:
      val = ctypes.c_int16(value)
    elif size == 4:
      val = ctypes.c_int32(value)
    else:
      raise ValueError('register access size must be 1, 2, or 4')
    
    if location == 'reg':
      function = GxFpga.GxFpgaWriteRegister
    elif location == 'mem':
      function = GxFpga.GxFpgaWriteMemory
      
    self._call(function, self._handle, addr, byref(val), size)
    return val.value
  

