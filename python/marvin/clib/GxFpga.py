from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxFpga.so'] = CDLL('libGxFpga.so')


# VOID = void # alias
GXFPGA_DMA_READ_TIMEOUT = -66 # Variable c_int '-0x000000042'
GT_FIRMWARE_UPGRADE_MODE_SYNC = 0 # Variable c_int '0'
GXFPGA_3571_VIDEO_MODE_NTSC = 2 # Variable c_int '2'
GXFPGA_EXPANSION_BOARD_NOT_FOUND = -59 # Variable c_int '-0x00000003b'
GT_NO_ERROR = 0 # Variable c_int '0'
GXFPGA_BYPASS_BANK_C = 4 # Variable c_int '4'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x000000005'
GXFPGA_EEPROM_INVALID_TIME_STAMP = -70 # Variable c_int '-0x000000046'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x000000018'
GXFPGA_EXPANSION_BOARD_ID_3509 = 9 # Variable c_int '9'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x000000008'
GXFPGA_LOAD_MODE_ASYNC = 1 # Variable c_int '1'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x000000002'
GXFPGA_BOARD_TYPE_GX3500E = 2 # Variable c_int '2'
GXFPGA_MEMORY_BAR4 = 4 # Variable c_int '4'
GXFPGA_MEMORY_BAR1 = 1 # Variable c_int '1'
GXFPGA_INVALID_DMA_DATA_SIZE = -64 # Variable c_int '-0x000000040'
GXFPGA_MEMORY_BAR3 = 3 # Variable c_int '3'
GXFPGA_MEMORY_BAR2 = 2 # Variable c_int '2'
GXFPGA_PIO_GROUP_D = 3 # Variable c_int '3'
GXFPGA_PIO_GROUP_A = 0 # Variable c_int '0'
GXFPGA_PIO_GROUP_C = 2 # Variable c_int '2'
GXFPGA_PIO_GROUP_B = 1 # Variable c_int '1'
GXFPGA_EXPANSION_BOARD_ID_5731 = 8 # Variable c_int '8'
GXFPGA_3571_COLOR_BLUE = 1020 # Variable c_int '1020'
GT_FIRMWARE_UPGRADE_MODE_ASYNC = 1 # Variable c_int '1'
GT_EVENT_TMO_IMMEDIATE = 0 # Variable c_int '0'
GXFPGA_LOAD_MODE_SYNC = 0 # Variable c_int '0'
GXFPGA_EEPROM_WRITE_TIMEOUT = -72 # Variable c_int '-0x000000048'
GXFPGA_DMA_WRITE_TIMEOUT = -67 # Variable c_int '-0x000000043'
GXFPGA_WARNINGS_DMA_BUSY = 10 # Variable c_int '10'
GXFPGA_3571_COLOR_MAGENTA = 1069548540 # Variable c_int '1069548540'
GT_EVENT_WAIT_TIMEOUT = -43 # Variable c_int '-0x00000002b'
GXFPGA_FLEX_PROGRAM_FAILURE = -60 # Variable c_int '-0x00000003c'
GXFPGA_3571_VIDEO_MODE_VGA = 1 # Variable c_int '1'
GXFPGA_3571_MODELINE_SCROLL_VERTICAL = 1 # Variable c_int '1'
GXFPGA_3571_MODELINE_SIGNAL_SYNC = 0 # Variable c_int '0'
GXFPGA_BOARD_TYPE_GX3700 = 3 # Variable c_int '3'
GXFPGA_BYPASS_BANK_D = 8 # Variable c_int '8'
GXFPGA_BYPASS_ALL = 15 # Variable c_int '15'
GXFPGA_BYPASS_BANK_B = 2 # Variable c_int '2'
GXFPGA_BOARD_TYPE_GX3700E = 4 # Variable c_int '4'
GXFPGA_BYPASS_BANK_A = 1 # Variable c_int '1'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x000000015'
GXFPGA_ERROR_VOLATILE_PROGRAMMING = -53 # Variable c_int '-0x000000035'
GXFPGA_3571_MODELINE_SIGNAL_FRONT_PORCH = 1 # Variable c_int '1'
GT_VISA_GETATTRIBUTE_ERROR = -33 # Variable c_int '-0x000000021'
GXFPGA_EXTERNAL_PROGRAMMER_DETECTED = -55 # Variable c_int '-0x000000037'
GXFPGA_3571_COLOR_CYAN = 1045500 # Variable c_int '1045500'
GXFPGA_EEPROM_READ_TIMEOUT = -71 # Variable c_int '-0x000000047'
GXFPGA_IMAGE_HEIGHT = 480 # Variable c_int '480'
GT_EVENT_ALL = 65535 # Variable c_int '65535'
GT_VISA_OPEN_ERROR = -32 # Variable c_int '-0x000000020'
GT_VISA_OPENDEFAULTRM_ERROR = -31 # Variable c_int '-0x00000001f'
GXFPGA_PIO_DIRECTION_OUTPUT = 1 # Variable c_int '1'
GXFPGA_DMA_WRITE = 1 # Variable c_int '1'
GT_INVALID_MODE = -25 # Variable c_int '-0x000000019'
GXFPGA_3571_MODELINE_SIGNAL_BACK_PORCH = 3 # Variable c_int '3'
GXFPGA_3571_COLOR_YELLOW = 1070592000 # Variable c_int '1070592000'
GT_VISA_MEMMAP_ERROR = -35 # Variable c_int '-0x000000023'
GXFPGA_PIO_DIRECTION_INPUT = 0 # Variable c_int '0'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x00000000b'
GXFPGA_3571_COLOR_WHITE = 1070593020 # Variable c_int '1070593020'
GXFPGA_PANEL_MODELESS = 0 # Variable c_int '0'
GXFPGA_EXPANSION_BOARD_ID_3540 = 2 # Variable c_int '2'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x000000006'
GXFPGA_FLEX_RELOAD_ERROR = -57 # Variable c_int '-0x000000039'
GXFPGA_PANEL_MODAL = 1 # Variable c_int '1'
GXFPGA_UNKNOWN_BOARD_TYPE = 0 # Variable c_int '0'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x00000000d'
GXFPGA_INVALID_FILENAME = -51 # Variable c_int '-0x000000033'
GXFPGA_EXPANSION_BOARD_ID_NONE = 15 # Variable c_int '15'
GXFPGA_BYPASS_NONE = 0 # Variable c_int '0'
GXFPGA_3571_COLOR_GREEN = 1044480 # Variable c_int '1044480'
GXFPGA_SIZE_NOT_DWORD = -58 # Variable c_int '-0x00000003a'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x000000004'
GT_WRONG_BOARD = -3 # Variable c_int '-0x000000003'
GXFPGA_BOARD_TYPE_GX3500 = 1 # Variable c_int '1'
GXFPGA_LOAD_TARGET_VOLATILE = 0 # Variable c_int '0'
GXFPGA_DMA_READ = 0 # Variable c_int '0'
GT_INVALID_ERROR = -20 # Variable c_int '-0x000000014'
GXFPGA_ERROR_EEPROM_PROGRAMMING = -54 # Variable c_int '-0x000000036'
GT_VISA_LOAD_DLL_ERROR = -30 # Variable c_int '-0x00000001e'
GT_EVENT_INTERRUPT = 1 # Variable c_int '1'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x00000000c'
GXFPGA_3571_COLOR_RED = 1069547520 # Variable c_int '1069547520'
GT_VISA_VIIN_ERROR = -34 # Variable c_int '-0x000000022'
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x00000000a'
GXFPGA_3571_MODELINE_SCROLL_HORIZONTAL = 0 # Variable c_int '0'
GT_INVALID_SLOT = -22 # Variable c_int '-0x000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x000000009'
GT_PARAMETER_OUT_OF_RANGE = -26 # Variable c_int '-0x00000001a'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x000000001'
GXFPGA_3571_VIDEO_MODE_STANDBY = 0 # Variable c_int '0'
GXFPGA_INVALID_DMA_OFFSET = -65 # Variable c_int '-0x000000041'
GXFPGA_ERROR_OFFSET = -62 # Variable c_int '-0x00000003e'
GXFPGA_3571_COLOR_BLACK = 0 # Variable c_int '0'
GXFPGA_INVALID_DATA_WIDTH = -63 # Variable c_int '-0x00000003f'
GXFPGA_EXPANSION_BOARD_ID_PIO = 1 # Variable c_int '1'
GXFPGA_ERROR_DATA_WIDTH_AND_NUM_BYTES = -61 # Variable c_int '-0x00000003d'
GT_EVENT_DISABLE_FAILED = -42 # Variable c_int '-0x00000002a'
GT_EVENT_WAIT_ERROR = -44 # Variable c_int '-0x00000002c'
GXFPGA_IMAGE_WIDTH = 640 # Variable c_int '640'
GXFPGA_OFFSET_OUT_OF_RANGE = -50 # Variable c_int '-0x000000032'
GT_EVENT_ENABLE_FAILED = -41 # Variable c_int '-0x000000029'
GXFPGA_LOAD_TARGET_EEPROM = 1 # Variable c_int '1'
GT_EVENT_TMO_INFINITE = 4294967295L # Variable c_uint '-1u'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x000000007'
GXFPGA_BUSY_LOAD_IN_PROGRESS = -56 # Variable c_int '-0x000000038'
GXFPGA_EXPANSION_BOARD_ID_3510 = 10 # Variable c_int '10'
GXFPGA_3571_MODELINE_SIGNAL_SYNC_PULSE = 2 # Variable c_int '2'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x000000017'
GXFPGA_ERROR_FILE_OPEN = -52 # Variable c_int '-0x000000034'
CHAR = c_char
BYTE = c_ubyte
SHORT = c_short
WORD = c_ushort
INT = c_int
UINT = c_uint
LONG = c_long
DWORD = c_ulong
DOUBLE = c_double
BOOL = c_int
PBOOL = POINTER(BOOL)
PSHORT = POINTER(SHORT)
PWORD = POINTER(WORD)
PLONG = POINTER(LONG)
PDWORD = POINTER(DWORD)
PDOUBLE = POINTER(DOUBLE)
PVOID = c_void_p
PSTR = STRING
PBYTE = POINTER(BYTE)
HWND = c_void_p
PCSTR = STRING
GxFpgaGetErrorString = _libraries['libGxFpga.so'].GxFpgaGetErrorString
GxFpgaGetErrorString.restype = None
GxFpgaGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxFpgaGetDriverSummary = _libraries['libGxFpga.so'].GxFpgaGetDriverSummary
GxFpgaGetDriverSummary.restype = None
GxFpgaGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
GxFpgaInitialize = _libraries['libGxFpga.so'].GxFpgaInitialize
GxFpgaInitialize.restype = None
GxFpgaInitialize.argtypes = [SHORT, PSHORT, PSHORT]
GxFpgaInitializeVisa = _libraries['libGxFpga.so'].GxFpgaInitializeVisa
GxFpgaInitializeVisa.restype = None
GxFpgaInitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
GxFpgaReset = _libraries['libGxFpga.so'].GxFpgaReset
GxFpgaReset.restype = None
GxFpgaReset.argtypes = [SHORT, PSHORT]
GxFpgaGetBoardSummary = _libraries['libGxFpga.so'].GxFpgaGetBoardSummary
GxFpgaGetBoardSummary.restype = None
GxFpgaGetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxFpgaGetEepromSummary = _libraries['libGxFpga.so'].GxFpgaGetEepromSummary
GxFpgaGetEepromSummary.restype = None
GxFpgaGetEepromSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxFpgaGetBoardType = _libraries['libGxFpga.so'].GxFpgaGetBoardType
GxFpgaGetBoardType.restype = None
GxFpgaGetBoardType.argtypes = [SHORT, PSHORT, PSHORT]
GxFpgaLoad = _libraries['libGxFpga.so'].GxFpgaLoad
GxFpgaLoad.restype = None
GxFpgaLoad.argtypes = [SHORT, SHORT, PCSTR, SHORT, PSHORT]
GxFpgaLoadFromEeprom = _libraries['libGxFpga.so'].GxFpgaLoadFromEeprom
GxFpgaLoadFromEeprom.restype = None
GxFpgaLoadFromEeprom.argtypes = [SHORT, PSHORT]
GxFpgaLoadStatus = _libraries['libGxFpga.so'].GxFpgaLoadStatus
GxFpgaLoadStatus.restype = None
GxFpgaLoadStatus.argtypes = [SHORT, PSHORT, PSHORT]
GxFpgaWriteRegister = _libraries['libGxFpga.so'].GxFpgaWriteRegister
GxFpgaWriteRegister.restype = None
GxFpgaWriteRegister.argtypes = [SHORT, DWORD, PVOID, DWORD, PSHORT]
GxFpgaReadRegister = _libraries['libGxFpga.so'].GxFpgaReadRegister
GxFpgaReadRegister.restype = None
GxFpgaReadRegister.argtypes = [SHORT, DWORD, PVOID, DWORD, PSHORT]
GxFpgaWriteMemory = _libraries['libGxFpga.so'].GxFpgaWriteMemory
GxFpgaWriteMemory.restype = None
GxFpgaWriteMemory.argtypes = [SHORT, DWORD, PVOID, DWORD, PSHORT]
GxFpgaReadMemory = _libraries['libGxFpga.so'].GxFpgaReadMemory
GxFpgaReadMemory.restype = None
GxFpgaReadMemory.argtypes = [SHORT, DWORD, PVOID, DWORD, PSHORT]
GxFpgaRead = _libraries['libGxFpga.so'].GxFpgaRead
GxFpgaRead.restype = None
GxFpgaRead.argtypes = [SHORT, SHORT, DWORD, PVOID, SHORT, DWORD, PSHORT]
GxFpgaWrite = _libraries['libGxFpga.so'].GxFpgaWrite
GxFpgaWrite.restype = None
GxFpgaWrite.argtypes = [SHORT, SHORT, DWORD, PVOID, SHORT, DWORD, PSHORT]
GxFpgaSetExpansionBoardBypass = _libraries['libGxFpga.so'].GxFpgaSetExpansionBoardBypass
GxFpgaSetExpansionBoardBypass.restype = None
GxFpgaSetExpansionBoardBypass.argtypes = [SHORT, BYTE, PSHORT]
GxFpgaGetExpansionBoardBypass = _libraries['libGxFpga.so'].GxFpgaGetExpansionBoardBypass
GxFpgaGetExpansionBoardBypass.restype = None
GxFpgaGetExpansionBoardBypass.argtypes = [SHORT, PBYTE, PSHORT]
GxFpgaGetExpansionBoardID = _libraries['libGxFpga.so'].GxFpgaGetExpansionBoardID
GxFpgaGetExpansionBoardID.restype = None
GxFpgaGetExpansionBoardID.argtypes = [SHORT, PBYTE, PSHORT]
Gt_EventCallback = CFUNCTYPE(LONG, SHORT, SHORT, PVOID)
GxFpgaSetEvent = _libraries['libGxFpga.so'].GxFpgaSetEvent
GxFpgaSetEvent.restype = None
GxFpgaSetEvent.argtypes = [SHORT, SHORT, BOOL, Gt_EventCallback, PVOID, PSHORT]
GxFpgaDiscardEvents = _libraries['libGxFpga.so'].GxFpgaDiscardEvents
GxFpgaDiscardEvents.restype = None
GxFpgaDiscardEvents.argtypes = [SHORT, SHORT, PSHORT]
GxFpgaWaitOnEvent = _libraries['libGxFpga.so'].GxFpgaWaitOnEvent
GxFpgaWaitOnEvent.restype = None
GxFpgaWaitOnEvent.argtypes = [SHORT, SHORT, LONG, PSHORT]
GxFpgaDmaGetTransferStatus = _libraries['libGxFpga.so'].GxFpgaDmaGetTransferStatus
GxFpgaDmaGetTransferStatus.restype = None
GxFpgaDmaGetTransferStatus.argtypes = [SHORT, PSHORT, PSHORT]
GxFpgaDmaTransfer = _libraries['libGxFpga.so'].GxFpgaDmaTransfer
GxFpgaDmaTransfer.restype = None
GxFpgaDmaTransfer.argtypes = [SHORT, BOOL, PVOID, SHORT, DWORD, DWORD, PVOID, PSHORT]
GxFpgaDmaFreeMemory = _libraries['libGxFpga.so'].GxFpgaDmaFreeMemory
GxFpgaDmaFreeMemory.restype = None
GxFpgaDmaFreeMemory.argtypes = [SHORT, PSHORT]
GxFpgaUpgradeFirmware = _libraries['libGxFpga.so'].GxFpgaUpgradeFirmware
GxFpgaUpgradeFirmware.restype = None
GxFpgaUpgradeFirmware.argtypes = [SHORT, PCSTR, SHORT, PSHORT]
GxFpgaUpgradeFirmwareStatus = _libraries['libGxFpga.so'].GxFpgaUpgradeFirmwareStatus
GxFpgaUpgradeFirmwareStatus.restype = None
GxFpgaUpgradeFirmwareStatus.argtypes = [SHORT, PSTR, SHORT, PSHORT, PBOOL, PSHORT]
GxFpga3571Reset = _libraries['libGxFpga.so'].GxFpga3571Reset
GxFpga3571Reset.restype = None
GxFpga3571Reset.argtypes = [SHORT, PSHORT]
GxFpga3571LoadFile = _libraries['libGxFpga.so'].GxFpga3571LoadFile
GxFpga3571LoadFile.restype = None
GxFpga3571LoadFile.argtypes = [SHORT, PCSTR, PSHORT]
GxFpga3571LoadColor = _libraries['libGxFpga.so'].GxFpga3571LoadColor
GxFpga3571LoadColor.restype = None
GxFpga3571LoadColor.argtypes = [SHORT, DWORD, PSHORT]
GxFpga3571LoadArray = _libraries['libGxFpga.so'].GxFpga3571LoadArray
GxFpga3571LoadArray.restype = None
GxFpga3571LoadArray.argtypes = [SHORT, PBYTE, PSHORT]
GxFpga3571SetModeline = _libraries['libGxFpga.so'].GxFpga3571SetModeline
GxFpga3571SetModeline.restype = None
GxFpga3571SetModeline.argtypes = [SHORT, SHORT, SHORT, DWORD, PSHORT]
GxFpga3571ResetModeline = _libraries['libGxFpga.so'].GxFpga3571ResetModeline
GxFpga3571ResetModeline.restype = None
GxFpga3571ResetModeline.argtypes = [SHORT, PSHORT]
GxFpga3571SetVideoMode = _libraries['libGxFpga.so'].GxFpga3571SetVideoMode
GxFpga3571SetVideoMode.restype = None
GxFpga3571SetVideoMode.argtypes = [SHORT, SHORT, PSHORT]
GxFpga3571GetVideoMode = _libraries['libGxFpga.so'].GxFpga3571GetVideoMode
GxFpga3571GetVideoMode.restype = None
GxFpga3571GetVideoMode.argtypes = [SHORT, PSHORT, PSHORT]
GxFpga3571SetAdvancedMode = _libraries['libGxFpga.so'].GxFpga3571SetAdvancedMode
GxFpga3571SetAdvancedMode.restype = None
GxFpga3571SetAdvancedMode.argtypes = [SHORT, BOOL, PSHORT]
GxFpga3571GetAdvancedMode = _libraries['libGxFpga.so'].GxFpga3571GetAdvancedMode
GxFpga3571GetAdvancedMode.restype = None
GxFpga3571GetAdvancedMode.argtypes = [SHORT, PBOOL, PSHORT]
GxFpgaPioReset = _libraries['libGxFpga.so'].GxFpgaPioReset
GxFpgaPioReset.restype = None
GxFpgaPioReset.argtypes = [SHORT, PSHORT]
GxFpgaPioSetGroup = _libraries['libGxFpga.so'].GxFpgaPioSetGroup
GxFpgaPioSetGroup.restype = None
GxFpgaPioSetGroup.argtypes = [SHORT, SHORT, DWORD, PSHORT]
GxFpgaPioGetGroup = _libraries['libGxFpga.so'].GxFpgaPioGetGroup
GxFpgaPioGetGroup.restype = None
GxFpgaPioGetGroup.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
GxFpgaPioSetGroupDirection = _libraries['libGxFpga.so'].GxFpgaPioSetGroupDirection
GxFpgaPioSetGroupDirection.restype = None
GxFpgaPioSetGroupDirection.argtypes = [SHORT, SHORT, DWORD, PSHORT]
GxFpgaPioSetChannelDirection = _libraries['libGxFpga.so'].GxFpgaPioSetChannelDirection
GxFpgaPioSetChannelDirection.restype = None
GxFpgaPioSetChannelDirection.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
GxFpgaPioGetGroupDirection = _libraries['libGxFpga.so'].GxFpgaPioGetGroupDirection
GxFpgaPioGetGroupDirection.restype = None
GxFpgaPioGetGroupDirection.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
GxFpgaPioGetChannelDirection = _libraries['libGxFpga.so'].GxFpgaPioGetChannelDirection
GxFpgaPioGetChannelDirection.restype = None
GxFpgaPioGetChannelDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
GxFpgaPioSetChannel = _libraries['libGxFpga.so'].GxFpgaPioSetChannel
GxFpgaPioSetChannel.restype = None
GxFpgaPioSetChannel.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
GxFpgaPioGetChannel = _libraries['libGxFpga.so'].GxFpgaPioGetChannel
GxFpgaPioGetChannel.restype = None
GxFpgaPioGetChannel.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
__all__ = ['GXFPGA_DMA_WRITE', 'GT_FIRMWARE_UPGRADE_MODE_SYNC',
           'GXFPGA_3571_VIDEO_MODE_NTSC', 'PDWORD',
           'GXFPGA_LOAD_MODE_ASYNC', 'GT_NO_ERROR',
           'GXFPGA_BYPASS_BANK_C', 'GT_UNABLE_REGISTER_DEVICE',
           'GXFPGA_EEPROM_INVALID_TIME_STAMP', 'GxFpgaReadRegister',
           'GxFpga3571SetModeline', 'GT_INVALID_STRLEN',
           'GXFPGA_EXPANSION_BOARD_ID_3509', 'GxFpga3571GetVideoMode',
           'GxFpgaWriteMemory', 'GxFpgaPioSetChannel', 'LONG',
           'GxFpgaSetExpansionBoardBypass', 'GT_UNABLE_CREATE_PANEL',
           'GxFpgaDiscardEvents', 'GT_BOARD_NOT_EXIST',
           'GXFPGA_BOARD_TYPE_GX3500E', 'GxFpgaWriteRegister',
           'GxFpgaGetBoardType', 'GXFPGA_MEMORY_BAR4',
           'GXFPGA_MEMORY_BAR1', 'GXFPGA_INVALID_DMA_DATA_SIZE',
           'GXFPGA_MEMORY_BAR3', 'GXFPGA_EXPANSION_BOARD_NOT_FOUND',
           'GXFPGA_PIO_GROUP_D', 'GxFpga3571LoadFile',
           'GXFPGA_PIO_GROUP_A', 'GXFPGA_PIO_GROUP_C',
           'GXFPGA_PIO_GROUP_B', 'GXFPGA_EXPANSION_BOARD_ID_5731',
           'GXFPGA_3571_COLOR_BLUE', 'GT_FIRMWARE_UPGRADE_MODE_ASYNC',
           'DOUBLE', 'GT_EVENT_TMO_IMMEDIATE',
           'GXFPGA_LOAD_MODE_SYNC', 'GXFPGA_EEPROM_WRITE_TIMEOUT',
           'HWND', 'GXFPGA_ERROR_VOLATILE_PROGRAMMING',
           'GT_VISA_LOAD_DLL_ERROR', 'GXFPGA_3571_COLOR_MAGENTA',
           'GT_EVENT_WAIT_TIMEOUT', 'GXFPGA_FLEX_PROGRAM_FAILURE',
           'SHORT', 'GxFpga3571SetVideoMode',
           'GXFPGA_3571_VIDEO_MODE_VGA',
           'GXFPGA_3571_MODELINE_SCROLL_VERTICAL',
           'GXFPGA_3571_MODELINE_SIGNAL_SYNC',
           'GXFPGA_BOARD_TYPE_GX3700',
           'GxFpgaGetExpansionBoardBypass', 'GXFPGA_BYPASS_BANK_D',
           'GXFPGA_BYPASS_ALL', 'GXFPGA_BYPASS_BANK_B',
           'GXFPGA_BOARD_TYPE_GX3700E', 'GXFPGA_BYPASS_BANK_A',
           'GT_INVALID_PARAMETER', 'PBOOL', 'GxFpgaPioGetGroup',
           'GXFPGA_DMA_WRITE_TIMEOUT', 'GxFpgaGetDriverSummary',
           'GXFPGA_3571_MODELINE_SIGNAL_FRONT_PORCH',
           'GT_VISA_GETATTRIBUTE_ERROR', 'PDOUBLE', 'WORD',
           'GXFPGA_EXTERNAL_PROGRAMMER_DETECTED',
           'GXFPGA_3571_COLOR_CYAN', 'GXFPGA_EEPROM_READ_TIMEOUT',
           'PSHORT', 'GxFpga3571Reset',
           'GxFpgaPioSetChannelDirection', 'INT',
           'GxFpga3571LoadArray', 'GXFPGA_IMAGE_HEIGHT',
           'GT_EVENT_ALL', 'GT_VISA_OPEN_ERROR',
           'GT_VISA_OPENDEFAULTRM_ERROR', 'GxFpgaLoad', 'UINT',
           'GXFPGA_PIO_DIRECTION_OUTPUT', 'GxFpgaReset',
           'GXFPGA_DMA_READ_TIMEOUT', 'GxFpgaWaitOnEvent',
           'GT_INVALID_MODE',
           'GXFPGA_3571_MODELINE_SIGNAL_BACK_PORCH', 'PCSTR',
           'GXFPGA_3571_COLOR_YELLOW', 'GT_VISA_MEMMAP_ERROR',
           'GXFPGA_PIO_DIRECTION_INPUT', 'CHAR',
           'GxFpgaDmaGetTransferStatus', 'GT_NOT_IN_CALIBRATION_MODE',
           'GXFPGA_3571_COLOR_WHITE', 'GXFPGA_PANEL_MODELESS',
           'GXFPGA_EXPANSION_BOARD_ID_3540',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GXFPGA_FLEX_RELOAD_ERROR', 'GxFpga3571GetAdvancedMode',
           'GXFPGA_PANEL_MODAL', 'GxFpgaDmaFreeMemory',
           'GxFpgaPioGetChannelDirection',
           'GXFPGA_UNKNOWN_BOARD_TYPE',
           'GT_ERR_FUNCTION_NOT_SUPPORTED',
           'GxFpgaPioSetGroupDirection', 'GXFPGA_MEMORY_BAR2',
           'GXFPGA_EXPANSION_BOARD_ID_NONE', 'GXFPGA_BYPASS_NONE',
           'GxFpgaRead', 'PSTR', 'GxFpga3571ResetModeline',
           'GXFPGA_3571_COLOR_GREEN', 'GXFPGA_SIZE_NOT_DWORD',
           'GT_SLOT_NOT_CONFIG', 'GxFpgaGetErrorString',
           'GT_WRONG_BOARD', 'GXFPGA_BOARD_TYPE_GX3500',
           'GXFPGA_LOAD_TARGET_VOLATILE', 'BYTE', 'GXFPGA_DMA_READ',
           'GXFPGA_INVALID_FILENAME',
           'GXFPGA_ERROR_EEPROM_PROGRAMMING', 'GxFpgaPioGetChannel',
           'GXFPGA_WARNINGS_DMA_BUSY', 'GT_INVALID_ERROR',
           'GT_EVENT_INTERRUPT', 'GxFpgaDmaTransfer', 'BOOL',
           'GT_NOT_CALIBRATED', 'GXFPGA_3571_COLOR_RED',
           'GT_VISA_VIIN_ERROR', 'GxFpga3571SetAdvancedMode',
           'GT_BOARD_INVALID_EEPROM', 'GxFpgaGetExpansionBoardID',
           'GXFPGA_3571_MODELINE_SCROLL_HORIZONTAL',
           'GxFpgaPioSetGroup', 'GxFpgaWrite', 'GT_INVALID_SLOT',
           'GT_UNABLE_TO_GETTIMER', 'GT_PARAMETER_OUT_OF_RANGE',
           'GT_CANT_OPEN_HW', 'GXFPGA_3571_VIDEO_MODE_STANDBY',
           'GXFPGA_INVALID_DMA_OFFSET', 'GxFpgaReadMemory',
           'GxFpgaUpgradeFirmware', 'GXFPGA_ERROR_OFFSET',
           'GXFPGA_3571_MODELINE_SIGNAL_SYNC_PULSE',
           'GxFpgaLoadFromEeprom', 'GXFPGA_INVALID_DATA_WIDTH',
           'GXFPGA_EXPANSION_BOARD_ID_PIO',
           'GxFpgaUpgradeFirmwareStatus',
           'GXFPGA_ERROR_DATA_WIDTH_AND_NUM_BYTES',
           'GxFpgaPioGetGroupDirection', 'GxFpgaInitializeVisa',
           'PLONG', 'GT_EVENT_DISABLE_FAILED', 'Gt_EventCallback',
           'DWORD', 'GxFpga3571LoadColor', 'GT_EVENT_WAIT_ERROR',
           'GxFpgaGetEepromSummary', 'GXFPGA_IMAGE_WIDTH',
           'GxFpgaInitialize', 'GxFpgaGetBoardSummary',
           'GXFPGA_OFFSET_OUT_OF_RANGE', 'GT_EVENT_ENABLE_FAILED',
           'GXFPGA_LOAD_TARGET_EEPROM', 'PVOID',
           'GT_EVENT_TMO_INFINITE', 'GxFpgaPioReset',
           'GT_UNABLE_ALLOC_MEMORY', 'PBYTE',
           'GXFPGA_BUSY_LOAD_IN_PROGRESS', 'GxFpgaLoadStatus',
           'GXFPGA_EXPANSION_BOARD_ID_3510',
           'GXFPGA_3571_COLOR_BLACK', 'PWORD', 'GxFpgaSetEvent',
           'GT_INVALID_HANDLE', 'GXFPGA_ERROR_FILE_OPEN']
