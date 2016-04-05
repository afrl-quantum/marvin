from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxPxi.so'] = CDLL('libGxPxi.so')


# VOID = void # alias
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x0000000000000000a'
GXPXI_INVALID_ERROR = -99 # Variable c_int '-0x00000000000000063'
GX7404_CHANNEL_INTERNAL = 4 # Variable c_int '4'
GT_INVALID_MODE = -25 # Variable c_int '-0x00000000000000019'
GX7404_ONBOARD_CHANNEL_PLUS15 = 5 # Variable c_int '5'
GT_NO_ERROR = 0 # Variable c_int '0'
GX7404_ONBOARD_CHANNEL_PLUS12 = 4 # Variable c_int '4'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x00000000000000005'
GT_INVALID_SLOT = -22 # Variable c_int '-0x00000000000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x00000000000000009'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x0000000000000000b'
GT_PARAMETER_OUT_OF_RANGE = -26 # Variable c_int '-0x0000000000000001a'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x00000000000000001'
GXPXI_STATE_OPEN = 0 # Variable c_int '0'
GXPXI_INVALID_BOARD_PCB_VER = -45 # Variable c_int '-0x0000000000000002d'
GXPXI_TIMEOUT_CURRENT_READ = -71 # Variable c_int '-0x00000000000000047'
GXPXI_PANEL_MODELESS = 0 # Variable c_int '0'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x00000000000000018'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x00000000000000006'
GX7404_ONBOARD_CHANNEL_PLUS3_3 = 2 # Variable c_int '2'
GXPXI_STATE_CLOSE = 1 # Variable c_int '1'
GX7404_ONBOARD_CHANNEL_NOT_INSTALLED = 0 # Variable c_int '0'
GXPXI_INVALID_VOLTAGE_RANGE = -41 # Variable c_int '-0x00000000000000029'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x0000000000000000d'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x00000000000000015'
GT_INVALID_ERROR = -20 # Variable c_int '-0x00000000000000014'
GXPXI_TIMEOUT_VOLTAGE_READ = -70 # Variable c_int '-0x00000000000000046'
GXPXI_EXTERNAL_RESET = -72 # Variable c_int '-0x00000000000000048'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x00000000000000002'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x00000000000000004'
GT_WRONG_BOARD = -3 # Variable c_int '-0x00000000000000003'
GXPXI_INVALID_CHANNEL = -40 # Variable c_int '-0x00000000000000028'
GX7404_CHANNEL_NEGATIVE12 = 3 # Variable c_int '3'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x00000000000000008'
GX7404_CHANNEL_PLUS5 = 0 # Variable c_int '0'
GXPXI_PANEL_MODAL = 1 # Variable c_int '1'
GXPXI_ERR_VOLTAGE_OUT_OF_RANGE = -42 # Variable c_int '-0x0000000000000002a'
GX7404_CHANNEL_PLUS3_3 = 1 # Variable c_int '1'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x00000000000000007'
GXPXI_CHANNEL_NOT_CONNECTED = -44 # Variable c_int '-0x0000000000000002c'
GXPXI_CHANNEL_BUSY_TIMEOUT = -43 # Variable c_int '-0x0000000000000002b'
GX7404_ONBOARD_CHANNEL_PLUS9 = 3 # Variable c_int '3'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x0000000000000000c'
GX7404_ONBOARD_CHANNEL_PLUS5 = 1 # Variable c_int '1'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x00000000000000017'
GX7404_CHANNEL_PLUS12 = 2 # Variable c_int '2'
CHAR = c_char
BYTE = c_ubyte
SHORT = c_short
WORD = c_ushort
INT = c_int
UINT = c_uint
LONG = c_int
DWORD = c_uint
DDWORD = c_ulonglong
DOUBLE = c_double
BOOL = c_int
PBOOL = POINTER(BOOL)
PSHORT = POINTER(SHORT)
PWORD = POINTER(WORD)
PLONG = POINTER(LONG)
PDWORD = POINTER(DWORD)
PDDWORD = POINTER(DDWORD)
PDOUBLE = POINTER(DOUBLE)
PVOID = c_void_p
PSTR = STRING
PBYTE = POINTER(BYTE)
HWND = c_void_p
PCSTR = STRING
GxPxiGetErrorString = _libraries['libGxPxi.so'].GxPxiGetErrorString
GxPxiGetErrorString.restype = None
GxPxiGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxPxiGetDriverSummary = _libraries['libGxPxi.so'].GxPxiGetDriverSummary
GxPxiGetDriverSummary.restype = None
GxPxiGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
Gx7404Initialize = _libraries['libGxPxi.so'].Gx7404Initialize
Gx7404Initialize.restype = None
Gx7404Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx7404Reset = _libraries['libGxPxi.so'].Gx7404Reset
Gx7404Reset.restype = None
Gx7404Reset.argtypes = [SHORT, PSHORT]
Gx7404GetBoardSummary = _libraries['libGxPxi.so'].Gx7404GetBoardSummary
Gx7404GetBoardSummary.restype = None
Gx7404GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx7404ConnectChannel = _libraries['libGxPxi.so'].Gx7404ConnectChannel
Gx7404ConnectChannel.restype = None
Gx7404ConnectChannel.argtypes = [SHORT, SHORT, BOOL, PSHORT]
Gx7404ConnectChannels = _libraries['libGxPxi.so'].Gx7404ConnectChannels
Gx7404ConnectChannels.restype = None
Gx7404ConnectChannels.argtypes = [SHORT, BYTE, PSHORT]
Gx7404GetChannel = _libraries['libGxPxi.so'].Gx7404GetChannel
Gx7404GetChannel.restype = None
Gx7404GetChannel.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx7404GetChannels = _libraries['libGxPxi.so'].Gx7404GetChannels
Gx7404GetChannels.restype = None
Gx7404GetChannels.argtypes = [SHORT, PBYTE, PSHORT]
Gx7404GetChannelCurrent = _libraries['libGxPxi.so'].Gx7404GetChannelCurrent
Gx7404GetChannelCurrent.restype = None
Gx7404GetChannelCurrent.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx7404GetChannelVoltage = _libraries['libGxPxi.so'].Gx7404GetChannelVoltage
Gx7404GetChannelVoltage.restype = None
Gx7404GetChannelVoltage.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx7404GetExternalDisableState = _libraries['libGxPxi.so'].Gx7404GetExternalDisableState
Gx7404GetExternalDisableState.restype = None
Gx7404GetExternalDisableState.argtypes = [SHORT, PBOOL, PSHORT]
Gx7404GetOnBoardChannelType = _libraries['libGxPxi.so'].Gx7404GetOnBoardChannelType
Gx7404GetOnBoardChannelType.restype = None
Gx7404GetOnBoardChannelType.argtypes = [SHORT, PSHORT, PSHORT]
__all__ = ['GT_BOARD_INVALID_EEPROM', 'GXPXI_INVALID_ERROR',
           'GX7404_CHANNEL_INTERNAL', 'SHORT',
           'GX7404_ONBOARD_CHANNEL_PLUS3_3',
           'Gx7404GetExternalDisableState',
           'GX7404_ONBOARD_CHANNEL_PLUS15', 'PCSTR', 'PDWORD',
           'Gx7404GetChannels', 'GT_NO_ERROR',
           'GX7404_ONBOARD_CHANNEL_PLUS12', 'CHAR',
           'GT_UNABLE_REGISTER_DEVICE', 'GT_INVALID_SLOT',
           'GT_UNABLE_TO_GETTIMER', 'Gx7404Reset',
           'GT_NOT_IN_CALIBRATION_MODE', 'GT_PARAMETER_OUT_OF_RANGE',
           'GT_CANT_OPEN_HW', 'DWORD', 'Gx7404GetChannelVoltage',
           'GXPXI_STATE_OPEN', 'GXPXI_INVALID_BOARD_PCB_VER',
           'GXPXI_TIMEOUT_CURRENT_READ', 'GXPXI_PANEL_MODELESS',
           'HWND', 'Gx7404GetChannel', 'GT_INVALID_STRLEN',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE', 'GT_INVALID_MODE',
           'GXPXI_STATE_CLOSE', 'Gx7404GetChannelCurrent',
           'GX7404_ONBOARD_CHANNEL_NOT_INSTALLED', 'LONG',
           'Gx7404GetOnBoardChannelType',
           'GXPXI_INVALID_VOLTAGE_RANGE', 'DDWORD',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GT_INVALID_PARAMETER',
           'GT_INVALID_ERROR', 'GxPxiGetErrorString', 'BYTE',
           'GXPXI_TIMEOUT_VOLTAGE_READ', 'GXPXI_EXTERNAL_RESET',
           'GT_BOARD_NOT_EXIST', 'PBOOL', 'PLONG', 'PSTR',
           'Gx7404ConnectChannels', 'GT_SLOT_NOT_CONFIG', 'PDDWORD',
           'GT_WRONG_BOARD', 'GXPXI_INVALID_CHANNEL', 'UINT',
           'GX7404_CHANNEL_NEGATIVE12', 'GT_UNABLE_CREATE_PANEL',
           'GX7404_CHANNEL_PLUS5', 'WORD', 'GXPXI_PANEL_MODAL',
           'Gx7404ConnectChannel', 'GXPXI_ERR_VOLTAGE_OUT_OF_RANGE',
           'GxPxiGetDriverSummary', 'PSHORT', 'Gx7404Initialize',
           'PVOID', 'GX7404_CHANNEL_PLUS3_3', 'INT',
           'GT_UNABLE_ALLOC_MEMORY', 'PBYTE', 'PDOUBLE',
           'GXPXI_CHANNEL_NOT_CONNECTED',
           'GXPXI_CHANNEL_BUSY_TIMEOUT', 'Gx7404GetBoardSummary',
           'BOOL', 'GX7404_ONBOARD_CHANNEL_PLUS9', 'PWORD',
           'GT_NOT_CALIBRATED', 'DOUBLE',
           'GX7404_ONBOARD_CHANNEL_PLUS5', 'GT_INVALID_HANDLE',
           'GX7404_CHANNEL_PLUS12']
