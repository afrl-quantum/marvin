from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxCnt.so'] = CDLL('libGxCnt.so')


# VOID = void # alias
GXCNT_MEASURE_CHANNEL_A = 0 # Variable c_int '0'
GXCNT_INVALID_CAL_TIME_BASE_FREQUENCY = -75 # Variable c_int '-0x00000004b'
GXCNT_MEASURE_CHANNEL_B = 1 # Variable c_int '1'
GXCNT_FUNCTION_TEST_CLOCK = 8 # Variable c_int '8'
GT_FIRMWARE_UPGRADE_MODE_SYNC = 0 # Variable c_int '0'
GXCNT_WARNING_MICRO_CONTROLLER_COM = 13 # Variable c_int '13'
GXCNT_ACQUISITION_CONTINUOUS = 0 # Variable c_int '0'
GT_NO_ERROR = 0 # Variable c_int '0'
GXCNT_FUNCTION_FAST_FREQUENCY = 2 # Variable c_int '2'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x000000005'
GXCNT_FUNCTION_PULSE_WIDTH = 5 # Variable c_int '5'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x000000018'
GXCNT_ERR_CAL_CHANNEL_B_TRIG_LEVEL = -74 # Variable c_int '-0x00000004a'
GXCNT_PRESCALE_OFF = 0 # Variable c_int '0'
GXCNT_MIN_TIME_DELAY = 2e-05 # Variable c_double '2.00000000000000016360610782806261909172462765127e-5'
GXCNT_ERR_RECV_LAST = -56 # Variable c_int '-0x000000038'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x000000008'
GXCNT_INVALID_CHANNEL = -40 # Variable c_int '-0x000000028'
GXCNT_MEASURE_A_DIVIDED_BY_B = 0 # Variable c_int '0'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x000000002'
GXCNT_INVALID_TRIGGER_LEVEL_RANGE = -43 # Variable c_int '-0x00000002b'
GXCNT_ARM_ALTERNATE = 2 # Variable c_int '2'
GXCNT_TRIGGER_LEVEL_FIXED = 0 # Variable c_int '0'
GXCNT_FUNCTION_SINGLE_PERIOD = 7 # Variable c_int '7'
GXCNT_ERR_RANGE = -50 # Variable c_int '-0x000000032'
GXCNT_ARM_STOP_SLOPE = 1 # Variable c_int '1'
GT_FIRMWARE_UPGRADE_MODE_ASYNC = 1 # Variable c_int '1'
GXCNT_WAIT_UNTIL_READY = 2 # Variable c_int '2'
GXCNT_IMPEDANCE_50OHMS = 1 # Variable c_int '1'
GXCNT_FUNCTION_ACCUMULATE = 0 # Variable c_int '0'
GXCNT_ERR_CAL_CHANNEL_A_TRIG_LEVEL = -73 # Variable c_int '-0x000000049'
GC2210 = 12 # Variable c_int '12'
GXCNT_CLOCK_TO_PXI_REF_CLOCK_OFF = 0 # Variable c_int '0'
GXCNT_MEASURE_B_GATED_BY_A = 1 # Variable c_int '1'
GXCNT_POSITIVE_SLOPE = 0 # Variable c_int '0'
GXCNT_MIN_ACQUISITION_TIME = 0.0008 # Variable c_double '8.00000000000000038337388819087436786503531038761e-4'
GXCNT_FUNCTION_TOTALIZE_GATED_ONCE = 13 # Variable c_int '13'
GXCNT_TRIGGER_LEVEL_AUTO = 1 # Variable c_int '1'
GXCNT_CAL_TIME_BASE_TIMEOUT = -72 # Variable c_int '-0x000000048'
GXCNT_IMPEDANCE_1MOHMS = 0 # Variable c_int '0'
GXCNT_ERR_ST_TMOUT = -55 # Variable c_int '-0x000000037'
GX2200_CAL_TRIG_LEVEL_CH_B = 2 # Variable c_int '2'
GX2200_CAL_TRIG_LEVEL_CH_A = 1 # Variable c_int '1'
GTX2210 = 2 # Variable c_int '2'
GXCNT_WARNING_UNABLE_TO_SET_AUTO_FILTER_VAL = 11 # Variable c_int '11'
GXCNT_PRESCALE_AUTO = 2 # Variable c_int '2'
GXCNT_WARNING_USER_TIMEOUT = 10 # Variable c_int '10'
GXCNT_MEASURE_B_DIVIDED_BY_A = 1 # Variable c_int '1'
GXCNT_TRIGGER_LEVEL_HOLD_LAST = 2 # Variable c_int '2'
GXCNT_ARM_POSITIVE_SLOPE = 0 # Variable c_int '0'
GXCNT_MAX_TIME_DELAY = 3200 # Variable c_int '3200'
GXCNT_MIN_GATE_TIME = 0.00025 # Variable c_double '2.50000000000000005204170427930421283235773444176e-4'
GXCNT_FUNCTION_TIME_INTERVAL_DELAY = 10 # Variable c_int '10'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x000000015'
GXCNT_MEASURE_NUM_OF_DIGITS_AUTO = 0 # Variable c_int '0'
GXCNT_CAL_OFF = 0 # Variable c_int '0'
GXCNT_MEASURE_A_TO_B = 0 # Variable c_int '0'
GXCNT_FUNCTION_FREQUENCY = 3 # Variable c_int '3'
GXCNT_ACQUISITION_PACED = 2 # Variable c_int '2'
GXCNT_ARM_OFF = 3 # Variable c_int '3'
GT_VISA_GETATTRIBUTE_ERROR = -33 # Variable c_int '-0x000000021'
GXCNT_ERR_RECV_ABORT = -53 # Variable c_int '-0x000000035'
GXCNT_FREQUENCY_RANGE_HIGH_MAX_VALUE_2220 = 1300000000.0 # Variable c_double '1.3e+9'
GXCNT_CLOCK_EXTERNAL = 1 # Variable c_int '1'
GXCNT_INVALID_MODE = -41 # Variable c_int '-0x000000029'
GXCNT_COUPLING_DC = 1 # Variable c_int '1'
GT_VISA_OPEN_ERROR = -32 # Variable c_int '-0x000000020'
GT_VISA_OPENDEFAULTRM_ERROR = -31 # Variable c_int '-0x00000001f'
GXCNT_FILTER_VALUE_FIXED = 2 # Variable c_int '2'
GXCNT_NEGATIVE_SLOPE = 1 # Variable c_int '1'
GXCNT_FILTER_AUTO = 1 # Variable c_int '1'
GXCNT_ERR_CAL_NOT_STARTED = -70 # Variable c_int '-0x000000046'
GXCNT_ARM_INTERNAL = 0 # Variable c_int '0'
GXCNT_INVALID_VALUE = -42 # Variable c_int '-0x00000002a'
GT_INVALID_MODE = -25 # Variable c_int '-0x000000019'
GXCNT_INVALID_TIME_BASE_FREQUENCY = -77 # Variable c_int '-0x00000004d'
GXCNT_FREQUENCY_RANGE_HIGH_MIN_VALUE = 100000000.0 # Variable c_double '1.0e+8'
GT_VISA_MEMMAP_ERROR = -35 # Variable c_int '-0x000000023'
GXCNT_CLOCK_INTERNAL = 0 # Variable c_int '0'
GTX2230 = 3 # Variable c_int '3'
GXCNT_MAX_ACQUISITION_TIME = 3200 # Variable c_int '3200'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x00000000b'
GXCNT_ACQUISITION_SINGLE = 1 # Variable c_int '1'
GXCNT_CLOCK_ALTERNATE = 2 # Variable c_int '2'
GXCNT_COUPLING_AC = 0 # Variable c_int '0'
GXCNT_INVALID_FUNCTION = -44 # Variable c_int '-0x00000002c'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x000000006'
GXCNT_FREQUENCY_RANGE_HIGH_MAX_VALUE_2230 = 2000000000.0 # Variable c_double '2.0e+9'
GXCNT_PANEL_MODELESS = 0 # Variable c_int '0'
GXCNT_FUNCTION_TIME_INTERVAL = 9 # Variable c_int '9'
GXCNT_TOTALIZE_GATE_OPEN = 0 # Variable c_int '0'
GXCNT_FILTER_OFF = 0 # Variable c_int '0'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x00000000d'
GXCNT_CHANNEL_A = 0 # Variable c_int '0'
GT_INVALID_ERROR = -20 # Variable c_int '-0x000000014'
GXCNT_ARM_EXTERNAL = 1 # Variable c_int '1'
GXCNT_FREQUENCY_RANGE_HIGH = 1 # Variable c_int '1'
GC2220 = 11 # Variable c_int '11'
GXCNT_FREQUENCY_RANGE_NORMAL = 0 # Variable c_int '0'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x000000004'
GT_WRONG_BOARD = -3 # Variable c_int '-0x000000003'
GXCNT_ARM_NEGATIVE_SLOPE = 1 # Variable c_int '1'
GXCNT_MEASUREMENT_MAX_NUM_OF_DIGITS = 14 # Variable c_int '14'
GXCNT_FUNCTION_RATIO = 6 # Variable c_int '6'
GXCNT_CHANNEL_B = 1 # Variable c_int '1'
GTX2220 = 1 # Variable c_int '1'
GXCNT_FUNCTION_TOTALIZE = 11 # Variable c_int '11'
GXCNT_MAX_GATE_TIME = 3200 # Variable c_int '3200'
GXCNT_ERR_COMM = -52 # Variable c_int '-0x000000034'
GT_VISA_LOAD_DLL_ERROR = -30 # Variable c_int '-0x00000001e'
GXCNT_CAL_ONCE = 2 # Variable c_int '2'
GX2200_DEVICE_PASSED_CALIBRATION = 1 # Variable c_int '1'
GXCNT_PRESCALE_CONTINUOUS = 1 # Variable c_int '1'
GXCNT_FUNCTION_PERIOD = 4 # Variable c_int '4'
GXCNT_WARNING_MEASUREMENT_VALUE = 12 # Variable c_int '12'
GXCNT_MEASURE_B_TO_A = 1 # Variable c_int '1'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x00000000c'
GXCNT_TRIGGER_EXTERNAL = 1 # Variable c_int '1'
GXCNT_FUNCTION_AUTO_RATIO = 1 # Variable c_int '1'
GXCNT_FILTER_MIN_VALUE = 5 # Variable c_int '5'
GXCNT_ERR_STUCK = -57 # Variable c_int '-0x000000039'
GT_VISA_VIIN_ERROR = -34 # Variable c_int '-0x000000022'
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x00000000a'
GXCNT_MAX_TIMEOUT = 3200 # Variable c_int '3200'
GT_SYNC_TIMEOUT = -38 # Variable c_int '-0x000000026'
GC2230 = 13 # Variable c_int '13'
GXCNT_CLOCK_TO_PXI_REF_CLOCK_ON = 1 # Variable c_int '1'
GT_INVALID_SLOT = -22 # Variable c_int '-0x000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x000000009'
GXCNT_TRIGGER_LEVEL_MIN = -5.12 # Variable c_double '-5.12000000000000010658141036401502788066864013672e+0'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x000000001'
GXCNT_ARM_DISABLE_SLOPE = 2 # Variable c_int '2'
GXCNT_TOTALIZE_GATE_CLOSE = 1 # Variable c_int '1'
GXCNT_TRIGGER_LEVEL_MAX = 5.12 # Variable c_double '5.12000000000000010658141036401502788066864013672e+0'
GXCNT_MEASURE_NUM_OF_DIGITS_FIXED = 1 # Variable c_int '1'
GXCNT_TRIGGER_INTERNAL = 0 # Variable c_int '0'
GXCNT_WAIT_FOR_MEASUR_TIMEOUT = -58 # Variable c_int '-0x00000003a'
GXCNT_ERROR_CAL_OSC_FREQ_OUT_OF_RANGE = -78 # Variable c_int '-0x00000004e'
GXCNT_CAL_INVALID_DEVICE = -71 # Variable c_int '-0x000000047'
GXCNT_MEASURE_A_GATED_BY_B = 0 # Variable c_int '0'
GXCNT_ARM_START_SLOPE = 0 # Variable c_int '0'
GXCNT_ANY_SLOPE = 2 # Variable c_int '2'
GXCNT_FUNCTION_TOTALIZE_GATED = 12 # Variable c_int '12'
GXCNT_FREQUENCY_RANGE_HIGH_MAX_VALUE_2210 = 225000000.0 # Variable c_double '2.25e+8'
GXCNT_CLOCK_PXI_10MHZ_CLOCK = 3 # Variable c_int '3'
GXCNT_INVALID_CAL_TRIG_LEVEL_AMPLITUDE = -76 # Variable c_int '-0x00000004c'
GXCNT_FILTER_MAX_VALUE = 6400 # Variable c_int '6400'
GX2200_DEVICE_NOT_CALIBRATED = 0 # Variable c_int '0'
GX2200_CAL_TIME_BASE = 0 # Variable c_int '0'
GXCNT_CAL_CONTINUOUS = 1 # Variable c_int '1'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x000000007'
GXCNT_ERR_SEND_TO = -51 # Variable c_int '-0x000000033'
GX2200_DEVICE_FAILED_CALIBRATION = 2 # Variable c_int '2'
GXCNT_PANEL_MODAL = 1 # Variable c_int '1'
GXCNT_TRIGGER_LEVEL_RESOLUTION = 0.04 # Variable c_double '4.00000000000000008326672684688674053177237510681e-2'
GXCNT_MEASUREMENT_MIN_NUM_OF_DIGITS = 5 # Variable c_int '5'
GXCNT_MIN_TIMEOUT = 0.001 # Variable c_double '1.0000000000000000208166817117216851329430937767e-3'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x000000017'
CHAR = c_char
BYTE = c_ubyte
SHORT = c_short
WORD = c_ushort
INT = c_int
UINT = c_uint
LONG = c_long
DWORD = c_ulong
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
GxCntGetErrorString = _libraries['libGxCnt.so'].GxCntGetErrorString
GxCntGetErrorString.restype = None
GxCntGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxCntGetDriverSummary = _libraries['libGxCnt.so'].GxCntGetDriverSummary
GxCntGetDriverSummary.restype = None
GxCntGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
GxCntInitialize = _libraries['libGxCnt.so'].GxCntInitialize
GxCntInitialize.restype = None
GxCntInitialize.argtypes = [SHORT, PSHORT, PSHORT]
GxCntInitializeVisa = _libraries['libGxCnt.so'].GxCntInitializeVisa
GxCntInitializeVisa.restype = None
GxCntInitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
GxCntReset = _libraries['libGxCnt.so'].GxCntReset
GxCntReset.restype = None
GxCntReset.argtypes = [SHORT, PSHORT]
GxCntGetBoardSummary = _libraries['libGxCnt.so'].GxCntGetBoardSummary
GxCntGetBoardSummary.restype = None
GxCntGetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxCntGetExtendedSerialNumber = _libraries['libGxCnt.so'].GxCntGetExtendedSerialNumber
GxCntGetExtendedSerialNumber.restype = None
GxCntGetExtendedSerialNumber.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxCntClear = _libraries['libGxCnt.so'].GxCntClear
GxCntClear.restype = None
GxCntClear.argtypes = [SHORT, PSHORT]
GxCntGetAcquisitionMode = _libraries['libGxCnt.so'].GxCntGetAcquisitionMode
GxCntGetAcquisitionMode.restype = None
GxCntGetAcquisitionMode.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetAcquisitionTimeInterval = _libraries['libGxCnt.so'].GxCntGetAcquisitionTimeInterval
GxCntGetAcquisitionTimeInterval.restype = None
GxCntGetAcquisitionTimeInterval.argtypes = [SHORT, PDOUBLE, PSHORT]
GxCntGetArmSlope = _libraries['libGxCnt.so'].GxCntGetArmSlope
GxCntGetArmSlope.restype = None
GxCntGetArmSlope.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntGetArmSource = _libraries['libGxCnt.so'].GxCntGetArmSource
GxCntGetArmSource.restype = None
GxCntGetArmSource.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetBoardType = _libraries['libGxCnt.so'].GxCntGetBoardType
GxCntGetBoardType.restype = None
GxCntGetBoardType.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetCalibrationMode = _libraries['libGxCnt.so'].GxCntGetCalibrationMode
GxCntGetCalibrationMode.restype = None
GxCntGetCalibrationMode.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetChannelAFrequencyRange = _libraries['libGxCnt.so'].GxCntGetChannelAFrequencyRange
GxCntGetChannelAFrequencyRange.restype = None
GxCntGetChannelAFrequencyRange.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetChannelCouplingMode = _libraries['libGxCnt.so'].GxCntGetChannelCouplingMode
GxCntGetChannelCouplingMode.restype = None
GxCntGetChannelCouplingMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntGetChannelFilterMode = _libraries['libGxCnt.so'].GxCntGetChannelFilterMode
GxCntGetChannelFilterMode.restype = None
GxCntGetChannelFilterMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntGetChannelFilterValue = _libraries['libGxCnt.so'].GxCntGetChannelFilterValue
GxCntGetChannelFilterValue.restype = None
GxCntGetChannelFilterValue.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntGetChannelImpedance = _libraries['libGxCnt.so'].GxCntGetChannelImpedance
GxCntGetChannelImpedance.restype = None
GxCntGetChannelImpedance.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntGetChannelSlope = _libraries['libGxCnt.so'].GxCntGetChannelSlope
GxCntGetChannelSlope.restype = None
GxCntGetChannelSlope.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntGetChannelTriggerLevel = _libraries['libGxCnt.so'].GxCntGetChannelTriggerLevel
GxCntGetChannelTriggerLevel.restype = None
GxCntGetChannelTriggerLevel.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
GxCntGetChannelTriggerLevelMode = _libraries['libGxCnt.so'].GxCntGetChannelTriggerLevelMode
GxCntGetChannelTriggerLevelMode.restype = None
GxCntGetChannelTriggerLevelMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntGetClockSource = _libraries['libGxCnt.so'].GxCntGetClockSource
GxCntGetClockSource.restype = None
GxCntGetClockSource.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetCounterRefClockToPxiRefClockState = _libraries['libGxCnt.so'].GxCntGetCounterRefClockToPxiRefClockState
GxCntGetCounterRefClockToPxiRefClockState.restype = None
GxCntGetCounterRefClockToPxiRefClockState.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetFunction = _libraries['libGxCnt.so'].GxCntGetFunction
GxCntGetFunction.restype = None
GxCntGetFunction.argtypes = [SHORT, PSHORT, PSHORT, PSHORT, PSHORT, PSHORT]
GxCntGetGateTime = _libraries['libGxCnt.so'].GxCntGetGateTime
GxCntGetGateTime.restype = None
GxCntGetGateTime.argtypes = [SHORT, PDOUBLE, PSHORT]
GxCntGetMeasurementTimeout = _libraries['libGxCnt.so'].GxCntGetMeasurementTimeout
GxCntGetMeasurementTimeout.restype = None
GxCntGetMeasurementTimeout.argtypes = [SHORT, PDOUBLE, PSHORT]
GxCntGetPrescaleMode = _libraries['libGxCnt.so'].GxCntGetPrescaleMode
GxCntGetPrescaleMode.restype = None
GxCntGetPrescaleMode.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetTimeIntervalDelay = _libraries['libGxCnt.so'].GxCntGetTimeIntervalDelay
GxCntGetTimeIntervalDelay.restype = None
GxCntGetTimeIntervalDelay.argtypes = [SHORT, PDOUBLE, PSHORT]
GxCntGetTotalizeGateMode = _libraries['libGxCnt.so'].GxCntGetTotalizeGateMode
GxCntGetTotalizeGateMode.restype = None
GxCntGetTotalizeGateMode.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetTriggerSlope = _libraries['libGxCnt.so'].GxCntGetTriggerSlope
GxCntGetTriggerSlope.restype = None
GxCntGetTriggerSlope.argtypes = [SHORT, PSHORT, PSHORT]
GxCntGetTriggerSource = _libraries['libGxCnt.so'].GxCntGetTriggerSource
GxCntGetTriggerSource.restype = None
GxCntGetTriggerSource.argtypes = [SHORT, PSHORT, PSHORT]
GxCntIsMeasurementReady = _libraries['libGxCnt.so'].GxCntIsMeasurementReady
GxCntIsMeasurementReady.restype = None
GxCntIsMeasurementReady.argtypes = [SHORT, PBOOL, PSHORT]
GxCntReadMeasurement = _libraries['libGxCnt.so'].GxCntReadMeasurement
GxCntReadMeasurement.restype = None
GxCntReadMeasurement.argtypes = [SHORT, PDOUBLE, PSHORT]
GxCntReadMeasurementArray = _libraries['libGxCnt.so'].GxCntReadMeasurementArray
GxCntReadMeasurementArray.restype = None
GxCntReadMeasurementArray.argtypes = [SHORT, PDOUBLE, PDWORD, DOUBLE, PSHORT]
GxCntReadMeasurementString = _libraries['libGxCnt.so'].GxCntReadMeasurementString
GxCntReadMeasurementString.restype = None
GxCntReadMeasurementString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxCntReadStatusRegister = _libraries['libGxCnt.so'].GxCntReadStatusRegister
GxCntReadStatusRegister.restype = None
GxCntReadStatusRegister.argtypes = [SHORT, PSHORT, PSHORT]
GxCntSelfTest = _libraries['libGxCnt.so'].GxCntSelfTest
GxCntSelfTest.restype = None
GxCntSelfTest.argtypes = [SHORT, PSHORT]
GxCntSetMeasurementNumberOfDigits = _libraries['libGxCnt.so'].GxCntSetMeasurementNumberOfDigits
GxCntSetMeasurementNumberOfDigits.restype = None
GxCntSetMeasurementNumberOfDigits.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntGetMeasurementNumberOfDigits = _libraries['libGxCnt.so'].GxCntGetMeasurementNumberOfDigits
GxCntGetMeasurementNumberOfDigits.restype = None
GxCntGetMeasurementNumberOfDigits.argtypes = [SHORT, PSHORT, PSHORT, PSHORT]
GxCntSetAcquisitionMode = _libraries['libGxCnt.so'].GxCntSetAcquisitionMode
GxCntSetAcquisitionMode.restype = None
GxCntSetAcquisitionMode.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetAcquisitionTimeInterval = _libraries['libGxCnt.so'].GxCntSetAcquisitionTimeInterval
GxCntSetAcquisitionTimeInterval.restype = None
GxCntSetAcquisitionTimeInterval.argtypes = [SHORT, DOUBLE, PSHORT]
GxCntSetArmSlope = _libraries['libGxCnt.so'].GxCntSetArmSlope
GxCntSetArmSlope.restype = None
GxCntSetArmSlope.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntSetArmSource = _libraries['libGxCnt.so'].GxCntSetArmSource
GxCntSetArmSource.restype = None
GxCntSetArmSource.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetCalibrationMode = _libraries['libGxCnt.so'].GxCntSetCalibrationMode
GxCntSetCalibrationMode.restype = None
GxCntSetCalibrationMode.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetChannelAFrequencyRange = _libraries['libGxCnt.so'].GxCntSetChannelAFrequencyRange
GxCntSetChannelAFrequencyRange.restype = None
GxCntSetChannelAFrequencyRange.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetChannelCouplingMode = _libraries['libGxCnt.so'].GxCntSetChannelCouplingMode
GxCntSetChannelCouplingMode.restype = None
GxCntSetChannelCouplingMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntSetChannelFilterMode = _libraries['libGxCnt.so'].GxCntSetChannelFilterMode
GxCntSetChannelFilterMode.restype = None
GxCntSetChannelFilterMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntSetChannelFilterValue = _libraries['libGxCnt.so'].GxCntSetChannelFilterValue
GxCntSetChannelFilterValue.restype = None
GxCntSetChannelFilterValue.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntSetChannelImpedance = _libraries['libGxCnt.so'].GxCntSetChannelImpedance
GxCntSetChannelImpedance.restype = None
GxCntSetChannelImpedance.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntSetChannelSlope = _libraries['libGxCnt.so'].GxCntSetChannelSlope
GxCntSetChannelSlope.restype = None
GxCntSetChannelSlope.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntSetChannelTriggerLevel = _libraries['libGxCnt.so'].GxCntSetChannelTriggerLevel
GxCntSetChannelTriggerLevel.restype = None
GxCntSetChannelTriggerLevel.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
GxCntSetChannelTriggerLevelMode = _libraries['libGxCnt.so'].GxCntSetChannelTriggerLevelMode
GxCntSetChannelTriggerLevelMode.restype = None
GxCntSetChannelTriggerLevelMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxCntSetClockSource = _libraries['libGxCnt.so'].GxCntSetClockSource
GxCntSetClockSource.restype = None
GxCntSetClockSource.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetCounterRefClockToPxiRefClockState = _libraries['libGxCnt.so'].GxCntSetCounterRefClockToPxiRefClockState
GxCntSetCounterRefClockToPxiRefClockState.restype = None
GxCntSetCounterRefClockToPxiRefClockState.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionAccumulate = _libraries['libGxCnt.so'].GxCntSetFunctionAccumulate
GxCntSetFunctionAccumulate.restype = None
GxCntSetFunctionAccumulate.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
GxCntSetFunctionAutoRatio = _libraries['libGxCnt.so'].GxCntSetFunctionAutoRatio
GxCntSetFunctionAutoRatio.restype = None
GxCntSetFunctionAutoRatio.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionFastFrequency = _libraries['libGxCnt.so'].GxCntSetFunctionFastFrequency
GxCntSetFunctionFastFrequency.restype = None
GxCntSetFunctionFastFrequency.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionFrequency = _libraries['libGxCnt.so'].GxCntSetFunctionFrequency
GxCntSetFunctionFrequency.restype = None
GxCntSetFunctionFrequency.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionPeriod = _libraries['libGxCnt.so'].GxCntSetFunctionPeriod
GxCntSetFunctionPeriod.restype = None
GxCntSetFunctionPeriod.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionPulseWidth = _libraries['libGxCnt.so'].GxCntSetFunctionPulseWidth
GxCntSetFunctionPulseWidth.restype = None
GxCntSetFunctionPulseWidth.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionRatio = _libraries['libGxCnt.so'].GxCntSetFunctionRatio
GxCntSetFunctionRatio.restype = None
GxCntSetFunctionRatio.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionSinglePeriod = _libraries['libGxCnt.so'].GxCntSetFunctionSinglePeriod
GxCntSetFunctionSinglePeriod.restype = None
GxCntSetFunctionSinglePeriod.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionTestInternalClock = _libraries['libGxCnt.so'].GxCntSetFunctionTestInternalClock
GxCntSetFunctionTestInternalClock.restype = None
GxCntSetFunctionTestInternalClock.argtypes = [SHORT, PSHORT]
GxCntSetFunctionTimeInterval = _libraries['libGxCnt.so'].GxCntSetFunctionTimeInterval
GxCntSetFunctionTimeInterval.restype = None
GxCntSetFunctionTimeInterval.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionTimeIntervalDelay = _libraries['libGxCnt.so'].GxCntSetFunctionTimeIntervalDelay
GxCntSetFunctionTimeIntervalDelay.restype = None
GxCntSetFunctionTimeIntervalDelay.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionTotalize = _libraries['libGxCnt.so'].GxCntSetFunctionTotalize
GxCntSetFunctionTotalize.restype = None
GxCntSetFunctionTotalize.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetFunctionTotalizeGated = _libraries['libGxCnt.so'].GxCntSetFunctionTotalizeGated
GxCntSetFunctionTotalizeGated.restype = None
GxCntSetFunctionTotalizeGated.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
GxCntSetFunctionTotalizeGatedOnce = _libraries['libGxCnt.so'].GxCntSetFunctionTotalizeGatedOnce
GxCntSetFunctionTotalizeGatedOnce.restype = None
GxCntSetFunctionTotalizeGatedOnce.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
GxCntSetGateTime = _libraries['libGxCnt.so'].GxCntSetGateTime
GxCntSetGateTime.restype = None
GxCntSetGateTime.argtypes = [SHORT, DOUBLE, PSHORT]
GxCntSetMeasurementTimeout = _libraries['libGxCnt.so'].GxCntSetMeasurementTimeout
GxCntSetMeasurementTimeout.restype = None
GxCntSetMeasurementTimeout.argtypes = [SHORT, DOUBLE, PSHORT]
GxCntSetPrescaleMode = _libraries['libGxCnt.so'].GxCntSetPrescaleMode
GxCntSetPrescaleMode.restype = None
GxCntSetPrescaleMode.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetTimeIntervalDelay = _libraries['libGxCnt.so'].GxCntSetTimeIntervalDelay
GxCntSetTimeIntervalDelay.restype = None
GxCntSetTimeIntervalDelay.argtypes = [SHORT, DOUBLE, PSHORT]
GxCntSetTotalizeGateMode = _libraries['libGxCnt.so'].GxCntSetTotalizeGateMode
GxCntSetTotalizeGateMode.restype = None
GxCntSetTotalizeGateMode.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetTriggerSlope = _libraries['libGxCnt.so'].GxCntSetTriggerSlope
GxCntSetTriggerSlope.restype = None
GxCntSetTriggerSlope.argtypes = [SHORT, SHORT, PSHORT]
GxCntSetTriggerSource = _libraries['libGxCnt.so'].GxCntSetTriggerSource
GxCntSetTriggerSource.restype = None
GxCntSetTriggerSource.argtypes = [SHORT, SHORT, PSHORT]
GxCntTrig = _libraries['libGxCnt.so'].GxCntTrig
GxCntTrig.restype = None
GxCntTrig.argtypes = [SHORT, PSHORT]
GxCntSetCommonInput = _libraries['libGxCnt.so'].GxCntSetCommonInput
GxCntSetCommonInput.restype = None
GxCntSetCommonInput.argtypes = [SHORT, BOOL, SHORT, PSHORT]
GxCntGetCommonInput = _libraries['libGxCnt.so'].GxCntGetCommonInput
GxCntGetCommonInput.restype = None
GxCntGetCommonInput.argtypes = [SHORT, PBOOL, PSHORT, PSHORT]
GxCntChannelAutoSet = _libraries['libGxCnt.so'].GxCntChannelAutoSet
GxCntChannelAutoSet.restype = None
GxCntChannelAutoSet.argtypes = [SHORT, SHORT, PSHORT]
GxCntInSystemCalDevice = _libraries['libGxCnt.so'].GxCntInSystemCalDevice
GxCntInSystemCalDevice.restype = None
GxCntInSystemCalDevice.argtypes = [SHORT, SHORT, PSHORT]
GxCntInSystemCalGetStatus = _libraries['libGxCnt.so'].GxCntInSystemCalGetStatus
GxCntInSystemCalGetStatus.restype = None
GxCntInSystemCalGetStatus.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxCntInSystemCalRestore = _libraries['libGxCnt.so'].GxCntInSystemCalRestore
GxCntInSystemCalRestore.restype = None
GxCntInSystemCalRestore.argtypes = [SHORT, SHORT, PSHORT]
GxCntInSystemCalSave = _libraries['libGxCnt.so'].GxCntInSystemCalSave
GxCntInSystemCalSave.restype = None
GxCntInSystemCalSave.argtypes = [SHORT, PSHORT]
GxCntInSystemCalStart = _libraries['libGxCnt.so'].GxCntInSystemCalStart
GxCntInSystemCalStart.restype = None
GxCntInSystemCalStart.argtypes = [SHORT, PSHORT]
GxCntUpgradeFirmware = _libraries['libGxCnt.so'].GxCntUpgradeFirmware
GxCntUpgradeFirmware.restype = None
GxCntUpgradeFirmware.argtypes = [SHORT, PCSTR, SHORT, PSHORT]
GxCntUpgradeFirmwareStatus = _libraries['libGxCnt.so'].GxCntUpgradeFirmwareStatus
GxCntUpgradeFirmwareStatus.restype = None
GxCntUpgradeFirmwareStatus.argtypes = [SHORT, PSTR, SHORT, PSHORT, PBOOL, PSHORT]
__all__ = ['GXCNT_MEASURE_CHANNEL_A',
           'GXCNT_INVALID_CAL_TIME_BASE_FREQUENCY',
           'GxCntSetCounterRefClockToPxiRefClockState',
           'GXCNT_MEASURE_CHANNEL_B', 'GXCNT_FUNCTION_TEST_CLOCK',
           'GT_FIRMWARE_UPGRADE_MODE_SYNC',
           'GXCNT_WARNING_MICRO_CONTROLLER_COM', 'PDWORD',
           'GxCntInitialize', 'GXCNT_ACQUISITION_CONTINUOUS',
           'GT_NO_ERROR', 'GxCntSetFunctionFastFrequency',
           'GXCNT_FUNCTION_FAST_FREQUENCY',
           'GT_UNABLE_REGISTER_DEVICE',
           'GxCntGetAcquisitionTimeInterval',
           'GXCNT_FUNCTION_PULSE_WIDTH', 'GxCntInSystemCalStart',
           'GXCNT_FILTER_OFF', 'GT_INVALID_STRLEN',
           'GXCNT_ERR_CAL_CHANNEL_B_TRIG_LEVEL', 'GxCntSetGateTime',
           'GXCNT_PRESCALE_OFF', 'LONG', 'GXCNT_MIN_TIME_DELAY',
           'GXCNT_ERR_RECV_LAST', 'GxCntSetArmSlope',
           'GxCntSetTotalizeGateMode', 'GT_VISA_VIIN_ERROR',
           'GT_UNABLE_CREATE_PANEL', 'GXCNT_INVALID_CHANNEL',
           'GXCNT_MEASURE_A_DIVIDED_BY_B', 'GT_BOARD_NOT_EXIST',
           'GxCntGetChannelTriggerLevelMode',
           'GxCntGetMeasurementTimeout', 'GXCNT_TRIGGER_INTERNAL',
           'GxCntSetFunctionPulseWidth', 'GXCNT_ARM_ALTERNATE',
           'GXCNT_TRIGGER_LEVEL_FIXED', 'GxCntSetFunctionPeriod',
           'BOOL', 'GxCntGetExtendedSerialNumber',
           'GxCntSetFunctionAccumulate', 'GxCntGetBoardSummary',
           'GXCNT_FUNCTION_SINGLE_PERIOD', 'PSTR',
           'GxCntSetFunctionSinglePeriod', 'GXCNT_ERR_RANGE',
           'GXCNT_ARM_STOP_SLOPE', 'DOUBLE',
           'GT_FIRMWARE_UPGRADE_MODE_ASYNC', 'GxCntGetChannelSlope',
           'GXCNT_WAIT_UNTIL_READY', 'GXCNT_IMPEDANCE_50OHMS',
           'GXCNT_FUNCTION_ACCUMULATE', 'GxCntSetChannelFilterValue',
           'GxCntGetTotalizeGateMode', 'GC2210',
           'GXCNT_CLOCK_TO_PXI_REF_CLOCK_OFF',
           'GxCntSetFunctionFrequency', 'HWND',
           'GxCntGetChannelFilterMode', 'GxCntSetAcquisitionMode',
           'GXCNT_MEASURE_B_GATED_BY_A',
           'GxCntSetMeasurementNumberOfDigits', 'PLONG',
           'GXCNT_POSITIVE_SLOPE', 'GXCNT_MIN_ACQUISITION_TIME',
           'GXCNT_FUNCTION_TOTALIZE_GATED_ONCE',
           'GxCntGetTimeIntervalDelay', 'GxCntSetTimeIntervalDelay',
           'GxCntSetTriggerSlope', 'GxCntTrig', 'GxCntGetFunction',
           'GXCNT_TRIGGER_LEVEL_AUTO', 'GXCNT_CAL_TIME_BASE_TIMEOUT',
           'GxCntReadMeasurement', 'GXCNT_WAIT_FOR_MEASUR_TIMEOUT',
           'GXCNT_ERR_ST_TMOUT', 'GX2200_CAL_TRIG_LEVEL_CH_B',
           'GX2200_CAL_TRIG_LEVEL_CH_A', 'GTX2210',
           'GXCNT_WARNING_UNABLE_TO_SET_AUTO_FILTER_VAL',
           'GxCntGetDriverSummary', 'GxCntSetChannelAFrequencyRange',
           'GXCNT_PRESCALE_AUTO', 'GxCntUpgradeFirmwareStatus',
           'GXCNT_WARNING_USER_TIMEOUT', 'DDWORD', 'PBOOL',
           'GxCntGetTriggerSource', 'GxCntGetCalibrationMode',
           'GxCntSetCalibrationMode', 'GxCntSetArmSource',
           'GXCNT_MEASURE_B_DIVIDED_BY_A', 'GxCntSetClockSource',
           'GXCNT_TRIGGER_LEVEL_HOLD_LAST',
           'GXCNT_ARM_POSITIVE_SLOPE', 'GxCntInSystemCalSave',
           'GXCNT_MAX_TIME_DELAY', 'GxCntIsMeasurementReady',
           'GXCNT_MIN_GATE_TIME',
           'GXCNT_FUNCTION_TIME_INTERVAL_DELAY',
           'GT_INVALID_PARAMETER', 'GxCntGetCommonInput',
           'GxCntInSystemCalRestore', 'GXCNT_CAL_OFF',
           'GT_NOT_CALIBRATED', 'GXCNT_FUNCTION_FREQUENCY',
           'GXCNT_ACQUISITION_PACED',
           'GxCntGetMeasurementNumberOfDigits',
           'GxCntSetFunctionTotalize', 'GxCntSetFunctionAutoRatio',
           'GxCntGetTriggerSlope', 'GXCNT_ARM_OFF',
           'GT_VISA_GETATTRIBUTE_ERROR', 'PDOUBLE', 'WORD',
           'GxCntSetFunctionTotalizeGatedOnce', 'GC2230', 'PSHORT',
           'GXCNT_ERR_RECV_ABORT',
           'GXCNT_FREQUENCY_RANGE_HIGH_MAX_VALUE_2220', 'INT',
           'GXCNT_CLOCK_EXTERNAL', 'GXCNT_INVALID_MODE',
           'GXCNT_COUPLING_DC', 'GxCntGetChannelFilterValue',
           'GT_VISA_OPEN_ERROR', 'GT_VISA_OPENDEFAULTRM_ERROR',
           'GXCNT_FILTER_VALUE_FIXED', 'GxCntUpgradeFirmware',
           'GXCNT_NEGATIVE_SLOPE', 'GX2200_CAL_TIME_BASE',
           'GXCNT_FILTER_AUTO', 'GxCntInSystemCalGetStatus',
           'GxCntSetCommonInput', 'GXCNT_PANEL_MODELESS',
           'GXCNT_ARM_START_SLOPE', 'GxCntGetClockSource',
           'GxCntGetArmSlope', 'GxCntSetFunctionTimeInterval',
           'GT_INVALID_MODE', 'GXCNT_INVALID_TIME_BASE_FREQUENCY',
           'PCSTR', 'GXCNT_FREQUENCY_RANGE_HIGH_MIN_VALUE',
           'GT_VISA_MEMMAP_ERROR', 'GXCNT_CLOCK_INTERNAL', 'CHAR',
           'GTX2230', 'SHORT', 'GXCNT_MAX_ACQUISITION_TIME',
           'GT_NOT_IN_CALIBRATION_MODE', 'GXCNT_ACQUISITION_SINGLE',
           'GxCntGetErrorString', 'GxCntSetChannelFilterMode',
           'GXCNT_FREQUENCY_RANGE_NORMAL', 'GXCNT_COUPLING_AC',
           'GXCNT_INVALID_FUNCTION',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GXCNT_FREQUENCY_RANGE_HIGH_MAX_VALUE_2230',
           'GxCntGetAcquisitionMode', 'GxCntSetChannelCouplingMode',
           'GxCntReset', 'GXCNT_ERR_CAL_NOT_STARTED',
           'GxCntReadMeasurementString', 'GXCNT_FUNCTION_TOTALIZE',
           'GXCNT_TOTALIZE_GATE_OPEN', 'GXCNT_CLOCK_ALTERNATE',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GXCNT_CHANNEL_A',
           'GT_INVALID_ERROR', 'GXCNT_ARM_EXTERNAL',
           'GxCntSetChannelTriggerLevel', 'GxCntGetPrescaleMode',
           'GxCntSelfTest', 'GxCntSetChannelTriggerLevelMode',
           'GC2220', 'GXCNT_MEASURE_NUM_OF_DIGITS_AUTO',
           'GT_SLOT_NOT_CONFIG', 'GT_WRONG_BOARD',
           'GXCNT_ARM_NEGATIVE_SLOPE', 'GxCntSetPrescaleMode',
           'GxCntGetCounterRefClockToPxiRefClockState',
           'GXCNT_MEASUREMENT_MAX_NUM_OF_DIGITS',
           'GXCNT_FUNCTION_RATIO', 'BYTE', 'GXCNT_CHANNEL_B',
           'GTX2220', 'GXCNT_INVALID_VALUE', 'GXCNT_MAX_GATE_TIME',
           'GxCntGetGateTime', 'GXCNT_ERR_COMM',
           'GxCntReadStatusRegister', 'GT_VISA_LOAD_DLL_ERROR',
           'GXCNT_CAL_CONTINUOUS', 'GX2200_DEVICE_PASSED_CALIBRATION',
           'GXCNT_PRESCALE_CONTINUOUS', 'GXCNT_FUNCTION_PERIOD',
           'GT_INVALID_SLOT', 'GXCNT_MEASURE_B_TO_A',
           'GxCntSetChannelImpedance', 'GXCNT_MEASURE_A_TO_B',
           'GXCNT_TRIGGER_EXTERNAL', 'GxCntSetFunctionTotalizeGated',
           'GXCNT_FUNCTION_AUTO_RATIO', 'GXCNT_FILTER_MIN_VALUE',
           'GXCNT_ERR_STUCK', 'GXCNT_FUNCTION_TIME_INTERVAL',
           'GT_BOARD_INVALID_EEPROM', 'GXCNT_MAX_TIMEOUT',
           'GXCNT_TRIGGER_LEVEL_MIN', 'GxCntClear',
           'GXCNT_ERR_CAL_CHANNEL_A_TRIG_LEVEL',
           'GxCntSetTriggerSource', 'PDDWORD',
           'GXCNT_CLOCK_TO_PXI_REF_CLOCK_ON', 'GxCntGetArmSource',
           'GXCNT_WARNING_MEASUREMENT_VALUE', 'GT_UNABLE_TO_GETTIMER',
           'GT_SYNC_TIMEOUT', 'GxCntGetBoardType', 'GT_CANT_OPEN_HW',
           'DWORD', 'GXCNT_ARM_DISABLE_SLOPE', 'GxCntSetChannelSlope',
           'GxCntReadMeasurementArray', 'GXCNT_TOTALIZE_GATE_CLOSE',
           'GxCntGetChannelCouplingMode', 'GxCntGetChannelImpedance',
           'GXCNT_TRIGGER_LEVEL_MAX',
           'GXCNT_MEASURE_NUM_OF_DIGITS_FIXED', 'GxCntChannelAutoSet',
           'GXCNT_INVALID_TRIGGER_LEVEL_RANGE',
           'GxCntGetChannelTriggerLevel', 'GXCNT_IMPEDANCE_1MOHMS',
           'GXCNT_ERROR_CAL_OSC_FREQ_OUT_OF_RANGE',
           'GxCntGetChannelAFrequencyRange', 'GxCntInSystemCalDevice',
           'GxCntSetFunctionRatio', 'GxCntSetMeasurementTimeout',
           'GXCNT_CAL_INVALID_DEVICE', 'GXCNT_MEASURE_A_GATED_BY_B',
           'UINT', 'GXCNT_ARM_INTERNAL', 'GXCNT_ANY_SLOPE',
           'GxCntSetFunctionTestInternalClock',
           'GXCNT_FUNCTION_TOTALIZE_GATED',
           'GXCNT_FREQUENCY_RANGE_HIGH_MAX_VALUE_2210',
           'GXCNT_CLOCK_PXI_10MHZ_CLOCK',
           'GXCNT_INVALID_CAL_TRIG_LEVEL_AMPLITUDE',
           'GxCntInitializeVisa', 'GXCNT_FILTER_MAX_VALUE',
           'GX2200_DEVICE_NOT_CALIBRATED', 'PVOID',
           'GXCNT_FREQUENCY_RANGE_HIGH', 'GXCNT_CAL_ONCE',
           'GT_UNABLE_ALLOC_MEMORY', 'PBYTE',
           'GxCntSetAcquisitionTimeInterval',
           'GxCntSetFunctionTimeIntervalDelay', 'GXCNT_ERR_SEND_TO',
           'GX2200_DEVICE_FAILED_CALIBRATION', 'PWORD',
           'GXCNT_PANEL_MODAL', 'GXCNT_TRIGGER_LEVEL_RESOLUTION',
           'GXCNT_MEASUREMENT_MIN_NUM_OF_DIGITS', 'GXCNT_MIN_TIMEOUT',
           'GT_INVALID_HANDLE']
