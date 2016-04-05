from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxPRes.so'] = CDLL('libGxPRes.so')


# VOID = void # alias
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x0000000000000000a'
GT_NO_ERROR = 0 # Variable c_int '0'
GXPRES_PANEL_MODAL = 1 # Variable c_int '1'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x00000000000000005'
GT_INVALID_SLOT = -22 # Variable c_int '-0x00000000000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x00000000000000009'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x00000000000000001'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x00000000000000018'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x00000000000000006'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x00000000000000008'
GT_INVALID_ERROR = -20 # Variable c_int '-0x00000000000000014'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x00000000000000002'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x00000000000000004'
GT_WRONG_BOARD = -3 # Variable c_int '-0x00000000000000003'
GXPRES_PANEL_MODELESS = 0 # Variable c_int '0'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x00000000000000015'
GXPRES_INVALID_VALUE = -43 # Variable c_int '-0x0000000000000002b'
GXPRES_INVALID_CHANNEL = -40 # Variable c_int '-0x00000000000000028'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x00000000000000007'
GXPRES_INVALID_GROUP = -41 # Variable c_int '-0x00000000000000029'
GXPRES_INVALID_MODE = -42 # Variable c_int '-0x0000000000000002a'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x00000000000000017'
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
Gx1164Initialize = _libraries['libGxPRes.so'].Gx1164Initialize
Gx1164Initialize.restype = None
Gx1164Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx1164InitializeVisa = _libraries['libGxPRes.so'].Gx1164InitializeVisa
Gx1164InitializeVisa.restype = None
Gx1164InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx1164Reset = _libraries['libGxPRes.so'].Gx1164Reset
Gx1164Reset.restype = None
Gx1164Reset.argtypes = [SHORT, PSHORT]
Gx1164GetBoardSummary = _libraries['libGxPRes.so'].Gx1164GetBoardSummary
Gx1164GetBoardSummary.restype = None
Gx1164GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx1164GetChannelMode = _libraries['libGxPRes.so'].Gx1164GetChannelMode
Gx1164GetChannelMode.restype = None
Gx1164GetChannelMode.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx1164GetChannelResistanceRange = _libraries['libGxPRes.so'].Gx1164GetChannelResistanceRange
Gx1164GetChannelResistanceRange.restype = None
Gx1164GetChannelResistanceRange.argtypes = [SHORT, SHORT, BOOL, PDOUBLE, PDOUBLE, PSHORT]
Gx1164SetSingleChannelResistance = _libraries['libGxPRes.so'].Gx1164SetSingleChannelResistance
Gx1164SetSingleChannelResistance.restype = None
Gx1164SetSingleChannelResistance.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
Gx1164GetSingleChannelResistance = _libraries['libGxPRes.so'].Gx1164GetSingleChannelResistance
Gx1164GetSingleChannelResistance.restype = None
Gx1164GetSingleChannelResistance.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx1164SetDoubleChannelResistance = _libraries['libGxPRes.so'].Gx1164SetDoubleChannelResistance
Gx1164SetDoubleChannelResistance.restype = None
Gx1164SetDoubleChannelResistance.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
Gx1164GetDoubleChannelResistance = _libraries['libGxPRes.so'].Gx1164GetDoubleChannelResistance
Gx1164GetDoubleChannelResistance.restype = None
Gx1164GetDoubleChannelResistance.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx1164SetWiperMode = _libraries['libGxPRes.so'].Gx1164SetWiperMode
Gx1164SetWiperMode.restype = None
Gx1164SetWiperMode.argtypes = [SHORT, SHORT, BOOL, PSHORT]
Gx1164GetWiperMode = _libraries['libGxPRes.so'].Gx1164GetWiperMode
Gx1164GetWiperMode.restype = None
Gx1164GetWiperMode.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx1164SetChannelRelays = _libraries['libGxPRes.so'].Gx1164SetChannelRelays
Gx1164SetChannelRelays.restype = None
Gx1164SetChannelRelays.argtypes = [SHORT, SHORT, BYTE, PSHORT]
Gx1164GetChannelRelays = _libraries['libGxPRes.so'].Gx1164GetChannelRelays
Gx1164GetChannelRelays.restype = None
Gx1164GetChannelRelays.argtypes = [SHORT, SHORT, PBYTE, PSHORT]
__all__ = ['GT_BOARD_INVALID_EEPROM', 'Gx1164GetChannelRelays',
           'SHORT', 'PCSTR', 'PDWORD',
           'Gx1164SetSingleChannelResistance', 'GT_NO_ERROR',
           'Gx1164Initialize', 'GXPRES_PANEL_MODAL',
           'GT_UNABLE_REGISTER_DEVICE', 'Gx1164GetBoardSummary',
           'GT_INVALID_SLOT', 'GT_UNABLE_TO_GETTIMER', 'Gx1164Reset',
           'GT_CANT_OPEN_HW', 'DWORD', 'DDWORD', 'HWND',
           'GT_INVALID_STRLEN', 'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'Gx1164GetWiperMode', 'Gx1164GetSingleChannelResistance',
           'LONG', 'Gx1164SetDoubleChannelResistance', 'PSHORT',
           'Gx1164GetChannelMode', 'GT_INVALID_PARAMETER',
           'GT_INVALID_ERROR', 'Gx1164SetWiperMode',
           'Gx1164GetChannelResistanceRange', 'CHAR', 'PWORD',
           'Gx1164InitializeVisa', 'GT_BOARD_NOT_EXIST', 'PBOOL',
           'Gx1164GetDoubleChannelResistance', 'PSTR',
           'Gx1164SetChannelRelays', 'GT_SLOT_NOT_CONFIG',
           'GT_WRONG_BOARD', 'GXPRES_PANEL_MODELESS',
           'GT_UNABLE_CREATE_PANEL', 'PDOUBLE', 'WORD', 'BYTE',
           'GXPRES_INVALID_VALUE', 'GXPRES_INVALID_CHANNEL', 'PVOID',
           'INT', 'GT_UNABLE_ALLOC_MEMORY', 'PBYTE', 'PDDWORD',
           'GXPRES_INVALID_GROUP', 'GXPRES_INVALID_MODE', 'BOOL',
           'DOUBLE', 'UINT', 'GT_INVALID_HANDLE', 'PLONG']
