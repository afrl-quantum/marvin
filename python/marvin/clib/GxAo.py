from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxAo.so'] = CDLL('libGxAo.so')


# VOID = void # alias
GXAO_INVALID_CLOCK_RATE = -58 # Variable c_int '-0x00000003a'
GXAO_CAL_NOT_IN_CALIBRATION_MODE = -72 # Variable c_int '-0x000000048'
GT_NO_ERROR = 0 # Variable c_int '0'
GX1649_DIO_MEMORY_OUTPUT_TYPE = 1 # Variable c_int '1'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x000000005'
GXAO_INVALID_ARB_MODE = -75 # Variable c_int '-0x00000004b'
GXAO_INVALID_CHANNEL = -51 # Variable c_int '-0x000000033'
GXAO_CHANNEL_NOT_ARB = -60 # Variable c_int '-0x00000003c'
GX1649_CAL_MODE_DISABLED = 0 # Variable c_int '0'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x000000018'
GXAO_ACCURACY_2MV = 0 # Variable c_int '0'
GT_LVRT_UNSUPPORTED = -39 # Variable c_int '-0x000000027'
GXAO_1649_TRIGGERMODE_PXI0 = 2 # Variable c_int '2'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x000000008'
GXAO_ARB_IS_RUNNING = -63 # Variable c_int '-0x00000003f'
GXAO_1649_TRIGGERMODE_STAR = 10 # Variable c_int '10'
GXAO_INVALID_VOLTAGE_RANGE = -52 # Variable c_int '-0x000000034'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x000000002'
GXAO_GROUP_GLOBAL_GROUPS = 4 # Variable c_int '4'
GXAO_VOLTAGE_OUT_OF_RANGE = -55 # Variable c_int '-0x000000037'
GXAO_INVALID_TRIGGER_MODE = -67 # Variable c_int '-0x000000043'
GXAO_1649_CLOCKSOURCE_PXI7 = 9 # Variable c_int '9'
GT_NOT_PXI_BOARD = -18 # Variable c_int '-0x000000012'
GXAO_1649_CLOCKSOURCE_EXTERNAL = 1 # Variable c_int '1'
GXAO_1649_ARB_STREAMING_STATUS_FULL = 4 # Variable c_int '4'
GXPIO_PANEL_MODELESS = 0 # Variable c_int '0'
GXAO_GROUPA = 0 # Variable c_int '0'
GXAO_GROUPB = 1 # Variable c_int '1'
GXAO_GROUPC = 2 # Variable c_int '2'
GXAO_GROUPD = 3 # Variable c_int '3'
GT_ERROR_FILE_NOT_EXIST = -16 # Variable c_int '-0x000000010'
GXAO_1649_CLOCKSOURCE_PXI1 = 3 # Variable c_int '3'
GXAO_ZERO_TO_POS5V = 2 # Variable c_int '2'
GT_EVENT_WAIT_TIMEOUT = -43 # Variable c_int '-0x00000002b'
GX1649_CAL_MODE_ENABLED = 1 # Variable c_int '1'
GXAO_DIO_INVALID_MEMORY_TYPE = -70 # Variable c_int '-0x000000046'
GXAO_INVALID_CLOCK_SOURCE = -68 # Variable c_int '-0x000000044'
GXAO_UNABLE_TO_LOCK_CHANNEL = -57 # Variable c_int '-0x000000039'
GXAO_1649_CLOCKSOURCE_STAR = 10 # Variable c_int '10'
GXAO_CAL_INVALID_CHANNEL_GAIN = -64 # Variable c_int '-0x000000040'
GXAO_ACCURACY_5MV = 1 # Variable c_int '1'
GXAO_1649_CLOCKSOURCE_INTERNAL = 0 # Variable c_int '0'
GT_DMA_MEM_ALLOC_FAILED = -45 # Variable c_int '-0x00000002d'
GXAO_1649_CLOCKSOURCE_PXI6 = 8 # Variable c_int '8'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x000000015'
GXAO_1649_CLOCKSOURCE_PXI4 = 6 # Variable c_int '6'
GXAO_1649_CLOCKSOURCE_PXI5 = 7 # Variable c_int '7'
GXAO_1649_CLOCKSOURCE_PXI2 = 4 # Variable c_int '4'
GXAO_1649_CLOCKSOURCE_PXI3 = 5 # Variable c_int '5'
GXAO_1649_CLOCKSOURCE_PXI0 = 2 # Variable c_int '2'
GXAO_INVALID_GROUP = -50 # Variable c_int '-0x000000032'
GXAO_DIO_ALLOCATED_SIZE_EXCEEDED = -71 # Variable c_int '-0x000000047'
GXAO_CHANNEL_BUSY_TIMEOUT = -56 # Variable c_int '-0x000000038'
GX1649_DIO_MEMORY_INPUT_TYPE = 0 # Variable c_int '0'
GT_VISA_GETATTRIBUTE_ERROR = -33 # Variable c_int '-0x000000021'
GXAO_1649_ARB_STREAMING_STATUS_EMPTY = 2 # Variable c_int '2'
GXAO_ZERO_TO_POS10V = 0 # Variable c_int '0'
GXAO_DIO_IS_RUNNING = -74 # Variable c_int '-0x00000004a'
GXAO_NEG5V_TO_POS5V = 3 # Variable c_int '3'
GT_VISA_OPEN_ERROR = -32 # Variable c_int '-0x000000020'
GT_VISA_OPENDEFAULTRM_ERROR = -31 # Variable c_int '-0x00000001f'
GXAO_DIO_MEMORY_SIZE_EXCEEDED = -69 # Variable c_int '-0x000000045'
GT_FILE_EXTENSION_NOT_SUPPORTED = -27 # Variable c_int '-0x00000001b'
GT_INVALID_MODE = -25 # Variable c_int '-0x000000019'
GT_UNABLE_TO_OPEN_FILE = -15 # Variable c_int '-0x00000000f'
GT_VISA_MEMMAP_ERROR = -35 # Variable c_int '-0x000000023'
GXAO_INVALID_PORT_BIT_NUMBER = -54 # Variable c_int '-0x000000036'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x00000000b'
GXAO_1649_WAVEFORM_TYPE_DOUBLE = 1 # Variable c_int '1'
GXAO_CHANNEL_NOT_STATIC = -62 # Variable c_int '-0x00000003e'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x000000006'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x00000000d'
GT_INVALID_ERROR = -20 # Variable c_int '-0x000000014'
GXAO_1642_NEG20V_TO_POS20V = 1 # Variable c_int '1'
GT_NOT_MTS_BOARD = -14 # Variable c_int '-0x00000000e'
GXAO_CAL_INVALID_ADC_OFFSET = -66 # Variable c_int '-0x000000042'
GT_INVALID_CHASSIS_NUMBER = -28 # Variable c_int '-0x00000001c'
GT_WRONG_BOARD = -3 # Variable c_int '-0x000000003'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x000000004'
GT_SYNC_CREATE = -37 # Variable c_int '-0x000000025'
GT_VISA_LOAD_DLL_ERROR = -30 # Variable c_int '-0x00000001e'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x00000000c'
GXAO_1649_WAVEFORM_TYPE_WORD = 0 # Variable c_int '0'
GT_VISA_VIIN_ERROR = -34 # Variable c_int '-0x000000022'
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x00000000a'
GXAO_1649_ARB_STREAMING_STATUS_HALF_EMPTY = 1 # Variable c_int '1'
GXAO_INVALID_PORT_DIRECTION = -53 # Variable c_int '-0x000000035'
GXAO_INVALID_MEMORY_CONFIG = -59 # Variable c_int '-0x00000003b'
GT_INVALID_SLOT = -22 # Variable c_int '-0x000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x000000009'
GT_SYNC_TIMEOUT = -38 # Variable c_int '-0x000000026'
GT_PARAMETER_OUT_OF_RANGE = -26 # Variable c_int '-0x00000001a'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x000000001'
GXAO_CAL_INVALID_ADC_GAIN = -65 # Variable c_int '-0x000000041'
GXPIO_PANEL_MODAL = 1 # Variable c_int '1'
GX1649_CAL_VOLTAGE_POINT_NEGATIVE = 0 # Variable c_int '0'
GXAO_1642_ZERO_TO_POS20V = 0 # Variable c_int '0'
GT_ERR_DMA_MEM_FREE = -47 # Variable c_int '-0x00000002f'
GXAO_NEG10V_TO_POS10V = 1 # Variable c_int '1'
GXAO_1649_TRIGGERMODE_PXI2 = 4 # Variable c_int '4'
GXAO_1649_TRIGGERMODE_PXI3 = 5 # Variable c_int '5'
GXAO_1649_TRIGGERMODE_GLOBAL = 11 # Variable c_int '11'
GXAO_1649_TRIGGERMODE_PXI1 = 3 # Variable c_int '3'
GXAO_1649_TRIGGERMODE_EXTERNAL = 1 # Variable c_int '1'
GXAO_1649_TRIGGERMODE_PXI7 = 9 # Variable c_int '9'
GXAO_1649_TRIGGERMODE_PXI4 = 6 # Variable c_int '6'
GXAO_1649_TRIGGERMODE_PXI5 = 7 # Variable c_int '7'
GXAO_ARB_MEMORY_SIZE_EXCEEDED = -61 # Variable c_int '-0x00000003d'
GXAO_1649_CLOCKSOURCE_GROUPA = 11 # Variable c_int '11'
GT_EVENT_DISABLE_FAILED = -42 # Variable c_int '-0x00000002a'
GT_ERR_DMA_MEM_UN_MAP = -46 # Variable c_int '-0x00000002e'
GXAO_1642_NEG10V_TO_POS10V = 3 # Variable c_int '3'
GT_EVENT_WAIT_ERROR = -44 # Variable c_int '-0x00000002c'
GT_INVALID_CALIBRATION_TIME_STAMP = -29 # Variable c_int '-0x00000001d'
GT_ERR_MODE_NOT_SUPPORTED_BY_SLOT = -17 # Variable c_int '-0x000000011'
GXAO_1649_TRIGGERMODE_PXI6 = 8 # Variable c_int '8'
GXAO_1649_TRIGGERMODE_SOFTWARE_ONLY = 0 # Variable c_int '0'
GX1649_CAL_VOLTAGE_POINT_POSITIVE = 1 # Variable c_int '1'
GT_EVENT_ENABLE_FAILED = -41 # Variable c_int '-0x000000029'
GXAO_STREAMING_NOT_SUPPORTED_BY_FIRMWARE = -76 # Variable c_int '-0x00000004c'
GT_NOT_PCI_BOARD = -19 # Variable c_int '-0x000000013'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x000000007'
GT_ERR_CHECKSUM = -48 # Variable c_int '-0x000000030'
GXAO_CAL_INVALID_VOLTAGE_POINT = -73 # Variable c_int '-0x000000049'
GX1649_DIO_MEMORY_DIRECTION_TYPE = 2 # Variable c_int '2'
GXAO_1642_ZERO_TO_POS10V = 2 # Variable c_int '2'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x000000017'
GT_LICENSE = -40 # Variable c_int '-0x000000028'
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
PBYTE = POINTER(BYTE)
PSHORT = POINTER(SHORT)
PWORD = POINTER(WORD)
PLONG = POINTER(LONG)
PDWORD = POINTER(DWORD)
PDOUBLE = POINTER(DOUBLE)
PVOID = c_void_p
PSTR = STRING
HWND = c_void_p
PCSTR = STRING
Gt_EventCallback = CFUNCTYPE(LONG, SHORT, SHORT, PVOID)
GxAoGetErrorString = _libraries['libGxAo.so'].GxAoGetErrorString
GxAoGetErrorString.restype = None
GxAoGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxAoGetDriverSummary = _libraries['libGxAo.so'].GxAoGetDriverSummary
GxAoGetDriverSummary.restype = None
GxAoGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
GxAoInitialize = _libraries['libGxAo.so'].GxAoInitialize
GxAoInitialize.restype = None
GxAoInitialize.argtypes = [SHORT, PSHORT, PSHORT]
GxAoInitializeVisa = _libraries['libGxAo.so'].GxAoInitializeVisa
GxAoInitializeVisa.restype = None
GxAoInitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
GxAoReset = _libraries['libGxAo.so'].GxAoReset
GxAoReset.restype = None
GxAoReset.argtypes = [SHORT, PSHORT]
GxAoPanel = _libraries['libGxAo.so'].GxAoPanel
GxAoPanel.restype = None
GxAoPanel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
GxAoGetBoardSummary = _libraries['libGxAo.so'].GxAoGetBoardSummary
GxAoGetBoardSummary.restype = None
GxAoGetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxAoGetCalibrationInfo = _libraries['libGxAo.so'].GxAoGetCalibrationInfo
GxAoGetCalibrationInfo.restype = None
GxAoGetCalibrationInfo.argtypes = [SHORT, PSTR, SHORT, PSHORT, PSHORT]
GxAoSetChannelVoltage = _libraries['libGxAo.so'].GxAoSetChannelVoltage
GxAoSetChannelVoltage.restype = None
GxAoSetChannelVoltage.argtypes = [SHORT, SHORT, SHORT, DOUBLE, PSHORT]
GxAoGetChannelVoltage = _libraries['libGxAo.so'].GxAoGetChannelVoltage
GxAoGetChannelVoltage.restype = None
GxAoGetChannelVoltage.argtypes = [SHORT, SHORT, SHORT, PDOUBLE, PSHORT]
GxAoLoadChannelVoltage = _libraries['libGxAo.so'].GxAoLoadChannelVoltage
GxAoLoadChannelVoltage.restype = None
GxAoLoadChannelVoltage.argtypes = [SHORT, SHORT, SHORT, DOUBLE, PSHORT]
GxAoUpdateGroupVoltage = _libraries['libGxAo.so'].GxAoUpdateGroupVoltage
GxAoUpdateGroupVoltage.restype = None
GxAoUpdateGroupVoltage.argtypes = [SHORT, SHORT, PSHORT]
GxAoUpdateAllGroupsVoltage = _libraries['libGxAo.so'].GxAoUpdateAllGroupsVoltage
GxAoUpdateAllGroupsVoltage.restype = None
GxAoUpdateAllGroupsVoltage.argtypes = [SHORT, PSHORT]
GxAoSetGroupExternalUpdate = _libraries['libGxAo.so'].GxAoSetGroupExternalUpdate
GxAoSetGroupExternalUpdate.restype = None
GxAoSetGroupExternalUpdate.argtypes = [SHORT, SHORT, BOOL, PSHORT]
GxAoGetGroupExternalUpdate = _libraries['libGxAo.so'].GxAoGetGroupExternalUpdate
GxAoGetGroupExternalUpdate.restype = None
GxAoGetGroupExternalUpdate.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
GxAoGetGroupUpdateState = _libraries['libGxAo.so'].GxAoGetGroupUpdateState
GxAoGetGroupUpdateState.restype = None
GxAoGetGroupUpdateState.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
GxAoGetBoardAccuracy = _libraries['libGxAo.so'].GxAoGetBoardAccuracy
GxAoGetBoardAccuracy.restype = None
GxAoGetBoardAccuracy.argtypes = [SHORT, PSHORT, PSHORT]
GxAoResetGroup = _libraries['libGxAo.so'].GxAoResetGroup
GxAoResetGroup.restype = None
GxAoResetGroup.argtypes = [SHORT, SHORT, PSHORT]
GxAoSetPortBit = _libraries['libGxAo.so'].GxAoSetPortBit
GxAoSetPortBit.restype = None
GxAoSetPortBit.argtypes = [SHORT, BOOL, PSHORT]
GxAoGetPortBit = _libraries['libGxAo.so'].GxAoGetPortBit
GxAoGetPortBit.restype = None
GxAoGetPortBit.argtypes = [SHORT, PBOOL, PSHORT]
GxAoSetGroupVoltageRange = _libraries['libGxAo.so'].GxAoSetGroupVoltageRange
GxAoSetGroupVoltageRange.restype = None
GxAoSetGroupVoltageRange.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxAoGetGroupVoltageRange = _libraries['libGxAo.so'].GxAoGetGroupVoltageRange
GxAoGetGroupVoltageRange.restype = None
GxAoGetGroupVoltageRange.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxAoSelfTest = _libraries['libGxAo.so'].GxAoSelfTest
GxAoSelfTest.restype = None
GxAoSelfTest.argtypes = [SHORT, PDWORD, PSTR, PSHORT]
GxAoArbEnableGroupStreaming = _libraries['libGxAo.so'].GxAoArbEnableGroupStreaming
GxAoArbEnableGroupStreaming.restype = None
GxAoArbEnableGroupStreaming.argtypes = [SHORT, SHORT, BOOL, PSHORT]
GxAoArbIsGroupStreaming = _libraries['libGxAo.so'].GxAoArbIsGroupStreaming
GxAoArbIsGroupStreaming.restype = None
GxAoArbIsGroupStreaming.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
GxAoArbGetGroupStreamingStatus = _libraries['libGxAo.so'].GxAoArbGetGroupStreamingStatus
GxAoArbGetGroupStreamingStatus.restype = None
GxAoArbGetGroupStreamingStatus.argtypes = [SHORT, SHORT, PWORD, PWORD, PSHORT]
GxAoArbSetupStreamingInterrupt = _libraries['libGxAo.so'].GxAoArbSetupStreamingInterrupt
GxAoArbSetupStreamingInterrupt.restype = None
GxAoArbSetupStreamingInterrupt.argtypes = [SHORT, WORD, Gt_EventCallback, PVOID, PSHORT]
GxAoArbDisableStreamingInterrupt = _libraries['libGxAo.so'].GxAoArbDisableStreamingInterrupt
GxAoArbDisableStreamingInterrupt.restype = None
GxAoArbDisableStreamingInterrupt.argtypes = [SHORT, PSHORT]
GxAoArbResumeStreamingInterrupt = _libraries['libGxAo.so'].GxAoArbResumeStreamingInterrupt
GxAoArbResumeStreamingInterrupt.restype = None
GxAoArbResumeStreamingInterrupt.argtypes = [SHORT, PSHORT]
GxAoArbSetGroupChannels = _libraries['libGxAo.so'].GxAoArbSetGroupChannels
GxAoArbSetGroupChannels.restype = None
GxAoArbSetGroupChannels.argtypes = [SHORT, SHORT, WORD, DWORD, PSHORT]
GxAoArbGetGroupChannels = _libraries['libGxAo.so'].GxAoArbGetGroupChannels
GxAoArbGetGroupChannels.restype = None
GxAoArbGetGroupChannels.argtypes = [SHORT, SHORT, PWORD, PDWORD, PSHORT]
GxAoArbSetGroupClock = _libraries['libGxAo.so'].GxAoArbSetGroupClock
GxAoArbSetGroupClock.restype = None
GxAoArbSetGroupClock.argtypes = [SHORT, SHORT, SHORT, DOUBLE, PSHORT]
GxAoArbGetGroupClock = _libraries['libGxAo.so'].GxAoArbGetGroupClock
GxAoArbGetGroupClock.restype = None
GxAoArbGetGroupClock.argtypes = [SHORT, SHORT, PSHORT, PDOUBLE, PSHORT]
GxAoArbSetGroupTrigger = _libraries['libGxAo.so'].GxAoArbSetGroupTrigger
GxAoArbSetGroupTrigger.restype = None
GxAoArbSetGroupTrigger.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxAoArbGetGroupTrigger = _libraries['libGxAo.so'].GxAoArbGetGroupTrigger
GxAoArbGetGroupTrigger.restype = None
GxAoArbGetGroupTrigger.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxAoArbWriteChannelWaveform = _libraries['libGxAo.so'].GxAoArbWriteChannelWaveform
GxAoArbWriteChannelWaveform.restype = None
GxAoArbWriteChannelWaveform.argtypes = [SHORT, SHORT, SHORT, PVOID, DWORD, SHORT, PSHORT]
GxAoArbReadChannelWaveform = _libraries['libGxAo.so'].GxAoArbReadChannelWaveform
GxAoArbReadChannelWaveform.restype = None
GxAoArbReadChannelWaveform.argtypes = [SHORT, SHORT, SHORT, PVOID, PDWORD, SHORT, PSHORT]
GxAoArbWriteStreamingData = _libraries['libGxAo.so'].GxAoArbWriteStreamingData
GxAoArbWriteStreamingData.restype = None
GxAoArbWriteStreamingData.argtypes = [SHORT, SHORT, PVOID, DWORD, SHORT, PSHORT]
GxAoArbArmGroup = _libraries['libGxAo.so'].GxAoArbArmGroup
GxAoArbArmGroup.restype = None
GxAoArbArmGroup.argtypes = [SHORT, SHORT, BOOL, BOOL, PSHORT]
GxAoArbTrigGroup = _libraries['libGxAo.so'].GxAoArbTrigGroup
GxAoArbTrigGroup.restype = None
GxAoArbTrigGroup.argtypes = [SHORT, SHORT, PSHORT]
GxAoArbGetGroupStatus = _libraries['libGxAo.so'].GxAoArbGetGroupStatus
GxAoArbGetGroupStatus.restype = None
GxAoArbGetGroupStatus.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
GxAoDioWriteMemory = _libraries['libGxAo.so'].GxAoDioWriteMemory
GxAoDioWriteMemory.restype = None
GxAoDioWriteMemory.argtypes = [SHORT, SHORT, PBYTE, DWORD, PSHORT]
GxAoDioWriteChannelMemory = _libraries['libGxAo.so'].GxAoDioWriteChannelMemory
GxAoDioWriteChannelMemory.restype = None
GxAoDioWriteChannelMemory.argtypes = [SHORT, SHORT, SHORT, PBYTE, DWORD, PSHORT]
GxAoDioReadMemory = _libraries['libGxAo.so'].GxAoDioReadMemory
GxAoDioReadMemory.restype = None
GxAoDioReadMemory.argtypes = [SHORT, SHORT, PBYTE, DWORD, PSHORT]
GxAoDioReadChannelMemory = _libraries['libGxAo.so'].GxAoDioReadChannelMemory
GxAoDioReadChannelMemory.restype = None
GxAoDioReadChannelMemory.argtypes = [SHORT, SHORT, SHORT, PBYTE, DWORD, PSHORT]
GxAoDioArm = _libraries['libGxAo.so'].GxAoDioArm
GxAoDioArm.restype = None
GxAoDioArm.argtypes = [SHORT, BOOL, BOOL, PSHORT]
GxAoDioTrig = _libraries['libGxAo.so'].GxAoDioTrig
GxAoDioTrig.restype = None
GxAoDioTrig.argtypes = [SHORT, PSHORT]
GxAoDioGetStatus = _libraries['libGxAo.so'].GxAoDioGetStatus
GxAoDioGetStatus.restype = None
GxAoDioGetStatus.argtypes = [SHORT, PDWORD, PSHORT]
GxAoDioSetClock = _libraries['libGxAo.so'].GxAoDioSetClock
GxAoDioSetClock.restype = None
GxAoDioSetClock.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
GxAoDioGetClock = _libraries['libGxAo.so'].GxAoDioGetClock
GxAoDioGetClock.restype = None
GxAoDioGetClock.argtypes = [SHORT, PSHORT, PDOUBLE, PSHORT]
GxAoDioSetVectorCount = _libraries['libGxAo.so'].GxAoDioSetVectorCount
GxAoDioSetVectorCount.restype = None
GxAoDioSetVectorCount.argtypes = [SHORT, DWORD, PSHORT]
GxAoDioGetVectorCount = _libraries['libGxAo.so'].GxAoDioGetVectorCount
GxAoDioGetVectorCount.restype = None
GxAoDioGetVectorCount.argtypes = [SHORT, PDWORD, PSHORT]
GxAoDioSetOutputEnable = _libraries['libGxAo.so'].GxAoDioSetOutputEnable
GxAoDioSetOutputEnable.restype = None
GxAoDioSetOutputEnable.argtypes = [SHORT, BYTE, PSHORT]
GxAoDioGetOutputEnable = _libraries['libGxAo.so'].GxAoDioGetOutputEnable
GxAoDioGetOutputEnable.restype = None
GxAoDioGetOutputEnable.argtypes = [SHORT, PBYTE, PSHORT]
GxAoCalSetMode = _libraries['libGxAo.so'].GxAoCalSetMode
GxAoCalSetMode.restype = None
GxAoCalSetMode.argtypes = [SHORT, SHORT, PSHORT]
GxAoCalSetVoltagePoint = _libraries['libGxAo.so'].GxAoCalSetVoltagePoint
GxAoCalSetVoltagePoint.restype = None
GxAoCalSetVoltagePoint.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
GxAoCalADCMeasure = _libraries['libGxAo.so'].GxAoCalADCMeasure
GxAoCalADCMeasure.restype = None
GxAoCalADCMeasure.argtypes = [SHORT, SHORT, SHORT, PDOUBLE, PSHORT]
GxAoCalADC = _libraries['libGxAo.so'].GxAoCalADC
GxAoCalADC.restype = None
GxAoCalADC.argtypes = [SHORT, DOUBLE, DOUBLE, DOUBLE, DOUBLE, PSHORT]
GxAoCalGroupChannel = _libraries['libGxAo.so'].GxAoCalGroupChannel
GxAoCalGroupChannel.restype = None
GxAoCalGroupChannel.argtypes = [SHORT, SHORT, SHORT, DOUBLE, DOUBLE, PSHORT]
GxAoCalWriteEEPROM = _libraries['libGxAo.so'].GxAoCalWriteEEPROM
GxAoCalWriteEEPROM.restype = None
GxAoCalWriteEEPROM.argtypes = [SHORT, PSHORT]
__all__ = ['GxAoCalGroupChannel', 'GXAO_INVALID_CLOCK_RATE',
           'GXAO_CAL_NOT_IN_CALIBRATION_MODE', 'PDWORD',
           'GxAoSelfTest', 'GT_NO_ERROR',
           'GX1649_DIO_MEMORY_OUTPUT_TYPE',
           'GT_UNABLE_REGISTER_DEVICE', 'GXAO_INVALID_ARB_MODE',
           'GxAoArbGetGroupClock', 'WORD', 'GXAO_INVALID_CHANNEL',
           'GXAO_CHANNEL_NOT_ARB', 'GX1649_CAL_MODE_DISABLED',
           'GxAoArbGetGroupStreamingStatus', 'GT_INVALID_STRLEN',
           'GXAO_ACCURACY_2MV', 'GT_LVRT_UNSUPPORTED',
           'GXAO_1649_TRIGGERMODE_GLOBAL', 'LONG',
           'GxAoDioWriteChannelMemory', 'GT_UNABLE_CREATE_PANEL',
           'GXAO_ARB_IS_RUNNING', 'GXAO_1649_TRIGGERMODE_STAR',
           'GXAO_INVALID_VOLTAGE_RANGE', 'GxAoGetChannelVoltage',
           'GxAoArbGetGroupChannels', 'GxAoInitializeVisa',
           'GT_BOARD_NOT_EXIST', 'GXAO_GROUP_GLOBAL_GROUPS',
           'GXAO_VOLTAGE_OUT_OF_RANGE', 'GXAO_INVALID_TRIGGER_MODE',
           'GxAoCalSetVoltagePoint', 'GxAoArbIsGroupStreaming',
           'GT_INVALID_PARAMETER', 'GxAoArbArmGroup',
           'GT_NOT_PXI_BOARD', 'GXAO_1649_CLOCKSOURCE_EXTERNAL',
           'PSTR', 'GXAO_1649_ARB_STREAMING_STATUS_FULL',
           'GXPIO_PANEL_MODELESS', 'GxAoSetPortBit', 'GXAO_GROUPA',
           'GXAO_GROUPB', 'GXAO_GROUPC', 'GXAO_GROUPD',
           'GXAO_CHANNEL_BUSY_TIMEOUT', 'DOUBLE',
           'GxAoArbResumeStreamingInterrupt', 'GXAO_INVALID_GROUP',
           'GT_VISA_LOAD_DLL_ERROR', 'PLONG', 'GT_EVENT_WAIT_TIMEOUT',
           'SHORT', 'GxAoArbDisableStreamingInterrupt',
           'GX1649_CAL_MODE_ENABLED', 'GXAO_DIO_INVALID_MEMORY_TYPE',
           'GXAO_INVALID_CLOCK_SOURCE', 'GxAoArbGetGroupStatus',
           'GxAoGetPortBit', 'GxAoCalADC', 'GxAoCalSetMode',
           'GXAO_UNABLE_TO_LOCK_CHANNEL', 'GxAoDioGetVectorCount',
           'GxAoReset', 'GxAoDioGetOutputEnable', 'PBOOL',
           'GXAO_1649_CLOCKSOURCE_STAR',
           'GXAO_CAL_INVALID_CHANNEL_GAIN', 'GxAoArbSetGroupTrigger',
           'GXAO_ACCURACY_5MV', 'GXAO_1649_CLOCKSOURCE_INTERNAL',
           'GT_DMA_MEM_ALLOC_FAILED', 'GxAoCalWriteEEPROM',
           'GxAoArbSetupStreamingInterrupt',
           'GXAO_1649_CLOCKSOURCE_PXI6', 'GXAO_1649_CLOCKSOURCE_PXI7',
           'GXAO_1649_CLOCKSOURCE_PXI4', 'GXAO_1649_CLOCKSOURCE_PXI5',
           'GXAO_1649_CLOCKSOURCE_PXI2', 'GXAO_1649_CLOCKSOURCE_PXI3',
           'GXAO_1649_CLOCKSOURCE_PXI0', 'GXAO_1649_CLOCKSOURCE_PXI1',
           'GXAO_DIO_ALLOCATED_SIZE_EXCEEDED',
           'GT_ERROR_FILE_NOT_EXIST', 'GxAoGetGroupVoltageRange',
           'PVOID', 'GxAoGetGroupExternalUpdate', 'GxAoDioGetStatus',
           'GX1649_DIO_MEMORY_INPUT_TYPE',
           'GT_VISA_GETATTRIBUTE_ERROR', 'PDOUBLE',
           'GXAO_1649_ARB_STREAMING_STATUS_EMPTY',
           'GxAoGetErrorString', 'GXAO_ZERO_TO_POS10V',
           'GXAO_DIO_IS_RUNNING', 'INT', 'GxAoDioSetClock',
           'GXAO_NEG5V_TO_POS5V', 'GT_VISA_OPEN_ERROR',
           'GT_VISA_OPENDEFAULTRM_ERROR',
           'GXAO_DIO_MEMORY_SIZE_EXCEEDED', 'UINT',
           'GxAoArbWriteChannelWaveform',
           'GT_FILE_EXTENSION_NOT_SUPPORTED', 'GT_INVALID_MODE',
           'GXAO_1649_ARB_STREAMING_STATUS_HALF_EMPTY', 'PCSTR',
           'GxAoResetGroup', 'GxAoGetDriverSummary',
           'GT_VISA_MEMMAP_ERROR', 'GxAoDioReadChannelMemory', 'CHAR',
           'GXAO_INVALID_PORT_BIT_NUMBER',
           'GT_NOT_IN_CALIBRATION_MODE',
           'GXAO_1649_WAVEFORM_TYPE_DOUBLE', 'GxAoSetChannelVoltage',
           'HWND', 'GXAO_CHANNEL_NOT_STATIC',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE', 'GxAoDioGetClock',
           'GxAoPanel', 'GxAoLoadChannelVoltage',
           'GxAoArbWriteStreamingData', 'GxAoDioReadMemory',
           'GxAoGetBoardAccuracy', 'GT_ERR_FUNCTION_NOT_SUPPORTED',
           'GxAoGetGroupUpdateState', 'GT_INVALID_ERROR',
           'GXAO_1642_NEG20V_TO_POS20V', 'GxAoCalADCMeasure',
           'GT_NOT_MTS_BOARD', 'GXAO_CAL_INVALID_ADC_OFFSET',
           'GxAoArbTrigGroup', 'GxAoArbSetGroupChannels',
           'GT_INVALID_CHASSIS_NUMBER', 'GT_WRONG_BOARD',
           'GT_SYNC_CREATE', 'GxAoSetGroupVoltageRange',
           'GxAoGetBoardSummary', 'GxAoGetCalibrationInfo',
           'GxAoUpdateAllGroupsVoltage', 'GxAoDioSetOutputEnable',
           'GxAoDioTrig', 'GXAO_ZERO_TO_POS5V', 'BYTE',
           'GxAoUpdateGroupVoltage', 'BOOL', 'GxAoDioArm',
           'GT_NOT_CALIBRATED', 'GT_UNABLE_TO_GETTIMER',
           'GT_VISA_VIIN_ERROR', 'GT_BOARD_INVALID_EEPROM',
           'GT_UNABLE_TO_OPEN_FILE', 'GxAoArbReadChannelWaveform',
           'GxAoArbGetGroupTrigger', 'GXAO_INVALID_PORT_DIRECTION',
           'GXAO_INVALID_MEMORY_CONFIG', 'GT_INVALID_SLOT',
           'GXAO_1649_WAVEFORM_TYPE_WORD', 'GT_SYNC_TIMEOUT',
           'GT_PARAMETER_OUT_OF_RANGE', 'GT_CANT_OPEN_HW', 'DWORD',
           'GXAO_CAL_INVALID_ADC_GAIN', 'GxAoSetGroupExternalUpdate',
           'GX1649_CAL_VOLTAGE_POINT_NEGATIVE',
           'GXAO_1642_ZERO_TO_POS20V', 'GXPIO_PANEL_MODAL',
           'GXAO_NEG10V_TO_POS10V', 'GXAO_1649_TRIGGERMODE_PXI2',
           'GXAO_1649_TRIGGERMODE_PXI3', 'GXAO_1649_TRIGGERMODE_PXI0',
           'GXAO_1649_TRIGGERMODE_PXI1',
           'GXAO_1649_TRIGGERMODE_EXTERNAL',
           'GXAO_1649_TRIGGERMODE_PXI7', 'GXAO_1649_TRIGGERMODE_PXI4',
           'GXAO_1649_TRIGGERMODE_PXI5', 'GxAoDioSetVectorCount',
           'GxAoDioWriteMemory', 'GXAO_ARB_MEMORY_SIZE_EXCEEDED',
           'GxAoArbSetGroupClock', 'GxAoInitialize',
           'GXAO_1649_CLOCKSOURCE_GROUPA', 'GT_EVENT_DISABLE_FAILED',
           'GT_ERR_DMA_MEM_UN_MAP', 'Gt_EventCallback',
           'GT_SLOT_NOT_CONFIG', 'PSHORT', 'GT_EVENT_WAIT_ERROR',
           'GT_INVALID_CALIBRATION_TIME_STAMP',
           'GT_ERR_MODE_NOT_SUPPORTED_BY_SLOT',
           'GXAO_1649_TRIGGERMODE_PXI6', 'GXAO_1642_ZERO_TO_POS10V',
           'GX1649_CAL_VOLTAGE_POINT_POSITIVE',
           'GT_EVENT_ENABLE_FAILED',
           'GXAO_STREAMING_NOT_SUPPORTED_BY_FIRMWARE',
           'GT_INVALID_HANDLE', 'GT_ERR_DMA_MEM_FREE',
           'GXAO_1642_NEG10V_TO_POS10V',
           'GxAoArbEnableGroupStreaming', 'GT_UNABLE_ALLOC_MEMORY',
           'GT_ERR_CHECKSUM', 'PBYTE',
           'GXAO_CAL_INVALID_VOLTAGE_POINT', 'PWORD',
           'GX1649_DIO_MEMORY_DIRECTION_TYPE',
           'GXAO_1649_TRIGGERMODE_SOFTWARE_ONLY', 'GT_NOT_PCI_BOARD',
           'GT_LICENSE']
