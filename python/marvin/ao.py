# vim: et:sw=2:ts=2:nowrap

import ctypes
from ctypes import create_string_buffer, byref, sizeof
import numpy as np
import os.path
import sys
import time

from six.moves import range

from .clib import GxAo


class AoError(Exception):
  """
  The exception thrown when an error occurs in communicating with
  the AO board.
  """
  pass

class Board(object):
  """A Pythonic interface to the Marvin Test GX164x AO board"""

  RANGES = {
    'GX1642' : {
      0: (0,20),
      1: (-20,20),
      2: (0,10),
      3: (-10,10),
    },
    'GX1648' : {
      0: (0,10),
      1: (-10,10),
      2: (0,5),
      3: (-5,5),
    },
    'GX1649' : {
      0: (-15,15),
    },
  }

  RANGES_reverse = {
    board : { v:k for k,v in D.items() }
    for board,D in RANGES.items()
  }

  ARB_DEVICES = [ 'GX1649', 'GX1649-1' ]
  STREAM_DEVICES = [ 'GX1649-1' ]

  CLOCK_SOURCES = {
    GxAo.GXAO_1649_CLOCKSOURCE_INTERNAL : 'internal',
    GxAo.GXAO_1649_CLOCKSOURCE_EXTERNAL : 'external',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI0     : 'TRIG/0',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI1     : 'TRIG/1',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI2     : 'TRIG/2',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI3     : 'TRIG/3',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI4     : 'TRIG/4',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI5     : 'TRIG/5',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI6     : 'TRIG/6',
    GxAo.GXAO_1649_CLOCKSOURCE_PXI7     : 'TRIG/7',
    GxAo.GXAO_1649_CLOCKSOURCE_STAR     : 'PXI_Star',
    GxAo.GXAO_1649_CLOCKSOURCE_GROUPA   : 'GROUPA',
  }

  CLOCK_SOURCES_reverse = { v:k for k,v in CLOCK_SOURCES.items() }

  TRIGGER_SOURCES = {
    GxAo.GXAO_1649_TRIGGERMODE_SOFTWARE_ONLY  : 'software_only',
    GxAo.GXAO_1649_TRIGGERMODE_EXTERNAL       : 'external',
    GxAo.GXAO_1649_TRIGGERMODE_PXI0           : 'TRIG/0',
    GxAo.GXAO_1649_TRIGGERMODE_PXI1           : 'TRIG/1',
    GxAo.GXAO_1649_TRIGGERMODE_PXI2           : 'TRIG/2',
    GxAo.GXAO_1649_TRIGGERMODE_PXI3           : 'TRIG/3',
    GxAo.GXAO_1649_TRIGGERMODE_PXI4           : 'TRIG/4',
    GxAo.GXAO_1649_TRIGGERMODE_PXI5           : 'TRIG/5',
    GxAo.GXAO_1649_TRIGGERMODE_PXI6           : 'TRIG/6',
    GxAo.GXAO_1649_TRIGGERMODE_PXI7           : 'TRIG/7',
    GxAo.GXAO_1649_TRIGGERMODE_STAR           : 'PXI_Star',
    GxAo.GXAO_1649_TRIGGERMODE_GLOBAL         : 'GLOBAL',
  }

  TRIGGER_SOURCES_reverse = { v:k for k,v in TRIGGER_SOURCES.items() }

  STREAMING_STATUS = {
    (1<<0): 'FIFO is half empty',
    (1<<1): 'FIFO is empty',
    (1<<2): 'FIFO is full',
  }

  MAX_WAVEFORM_LEN = 256000



  def __init__(self, slot):
    """
    Create a binding to a given GX164x board.

    :param slot: the PCI bus/slot number to bind against
    """

    handle = ctypes.c_short(0)
    self._call(GxAo.GxAoInitialize, slot, byref(handle))
    self._handle = handle
    self.groups = [ Group(self, i) for i in range(4) ]
    self.name = self.board_summary.split()[0]

  def __getitem__(self, i):
    if type(i) is str:
      i = ord(i.upper()) - ord('A')
    return self.groups[i]

  @property
  def can_stream(self):
    return self.name in self.STREAM_DEVICES

  @property
  def can_waveform(self):
    return self.name in self.ARB_DEVICES

  def _call(self, function, *args):
    """
    Call a libGxAo function, automatically passing in a final argument
    byref(status), then raise an appropriate AoError if status != 0.

    :param function: the function in .clib.GxAo to call
    :param *args: the first N-1 arguments taken by the function (argument N
                  is assumed to be byref(status)
    """
    status = ctypes.c_short(0)
    args = args + (byref(status), )
    function(*args)

    if status.value != 0:
      err_str = create_string_buffer('', size=256)
      GxAo.GxAoGetErrorString(status, err_str, 256, byref(status))
      raise AoError(err_str.value)

  def reset(self):
    """
    Reset the board.

    The function does the following:
      - All groups' voltage ranges are set to 0-10V.
      - All channels of all groups are set to 0V.
      - All external updates are disabled
      - TTL out bit values are set to zero
      - All Channels set to Static mode (GX1649 Only)
      - All DIO Channels output disabled (GX1649 Only)
      - ARB memory size set to 1 (GX1649 Only)
      - ARB sample clock set to 100000 Hz
      - DIO memory size set to 1 (GX1649 Only)
      - DIO sample clock set to 100000 Hz
    """
    self._call(GxAo.GxAoReset, self._handle)

  def _call_summary(self, fn, buflen=256):
    """
    Call a GxAoGet*Summary() function which takes a handle,
    a string buffer, and the buffer's length.

    :param fn: the GxAo function to call
    :param buflen: the size of the string buffer to use
    :return: the fetched string
    """
    buf = ctypes.create_string_buffer(buflen)
    self._call(fn, self._handle, buf, sizeof(buf))
    return buf.value

  @property
  def driver_summary(self):
    """
    The Marvin Test GxAo driver info.

    :return: the driver information tuple(string, major_version, minor_version)
    """
    buf = ctypes.create_string_buffer(256)
    ver = ctypes.c_uint32()
    self._call(GxAo.GxAoGetDriverSummary, buf, sizeof(buf), byref(ver))
    ver = ver.value

    return (buf.value, ver >> 16, ver & 0xffff)

  @property
  def board_summary(self):
    """
    The board summary information as a string.

    :return: the board summary string
    """
    return self._call_summary(GxAo.GxAoGetBoardSummary)

  @property
  def calibration_info(self):
    """
    Returns the calibration information.

    The returned board's calibration information has the following fields:
    Model: model number, e.g. "GX1649"

    Serial Number: serial number, e.g. 216

    Control Number: Marvin Test Solutions control number, e.g. "ZZ-AD-AA-000"

    Production Calibration Date: Wed Oct 24 12:30:25 2010

    Calibration Date: Wed Oct 24 12:31:58 2010

    Recommended Interval: 1 year

    Next Calibration Date: Fri Oct 24 12:31:58 2011

    Status: calibration status can be either "Expired" followed by the number of
    days past expiration or "Current" followed by number of days until expire.

    Calibration License: can be either "Installed" with the calibration license
    number or "Not Installed".
    """
    buf = ctypes.create_string_buffer(1024)
    days = ctypes.c_short()
    self._call(GxAo.GxAoGetCalibrationInfo, self._handle, buf, sizeof(buf),
               byref(days))
    return days.value, buf.value.strip().split('\r\n')

  @property
  def board_accuracy(self):
    """
    Returns the board minimum per channel resolution.

    Board accuracy depends on the board factory installed output amplifier type.
    """
    value = ctypes.c_short(0)
    self._call(GxAo.GxAoGetBoardAccuracy, self._handle, byref(value))
    return {0: '2 mV', 1: '5 mV'}[value.value]


  def update(self):
    """
    Update all groups' channels outputs with the latest load values.
    """
    self._call(GxAo.GxAoUpdateAllGroupsVoltage, self._handle)






class Group(object):
  def __init__(self, board, group):
    self._board = board
    self._group = group

    self.channels = [ Channel(self, i) for i in range(16) ]

  def __getitem__(self, i):
    return self.channels[i]

  def __repr__(self):
    return 'Group<{}>'.format( chr( ord('A') + self._group ) )

  def _call(self, fn, *args):
    return self._board._call(fn, self._board._handle, self._group, *args)

  @property
  def range(self):
    R = ctypes.c_short(0)
    self._call(GxAo.GxAoGetGroupVoltageRange, byref(R))
    return self._board.RANGES[self._board.name][R.value]

  @range.setter
  def range(self, value):
    value = self._board.RANGES_reverse[self._board.name].get(value, value)

    self._call(GxAo.GxAoSetGroupVoltageRange, value)

  def reset(self):
    """
    Resets the specified group to the default state.

    The specified groups will be reset to:
      - Group's channels set to 0V.
      - Group's voltage range is set to 0-20V (GX1642) or 0-10 (GX1648).
      - External update is disabled
    """
    self._call(GxAo.GxAoResetGroup)

  def update(self):
    """
    Update all the specified group channels outputs with the load latest
    values. (i.e. software update)
    """
    self._call(GxAo.GxAoUpdateGroupVoltage)

  @property
  def external_update(self):
    value = GxAo.BOOL()
    self._call(GxAo.GxAoGetGroupExternalUpdate, byref(value))
    return bool(value.value)

  @external_update.setter
  def external_update(self, value):
    """
    En/Dis-ables the specified group external update.
    """
    self._call(GxAo.GxAoSetGroupExternalUpdate, GxAo.BOOL(bool(value)))

  @property
  def updated(self):
    """
    Returns whether the group channels loaded values were loaded to it DACs.

    Loading new value to any or all the specified group channels using
    GxAoSetChannelVoltage will set pbUpdated to FALSE. Updating the specified
    group channels will set load the value to the board DAC and will cause
    pbUpdated to return TRUE.
    """
    value = GxAo.BOOL()
    self._call(GxAo.GxAoGetGroupUpdateState, byref(value))
    return bool(value.value)


  # ### arbitrary waveform generation stuff ###
  def arm(self, continuous=True, disarm=False):
    """
    Arms or disables arming the specified group.

    Disabling arming the group (disarm=True) will cause the card to stop
    generating waveforms.
    """
    self._call(GxAo.GxAoArbArmGroup, int(not disarm), int(continuous))

  def disarm(self):
    """
    Disarms or disables arming the specified group.
    """
    self.arm(disarm=True)

  @property
  def trigger_source(self):
    """
    Returns the specified group trigger mode.

    Default trigger mode is software only (GXAO_1649_TRIGGERMODE_SOFTWARE_ONLY).
    Setting the trigger mode to global (GXAO_1649_TRIGGERMODE_GLOBAL)
    will allow global software trigger to trigger multiple groups at the same
    time.
    """
    if not self._board.can_waveform:
      return None
    value = ctypes.c_short()
    self._call(GxAo.GxAoArbGetGroupTrigger, byref(value))
    return self._board.TRIGGER_SOURCES[value.value]

  @trigger_source.setter
  def trigger_source(self, value):
    """
    Sets the specified group trigger mode.

    Default trigger mode is software only (GXAO_1649_TRIGGERMODE_SOFTWARE_ONLY).
    Setting the trigger mode to global (GXAO_1649_TRIGGERMODE_GLOBAL)
    will allow global software trigger to trigger multiple groups at the same
    time.
    """
    if not self._board.can_waveform:
      raise AoError('Cannot set trigger for board that cannot do waveforms')
    try:
      value = self._board.TRIGGER_SOURCES_reverse[value]
    except KeyError:
      raise AoError('expected trigger source to be one of {}'
                    .format(list(self._board.TRIGGER_SOURCES.values())))
    self._call(GxAo.GxAoArbSetGroupTrigger, value)

  def trigger(self):
    """
    Trigger the group and starts waveform generation.

    This function will start generating the waveform in all trigger modes. The
    group must be in armed state.
    """
    self._call(GxAo.GxAoArbTrigGroup)

  @property
  def streaming(self):
    """
    Returns the group streaming mode.

    The GX1649-1 ARB can operate in streaming or non-streaming mode. By default,
    each group (Group A-D) is set to non-streaming mode. When the board is in
    non-streaming mode, the ARB will use the onboard memory as a source for the
    waveform it will generate. When the board is in streaming mode, the ARB will
    continuously generate a waveform. The PC will write samples to a FIFO
    located on the ARB as needed to maintain the streaming operation.
    """
    if not self._board.can_stream:
      return False
    value = GxAo.BOOL()
    self._call(GxAo.GxAoArbIsGroupStreaming, byref(value))
    return bool(value.value)

  @streaming.setter
  def streaming(self, value):
    """
    Enables the group streaming mode.

    The GX1649-1 ARB can operate in streaming or non-streaming mode. By default,
    each group (Group A-D) is set to non-streaming mode. When the board is in
    non-streaming mode, the ARB will use the onboard memory as a source for the
    waveform it will generate. When the board is in streaming mode, the ARB will
    continuously generate a waveform. The PC will write samples to a FIFO
    located on the ARB as needed to maintain the streaming operation.
    """
    if not self._board.can_stream:
      raise AoError('Board cannot stream')
    value = GxAo.BOOL(value)
    self._call(GxAo.GxAoArbEnableGroupStreaming, value)

  @property
  def status(self):
    """
    Returns the group ARB sequencer status.

    All channels configured to generate waveform have the size waveform length.

    For streaming devices, this also returns the streaming status:
    The function returns the status of the streaming FIFO capacity. This can be
    used to determine when to write to the FIFO when streaming using the polling
    method (not using interrupts).
    """
    if not self._board.can_waveform:
      return dict()
    value = GxAo.DWORD()
    self._call(GxAo.GxAoArbGetGroupStatus, byref(value))
    status = dict(
      running     =bool(value.value & 0x1),
      armed_ready =bool(value.value & 0x2),
    )
    if self._board.can_stream:
      sstat = GxAo.WORD()
      count = GxAo.WORD()
      self._call(GxAo.GxAoArbGetGroupStreamingStatus, byref(sstat),byref(count))
      status.update(
        fifo_status = self._board.STREAMING_STATUS[sstat.value],
        fifo_samples = count.value,
      )
    return status

  @property
  def armed(self):
    return self.status['armed_ready']

  @property
  def running(self):
    return self.status['running']

  def get_waveform_params(self):
    value = GxAo.WORD()
    wvsz = GxAo.DWORD()
    self._call(GxAo.GxAoArbGetGroupChannels, byref(value), byref(wvsz))
    return dict(channels=value.value, per_channel_length=wvsz.value)

  def set_waveform_params(self, channels=None, per_channel_length=None):
    vals = self.get_waveform_params()
    if channels is not None:
      vals['channels'] = channels
    if per_channel_length is not None:
      vals['per_channel_length'] = per_channel_length
    self._call(GxAo.GxAoArbSetGroupChannels, vals['channels'],
               vals['per_channel_length'])

  @property
  def waveform_channels(self):
    V = self.get_waveform_params()['channels']
    return [i for i in range(16) if (V&(1<<i))]

  @waveform_channels.setter
  def waveform_channels(self, value):
    V = 0
    for i in value:
      if not 0 <= i <= 15:
        raise AoError('Cannot set non-existent channel: ' +str(i))
      V |= 1<<i
    return self.set_waveform_params(channels=V)

  @property
  def per_channel_length(self):
    return self.get_waveform_params()['per_channel_length']

  @per_channel_length.setter
  def per_channel_length(self, value):
    return self.set_waveform_params(per_channel_length=value)

  @property
  def max_waveform_len(self):
    lwc = len(self.waveform_channels)
    if lwc > 0:
      return (self._board.MAX_WAVEFORM_LEN//lwc)
    return None

  def _get_clock(self):
    if not self._board.can_waveform:
      return None
    clock = ctypes.c_short()
    freq = ctypes.c_double()
    self._call(GxAo.GxAoArbGetGroupClock, byref(clock), byref(freq))
    return clock.value, freq.value

  @property
  def clock(self):
    """
    Returns the specified group clock source and frequency.

    Default clock source is internal with frequency of 10MHz.

    GROUPA is only valid for groups B, C, and D.  Using group A clock source
    will synchronizes all group channels to use same clock source as group A.

    :param value: clock to use.  For an internal clock, a tuple like
    ('internal', <frequency>) should be used.

    :see Board.CLOCK_SOURCES: For valid clock sources.
    """
    if not self._board.can_waveform:
      return None
    clock, freq = self._get_clock()
    clock = self._board.CLOCK_SOURCES[clock]
    if clock == 'internal':
      return (clock, freq)
    return clock

  @clock.setter
  def clock(self, value):
    """
    Sets the specified group clock source and frequency.

    Default clock source is internal with frequency of 10MHz.

    GROUPA is only valid for groups B, C, and D.  Using group A clock source
    will synchronizes all group channels to use same clock source as group A.

    :param value: clock to use.  For an internal clock, a tuple like
    ('internal', <frequency>) should be used.
    """
    if not self._board.can_waveform:
      raise AoError('Cannot set clock for board that cannot do waveforms')
    if type(value) is not str:
      if len(value) != 2 or value[0] != 'internal':
        raise AoError('clock source only accepts tuple when source == '
                      '(\'internal\', frequency)')
      value, freq = value
    else:
      ignore, freq = self._get_clock()

    try:
      clock = self._board.CLOCK_SOURCES_reverse[value]
    except KeyError:
      raise AoError('expected clock source to be one of {}'
                    .format(list(self._board.CLOCK_SOURCES.values())))
    self._call(GxAo.GxAoArbSetGroupClock, clock, freq)




class Channel(object):
  def __init__(self, group, channel):
    self._group = group
    self._channel = channel

  def __repr__(self):
    return 'Channel<{}>'.format(self._channel)

  def _call(self, fn, *args):
    return self._group._call(fn, self._channel, *args)

  @property
  def voltage(self):
    """
    Returns the specified channel's group voltage.
    """
    value = ctypes.c_double()
    self._call(GxAo.GxAoGetChannelVoltage, byref(value))
    return value.value

  @voltage.setter
  def voltage(self, value):
    """
    Sets the specified channel's group voltage.

    The voltage must be in the group's voltage range otherwise the function
    returns an error.
    Calling this function will set GxAoGetGroupUpdateState to low (i.e. the
    group was updated).
    """
    self._call(GxAo.GxAoSetChannelVoltage, value)

  def load(self, value):
    """
    Load the specified groups' channel with new voltage value.

    Loading a channel with a new value does not affect the channels output. The
    channel's DAC will be programmed with the new value only after calling
    GxAoUpdateGroupVoltage. Calling GxAoSetChannelVoltage will only update all
    the channels in the specified group with their current loaded values. This
    function allows the user to load different values to different
    channels/groups and update all the channels at once.

    Calling this function will set GxAoGetGroupUpdateState to high (i.e. new
    value is waiting for the group to be updated).

    If the new voltage is out of range the function will return an error.
    """
    self._call(GxAo.GxAoLoadChannelVoltage, value)

  @property
  def updated(self):
    """
    Returns whether the channel's loaded values were loaded to it DACs.

    Loading new value to any or all the specified group channels using
    GxAoLoadChannelVoltage will set pbUpdated to FALSE. Updating the specified
    group channels will set load the value to the board DAC and will cause
    pbUpdated to return TRUE.
    """
    return self._group.updated

  def _get_waveform(self, wtype):
    if not self._group._board.can_waveform:
      return None

    dtype = {
      GxAo.GXAO_1649_WAVEFORM_TYPE_WORD : GxAo.WORD,
      GxAo.GXAO_1649_WAVEFORM_TYPE_DOUBLE : ctypes.c_double,
    }[wtype]
      
    sz = GxAo.DWORD(256000)
    waveform = np.ndarray(sz.value, dtype=dtype)
    self._call(GxAo.GxAoArbReadChannelWaveform,
               ctypes.c_void_p(waveform.ctypes.data),
               byref(sz), wtype)
    return np.resize(waveform, sz.value)

  def _set_waveform(self, waveform, wtype):
    if not self._group._board.can_waveform:
      raise AoError('Cannot set waveform for device without ARB capabilities')

    if self._channel not in self._group.waveform_channels:
      raise AoError('Cannot set waveform for channel not added to waveform')

    if len(waveform) > self._group.max_waveform_len:
      raise AoError('Trying to set too large a waveform')
    if len(waveform) != self._group.per_channel_length:
      raise AoError('Trying to set a waveform != in length to '
                    '{}.per_channel_length (={})'
                    .format(self._group, self._group.per_channel_length))

    dtype = {
      GxAo.GXAO_1649_WAVEFORM_TYPE_WORD : GxAo.WORD,
      GxAo.GXAO_1649_WAVEFORM_TYPE_DOUBLE : ctypes.c_double,
    }[wtype]

    # the following is supposed to ensure the correct type for the waveform
    # while only copying when absolutely necessary
    waveform = np.array(waveform, copy=False, dtype=dtype)
    self._call(GxAo.GxAoArbWriteChannelWaveform,
               ctypes.c_void_p(waveform.ctypes.data),
               len(waveform), wtype)

  @property
  def raw_waveform(self):
    """
    Returns the specified channel waveform to an array of 16-bit integers.
    """
    return self._get_waveform(GxAo.GXAO_1649_WAVEFORM_TYPE_WORD)

  @property
  def waveform(self):
    """
    Returns the specified channel waveform to an array of floats.
    """
    return self._get_waveform(GxAo.GXAO_1649_WAVEFORM_TYPE_DOUBLE)

  @raw_waveform.setter
  def raw_waveform(self, value):
    self._set_waveform(value, GxAo.GXAO_1649_WAVEFORM_TYPE_WORD)

  @waveform.setter
  def waveform(self, value):
    self._set_waveform(value, GxAo.GXAO_1649_WAVEFORM_TYPE_DOUBLE)
