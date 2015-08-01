from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxDmm.so'] = CDLL('libGxDmm.so')


# VOID = void # alias
GXDMM_RANGE_1Arms = 1.0 # Variable c_double '1.0e+0'
GXDMM_PANEL_MODELESS = 0 # Variable c_int '0'
GXDMM_CAL_Daq100mAAC = 43 # Variable c_int '43'
GT_NO_ERROR = 0 # Variable c_int '0'
GXDMM_ERROR_INVALID_CAL_GROUP = -134 # Variable c_int '-0x000000086'
GXDMM_CAL_Daq10VDC = 30 # Variable c_int '30'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x000000005'
GXDMM_ERROR_READ_ONLY_COMMAND = -113 # Variable c_int '-0x000000071'
GXDMM_RANGE_100Ohm = 100 # Variable c_int '100'
GXDMM_ERROR_INVALID_TRIGGER_TIMER_RATE = -126 # Variable c_int '-0x00000007e'
GXDMM_CAL_HiResVCalOpen = 26 # Variable c_int '26'
GXDMM_CAL_DaqTempTypeN = 50 # Variable c_int '50'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x000000018'
GXDMM_CAL_Daq100VAC = 40 # Variable c_int '40'
GXDMM_TRIGGER_SOFTWARE = 3 # Variable c_int '3'
GT_LVRT_UNSUPPORTED = -39 # Variable c_int '-0x000000027'
GXDMM_WARNING_TIMEOUT = 101 # Variable c_int '101'
GXDMM_ERROR_INVALID_FUNCTION = -122 # Variable c_int '-0x00000007a'
GXDMM_AUTO_ZERO_ON = 0 # Variable c_int '0'
GXDMM_RANGE_10MOhm = 10000000 # Variable c_int '10000000'
GXDMM_CAL_HiRes1M_Ohms4W = 20 # Variable c_int '20'
GXDMM_ERROR_READ_ERROR = -109 # Variable c_int '-0x00000006d'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x000000008'
GXDMM_ERROR_INVALID_DAQ_ARRAY = -92 # Variable c_int '-0x00000005c'
GXDMM_ERROR_CAL_LICENSE = -137 # Variable c_int '-0x000000089'
GXDMM_FUNCTION_4WIRE_OHM = 7 # Variable c_int '7'
GXDMM_CAL_DaqTempTypeT = 53 # Variable c_int '53'
GXDMM_FUNCTION_DIODE = 10 # Variable c_int '10'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x000000007'
GXDMM_CAL_Daq20mAAC = 42 # Variable c_int '42'
GXDMM_ERROR_MBOARD_NOT_PRESENT = -112 # Variable c_int '-0x000000070'
GXDMM_CAL_HiRes_R_Ref = 27 # Variable c_int '27'
GXDMM_CAL_Daq2AAC = 45 # Variable c_int '45'
GXDMM_ERROR_COMM = -121 # Variable c_int '-0x000000079'
GXDMM_RESOLUTION_3_5_DIGITS = 4 # Variable c_int '4'
GXDMM_ERROR_INVALID_APERTURE = -131 # Variable c_int '-0x000000083'
GXDMM_CAL_HiRes1k_Ohms2W = 10 # Variable c_int '10'
GXDMM_ERROR_FLASH_FAIL = -110 # Variable c_int '-0x00000006e'
GXDMM_CAL_HiRes100_Ohms2W = 9 # Variable c_int '9'
GXDMM_FUNCTION_CONTINUITY = 8 # Variable c_int '8'
GXDMM_CAL_HiRes100mADC = 6 # Variable c_int '6'
GXDMM_CAL_HiRes100mVDC = 0 # Variable c_int '0'
GXDMM_RANGE_10mArms = 0.01 # Variable c_double '1.0000000000000000208166817117216851329430937767e-2'
GXDMM_ERROR_INVALID_AUTO_ZERO_MODE = -143 # Variable c_int '-0x00000008f'
GXDMM_CAL_Daq2ADC = 36 # Variable c_int '36'
GXDMM_ERROR_ABORTED_VALUE = -90 # Variable c_int '-0x00000005a'
GXDMM_CAL_HiRes1k_Ohms4W = 17 # Variable c_int '17'
GXDMM_RESOLUTION_4_5_DIGITS = 5 # Variable c_int '5'
GXDMM_CAL_HiRes20mADC = 5 # Variable c_int '5'
GXDMM_RANGE_1mA = 0.001 # Variable c_double '1.0000000000000000208166817117216851329430937767e-3'
GXDMM_CAL_HiRes10k_Ohms4W = 18 # Variable c_int '18'
GXDMM_CAL_Daq100mVDC = 28 # Variable c_int '28'
GXDMM_RANGE_50mArms = 0.05 # Variable c_double '5.00000000000000027755575615628913510590791702271e-2'
GXDMM_ERROR_DATA_NT_READ_WARN = -96 # Variable c_int '-0x000000060'
GXDMM_ERROR_BUSY = -91 # Variable c_int '-0x00000005b'
GXDMM_RANGE_2A = 2.0 # Variable c_double '2.0e+0'
GXDMM_ERROR_MIN_MAX_NOT_SET = -95 # Variable c_int '-0x00000005f'
GXDMM_RANGE_50mVrms = 0.05 # Variable c_double '5.00000000000000027755575615628913510590791702271e-2'
GXDMM_ERROR_CAL_SET_LENGTH_TOO_LONG = -118 # Variable c_int '-0x000000076'
GXDMM_ERROR_GENERAL_ERROR = -101 # Variable c_int '-0x000000065'
GXDMM_AUTO_ZERO_OFF = 1 # Variable c_int '1'
GXDMM_ERROR_FLASH_BAD_SIGNATURE = -115 # Variable c_int '-0x000000073'
GXDMM_ERROR_INVALID_DIGITIZER_CLOCK_DIVISOR = -139 # Variable c_int '-0x00000008b'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x000000015'
GXDMM_CAL_HiRes100k_Ohms4W = 19 # Variable c_int '19'
GXDMM_AC_MATH_AVG = 1 # Variable c_int '1'
GXDMM_ERROR_INVALID_CAL_SET = -135 # Variable c_int '-0x000000087'
GXDMM_CAL_Daq100VDC = 31 # Variable c_int '31'
GXDMM_RESOLUTION_6_5_DIGITS = 7 # Variable c_int '7'
GXDMM_CAL_Daq1AAC = 44 # Variable c_int '44'
GXDMM_FUNCTION_VDC = 0 # Variable c_int '0'
GXDMM_RANGE_300V = 300.0 # Variable c_double '3.0e+2'
GXDMM_WARNING_OVERFLOW = 100 # Variable c_int '100'
GXDMM_TRIGGER_ARRAY = 4 # Variable c_int '4'
GT_VISA_GETATTRIBUTE_ERROR = -33 # Variable c_int '-0x000000021'
GXDMM_ERROR_CAL_SET_BAD_CHECKSUM = -119 # Variable c_int '-0x000000077'
GXDMM_RANGE_10KOhm = 10000 # Variable c_int '10000'
GXDMM_ERROR_WRAP_AROUND = -111 # Variable c_int '-0x00000006f'
GXDMM_TRIGGER_CONTINUOUS = 0 # Variable c_int '0'
GXDMM_FUNCTION_TEMPERATURE = 11 # Variable c_int '11'
GXDMM_ERROR_INVALID_RESOLUTION = -124 # Variable c_int '-0x00000007c'
GT_VISA_OPEN_ERROR = -32 # Variable c_int '-0x000000020'
GT_VISA_OPENDEFAULTRM_ERROR = -31 # Variable c_int '-0x00000001f'
GXDMM_FUNCTION_2WIRE_OHM = 6 # Variable c_int '6'
GXDMM_CAL_Daq1VDC = 29 # Variable c_int '29'
GXDMM_ERROR_INVALID_CAL_SET_HEADER_CHECKSUM = -116 # Variable c_int '-0x000000074'
GXDMM_ERROR_NOT_SUPPORTED = -106 # Variable c_int '-0x00000006a'
GXDMM_RANGE_10V = 10.0 # Variable c_double '1.0e+1'
GXDMM_ERROR_MEM_ADDR = -201 # Variable c_int '-0x0000000c9'
GXDMM_FUNCTION_IAC_AC_CPL = 3 # Variable c_int '3'
GXDMM_ERROR_DEVICE_BUSY = -108 # Variable c_int '-0x00000006c'
GXDMM_CAL_HiRes100k_Ohms2W = 12 # Variable c_int '12'
GXDMM_ERROR_ARRAY_EMPTY = -94 # Variable c_int '-0x00000005e'
GXDMM_CAL_HiRes1ADC = 7 # Variable c_int '7'
GXDMM_AC_MATH_RMS = 0 # Variable c_int '0'
GT_VISA_MEMMAP_ERROR = -35 # Variable c_int '-0x000000023'
GXDMM_LINE_FREQUENCY_50HZ = 50 # Variable c_int '50'
GXDMM_ERROR_ARRAY_OUT_BNDS = -93 # Variable c_int '-0x00000005d'
GXDMM_ERROR_BAD_PARAMETER = -102 # Variable c_int '-0x000000066'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x00000000b'
GXDMM_ERROR_MEM_ECHB = -203 # Variable c_int '-0x0000000cb'
GXDMM_AC_MATH_PKAMP = 3 # Variable c_int '3'
GXDMM_CAL_Daq20mADC = 33 # Variable c_int '33'
GXDMM_CALSET_USER_CALIBRATION = 0 # Variable c_int '0'
GXDMM_FUNCTION_FREQUENCY = 9 # Variable c_int '9'
GXDMM_CAL_Daq300VDC = 32 # Variable c_int '32'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x000000006'
GXDMM_CALSET_FACTORY_CALIBRATION = 1 # Variable c_int '1'
GXDMM_ERROR_INVALID_DAQ_BUFFER_POINTER = -127 # Variable c_int '-0x00000007f'
GXDMM_CAL_HiRes10M_Ohms4W = 21 # Variable c_int '21'
GXDMM_ERROR_NOT_FOUND = -104 # Variable c_int '-0x000000068'
GXDMM_FUNCTION_BOARD_TEMP = 12 # Variable c_int '12'
GXDMM_CAL_HiRes300VDC = 4 # Variable c_int '4'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x00000000d'
GT_INVALID_ERROR = -20 # Variable c_int '-0x000000014'
GXDMM_RANGE_10uA = 1e-05 # Variable c_double '1.00000000000000008180305391403130954586231382564e-5'
GXDMM_CAL_HiRes100mVSHiDC = 23 # Variable c_int '23'
GXDMM_ERROR_CAL_SET_DOES_NOT_EXIST = -117 # Variable c_int '-0x000000075'
GXDMM_CAL_HiRes100M_Ohms2W = 15 # Variable c_int '15'
GXDMM_ERROR_INVALID_RANGE = -123 # Variable c_int '-0x00000007b'
GXDMM_ERROR_NO_CALIBRATION = -142 # Variable c_int '-0x00000008e'
GXDMM_CAL_HiRes1VDC = 1 # Variable c_int '1'
GXDMM_ERROR_MEM_DATA = -200 # Variable c_int '-0x0000000c8'
GT_WRONG_BOARD = -3 # Variable c_int '-0x000000003'
GXDMM_TRIGGER_EXTERNAL = 2 # Variable c_int '2'
GXDMM_RANGE_300Vrms = 300.0 # Variable c_double '3.0e+2'
GXDMM_CAL_Daq100mVAC = 37 # Variable c_int '37'
GXDMM_CAL_Daq100mADC = 34 # Variable c_int '34'
GT_SYNC_CREATE = -37 # Variable c_int '-0x000000025'
GXDMM_RANGE_100KOhm = 100000 # Variable c_int '100000'
GXDMM_RANGE_500mArms = 0.5 # Variable c_double '5.0e-1'
GXDMM_ERROR_TIMER_ALTER = -107 # Variable c_int '-0x00000006b'
GXDMM_ERROR_GENERAL_WARNING = -97 # Variable c_int '-0x000000061'
GXDMM_ERROR_INVALID_CAL = -133 # Variable c_int '-0x000000085'
GT_VISA_LOAD_DLL_ERROR = -30 # Variable c_int '-0x00000001e'
GXDMM_ERROR_CONTROLER_TIMEOUT = -141 # Variable c_int '-0x00000008d'
GXDMM_ERROR_SOFTWARE_TIMEOUT = -120 # Variable c_int '-0x000000078'
GXDMM_ERROR_INVALID_HIRES_BUFFER_POINTER = -129 # Variable c_int '-0x000000081'
GXDMM_FUNCTION_IAC_DC_CPL = 5 # Variable c_int '5'
GXDMM_TRIGGER_TIMER = 1 # Variable c_int '1'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x00000000c'
GXDMM_FUNCTION_VAC_AC_CPL = 2 # Variable c_int '2'
GXDMM_ERROR_INVALID_AC_LINE_FREQUENCY = -138 # Variable c_int '-0x00000008a'
GXDMM_ERROR_SPI_BUSY = -103 # Variable c_int '-0x000000067'
GT_VISA_VIIN_ERROR = -34 # Variable c_int '-0x000000022'
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x00000000a'
GXDMM_CALSET_FOR_CALIBRATION = 2 # Variable c_int '2'
GXDMM_RANGE_50Vrms = 50.0 # Variable c_double '5.0e+1'
GXDMM_ERROR_INVALID_TRIGGER_READING = -125 # Variable c_int '-0x00000007d'
GXDMM_FUNCTION_VAC_DC_CPL = 4 # Variable c_int '4'
GXDMM_ERROR_MEM_BHWA = -202 # Variable c_int '-0x0000000ca'
GXDMM_CAL_HiRes2ADC = 8 # Variable c_int '8'
GXDMM_ERROR_INVALID_DAQ_BUFFER_COUNT = -128 # Variable c_int '-0x000000080'
GXDMM_FUNCTION_IDC = 1 # Variable c_int '1'
GXDMM_ERROR_INVALID_DAQ_MATH_TYPE = -132 # Variable c_int '-0x000000084'
GT_INVALID_SLOT = -22 # Variable c_int '-0x000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x000000009'
GXDMM_OVERFLOW_MEASUREMENT = 1000000000000.0 # Variable c_double '1.0e+12'
GT_SYNC_TIMEOUT = -38 # Variable c_int '-0x000000026'
GXDMM_CAL_HiRes100_Ohms4W = 16 # Variable c_int '16'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x000000001'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x000000002'
GXDMM_CAL_Daq300VAC = 41 # Variable c_int '41'
GXDMM_LINE_FREQUENCY_60HZ = 60 # Variable c_int '60'
GXDMM_CAL_HiRes10M_Ohms2W = 14 # Variable c_int '14'
GXDMM_PANEL_MODAL = 1 # Variable c_int '1'
GXDMM_CAL_DaqTempTypeC = 54 # Variable c_int '54'
GXDMM_CAL_HiRes100VDC = 3 # Variable c_int '3'
GXDMM_CAL_DaqTempTypeE = 48 # Variable c_int '48'
GXDMM_RANGE_5Vrms = 5.0 # Variable c_double '5.0e+0'
GXDMM_CAL_Daq1VAC = 38 # Variable c_int '38'
GXDMM_CAL_HiRes10VDC = 2 # Variable c_int '2'
GXDMM_CAL_DaqTempTypeK = 47 # Variable c_int '47'
GXDMM_CAL_DaqTempTypeJ = 49 # Variable c_int '49'
GXDMM_CAL_DaqTempTypeM = 55 # Variable c_int '55'
GXDMM_RANGE_1MOhm = 1000000 # Variable c_int '1000000'
GXDMM_CAL_DaqTempTypeS = 52 # Variable c_int '52'
GXDMM_CAL_HiRes10VSHiDC = 25 # Variable c_int '25'
GXDMM_CAL_HiRes10k_Ohms2W = 11 # Variable c_int '11'
GXDMM_RANGE_1KOhm = 1000 # Variable c_int '1000'
GXDMM_CAL_HiRes1M_Ohms2W = 13 # Variable c_int '13'
GXDMM_RESOLUTION_5_5_DIGITS = 6 # Variable c_int '6'
GXDMM_ERROR_INVALID_HIRES_BUFFER_COUNT = -130 # Variable c_int '-0x000000082'
GXDMM_RANGE_1V = 1.0 # Variable c_double '1.0e+0'
GXDMM_AC_MATH_PP = 2 # Variable c_int '2'
GXDMM_RANGE_20mA = 0.02 # Variable c_double '2.00000000000000004163336342344337026588618755341e-2'
GXDMM_CAL_DaqTempTypeR = 51 # Variable c_int '51'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x000000004'
GXDMM_CAL_DaqTempTypeB = 46 # Variable c_int '46'
GXDMM_RANGE_1A = 1.0 # Variable c_double '1.0e+0'
GXDMM_LINE_FREQUENCY_400HZ = 400 # Variable c_int '400'
GXDMM_CAL_HiRes100M_Ohms4W = 22 # Variable c_int '22'
GXDMM_CAL_Daq1ADC = 35 # Variable c_int '35'
GXDMM_RANGE_500mVrms = 0.5 # Variable c_double '5.0e-1'
GXDMM_RANGE_100mV = 0.1 # Variable c_double '1.00000000000000005551115123125782702118158340454e-1'
GXDMM_ERROR_END_OF_BUFFER = -114 # Variable c_int '-0x000000072'
GXDMM_RANGE_100MOhm = 100000000 # Variable c_int '100000000'
GXDMM_ERROR_INVALID_BUFFER_TYPE = -140 # Variable c_int '-0x00000008c'
GXDMM_RANGE_100V = 100.0 # Variable c_double '1.0e+2'
GXDMM_RANGE_100uA = 0.0001 # Variable c_double '1.00000000000000004792173602385929598312941379845e-4'
GXDMM_ERROR_RUN_GTBN = -105 # Variable c_int '-0x000000069'
GT_INVALID_MODE = -25 # Variable c_int '-0x000000019'
GXDMM_RANGE_100mA = 0.1 # Variable c_double '1.00000000000000005551115123125782702118158340454e-1'
GXDMM_AUTO_ZERO_NOW = 2 # Variable c_int '2'
GXDMM_ERROR_INVALID_AC_MIN_FREQ = -136 # Variable c_int '-0x000000088'
GXDMM_CAL_HiRes1VSHiDC = 24 # Variable c_int '24'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x000000017'
GXDMM_CAL_Daq10VAC = 39 # Variable c_int '39'
GT_LICENSE = -40 # Variable c_int '-0x000000028'
CHAR = c_char
BYTE = c_ubyte
SHORT = c_short
WORD = c_ushort
INT = c_int
UINT = c_uint
DLONG = c_longlong
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
GxDmmGetDriverSummary = _libraries['libGxDmm.so'].GxDmmGetDriverSummary
GxDmmGetDriverSummary.restype = None
GxDmmGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
GxDmmGetErrorString = _libraries['libGxDmm.so'].GxDmmGetErrorString
GxDmmGetErrorString.restype = None
GxDmmGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxDmmInitialize = _libraries['libGxDmm.so'].GxDmmInitialize
GxDmmInitialize.restype = None
GxDmmInitialize.argtypes = [SHORT, PSHORT, PSHORT]
GxDmmInitializeVisa = _libraries['libGxDmm.so'].GxDmmInitializeVisa
GxDmmInitializeVisa.restype = None
GxDmmInitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
GxDmmGetCalibrationInfo = _libraries['libGxDmm.so'].GxDmmGetCalibrationInfo
GxDmmGetCalibrationInfo.restype = None
GxDmmGetCalibrationInfo.argtypes = [SHORT, PSTR, SHORT, PSHORT, PSHORT]
GxDmmGetBoardSummary = _libraries['libGxDmm.so'].GxDmmGetBoardSummary
GxDmmGetBoardSummary.restype = None
GxDmmGetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxDmmReset = _libraries['libGxDmm.so'].GxDmmReset
GxDmmReset.restype = None
GxDmmReset.argtypes = [SHORT, PSHORT]
GxDmmPanel = _libraries['libGxDmm.so'].GxDmmPanel
GxDmmPanel.restype = None
GxDmmPanel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
GxDmmSetRelative = _libraries['libGxDmm.so'].GxDmmSetRelative
GxDmmSetRelative.restype = None
GxDmmSetRelative.argtypes = [SHORT, BOOL, PSHORT]
GxDmmGetRelative = _libraries['libGxDmm.so'].GxDmmGetRelative
GxDmmGetRelative.restype = None
GxDmmGetRelative.argtypes = [SHORT, PBOOL, PSHORT]
GxDmmMeasure = _libraries['libGxDmm.so'].GxDmmMeasure
GxDmmMeasure.restype = None
GxDmmMeasure.argtypes = [SHORT, PDOUBLE, PSHORT]
GxDmmMeasureEx = _libraries['libGxDmm.so'].GxDmmMeasureEx
GxDmmMeasureEx.restype = None
GxDmmMeasureEx.argtypes = [SHORT, PDOUBLE, PSTR, PSTR, PDDWORD, PSHORT]
GxDmmRead = _libraries['libGxDmm.so'].GxDmmRead
GxDmmRead.restype = None
GxDmmRead.argtypes = [SHORT, PDOUBLE, PSHORT]
GxDmmReadEx = _libraries['libGxDmm.so'].GxDmmReadEx
GxDmmReadEx.restype = None
GxDmmReadEx.argtypes = [SHORT, PDOUBLE, PSTR, PSTR, PDDWORD, PSHORT]
GxDmmReadArray = _libraries['libGxDmm.so'].GxDmmReadArray
GxDmmReadArray.restype = None
GxDmmReadArray.argtypes = [SHORT, PDOUBLE, PDDWORD, DWORD, PSHORT]
GxDmmGetReadArrayStatus = _libraries['libGxDmm.so'].GxDmmGetReadArrayStatus
GxDmmGetReadArrayStatus.restype = None
GxDmmGetReadArrayStatus.argtypes = [SHORT, PBOOL, PDWORD, PSHORT]
GxDmmGetReadStatus = _libraries['libGxDmm.so'].GxDmmGetReadStatus
GxDmmGetReadStatus.restype = None
GxDmmGetReadStatus.argtypes = [SHORT, PBOOL, PSHORT]
GxDmmTrig = _libraries['libGxDmm.so'].GxDmmTrig
GxDmmTrig.restype = None
GxDmmTrig.argtypes = [SHORT, PSHORT]
GxDmmAbortReading = _libraries['libGxDmm.so'].GxDmmAbortReading
GxDmmAbortReading.restype = None
GxDmmAbortReading.argtypes = [SHORT, PSHORT]
GxDmmSetFunction = _libraries['libGxDmm.so'].GxDmmSetFunction
GxDmmSetFunction.restype = None
GxDmmSetFunction.argtypes = [SHORT, DWORD, PSHORT]
GxDmmGetFunction = _libraries['libGxDmm.so'].GxDmmGetFunction
GxDmmGetFunction.restype = None
GxDmmGetFunction.argtypes = [SHORT, PDWORD, PSHORT]
GxDmmGetMinMax = _libraries['libGxDmm.so'].GxDmmGetMinMax
GxDmmGetMinMax.restype = None
GxDmmGetMinMax.argtypes = [SHORT, PDOUBLE, PDOUBLE, BOOL, PSHORT]
GxDmmSetLineFrequency = _libraries['libGxDmm.so'].GxDmmSetLineFrequency
GxDmmSetLineFrequency.restype = None
GxDmmSetLineFrequency.argtypes = [SHORT, DWORD, PSHORT]
GxDmmGetLineFrequency = _libraries['libGxDmm.so'].GxDmmGetLineFrequency
GxDmmGetLineFrequency.restype = None
GxDmmGetLineFrequency.argtypes = [SHORT, PDWORD, PSHORT]
GxDmmSetAutoZero = _libraries['libGxDmm.so'].GxDmmSetAutoZero
GxDmmSetAutoZero.restype = None
GxDmmSetAutoZero.argtypes = [SHORT, DWORD, PSHORT]
GxDmmGetAutoZero = _libraries['libGxDmm.so'].GxDmmGetAutoZero
GxDmmGetAutoZero.restype = None
GxDmmGetAutoZero.argtypes = [SHORT, PDWORD, PSHORT]
GxDmmSetACMath = _libraries['libGxDmm.so'].GxDmmSetACMath
GxDmmSetACMath.restype = None
GxDmmSetACMath.argtypes = [SHORT, DWORD, PSHORT]
GxDmmGetACMath = _libraries['libGxDmm.so'].GxDmmGetACMath
GxDmmGetACMath.restype = None
GxDmmGetACMath.argtypes = [SHORT, PDWORD, PSHORT]
GxDmmSetACMinFrequency = _libraries['libGxDmm.so'].GxDmmSetACMinFrequency
GxDmmSetACMinFrequency.restype = None
GxDmmSetACMinFrequency.argtypes = [SHORT, DOUBLE, PSHORT]
GxDmmGetACMinFrequency = _libraries['libGxDmm.so'].GxDmmGetACMinFrequency
GxDmmGetACMinFrequency.restype = None
GxDmmGetACMinFrequency.argtypes = [SHORT, PDOUBLE, PSHORT]
GxDmmSetACClockDivider = _libraries['libGxDmm.so'].GxDmmSetACClockDivider
GxDmmSetACClockDivider.restype = None
GxDmmSetACClockDivider.argtypes = [SHORT, DWORD, PSHORT]
GxDmmGetACClockDivider = _libraries['libGxDmm.so'].GxDmmGetACClockDivider
GxDmmGetACClockDivider.restype = None
GxDmmGetACClockDivider.argtypes = [SHORT, PDWORD, PSHORT]
GxDmmSetRange = _libraries['libGxDmm.so'].GxDmmSetRange
GxDmmSetRange.restype = None
GxDmmSetRange.argtypes = [SHORT, DOUBLE, PSHORT]
GxDmmGetRange = _libraries['libGxDmm.so'].GxDmmGetRange
GxDmmGetRange.restype = None
GxDmmGetRange.argtypes = [SHORT, PDOUBLE, PSHORT]
GxDmmSetAutoRange = _libraries['libGxDmm.so'].GxDmmSetAutoRange
GxDmmSetAutoRange.restype = None
GxDmmSetAutoRange.argtypes = [SHORT, BOOL, PSHORT]
GxDmmGetAutoRange = _libraries['libGxDmm.so'].GxDmmGetAutoRange
GxDmmGetAutoRange.restype = None
GxDmmGetAutoRange.argtypes = [SHORT, PBOOL, PSHORT]
GxDmmSetResolution = _libraries['libGxDmm.so'].GxDmmSetResolution
GxDmmSetResolution.restype = None
GxDmmSetResolution.argtypes = [SHORT, DWORD, PSHORT]
GxDmmGetResolution = _libraries['libGxDmm.so'].GxDmmGetResolution
GxDmmGetResolution.restype = None
GxDmmGetResolution.argtypes = [SHORT, PDWORD, PSHORT]
GxDmmSetTriggerMode = _libraries['libGxDmm.so'].GxDmmSetTriggerMode
GxDmmSetTriggerMode.restype = None
GxDmmSetTriggerMode.argtypes = [SHORT, DWORD, DWORD, PSHORT]
GxDmmGetTriggerMode = _libraries['libGxDmm.so'].GxDmmGetTriggerMode
GxDmmGetTriggerMode.restype = None
GxDmmGetTriggerMode.argtypes = [SHORT, PDWORD, PSHORT]
GxDmmSetExternalTriggers = _libraries['libGxDmm.so'].GxDmmSetExternalTriggers
GxDmmSetExternalTriggers.restype = None
GxDmmSetExternalTriggers.argtypes = [SHORT, DWORD, DWORD, PSHORT]
GxDmmGetExternalTriggers = _libraries['libGxDmm.so'].GxDmmGetExternalTriggers
GxDmmGetExternalTriggers.restype = None
GxDmmGetExternalTriggers.argtypes = [SHORT, PDWORD, PDWORD, PSHORT]
GxDmmSetAperture = _libraries['libGxDmm.so'].GxDmmSetAperture
GxDmmSetAperture.restype = None
GxDmmSetAperture.argtypes = [SHORT, DOUBLE, PSHORT]
GxDmmGetAperture = _libraries['libGxDmm.so'].GxDmmGetAperture
GxDmmGetAperture.restype = None
GxDmmGetAperture.argtypes = [SHORT, PDOUBLE, PSHORT]
GxDmmRestoreFactoryCalibration = _libraries['libGxDmm.so'].GxDmmRestoreFactoryCalibration
GxDmmRestoreFactoryCalibration.restype = None
GxDmmRestoreFactoryCalibration.argtypes = [SHORT, PSHORT]
GxDmmSetCalibrationSet = _libraries['libGxDmm.so'].GxDmmSetCalibrationSet
GxDmmSetCalibrationSet.restype = None
GxDmmSetCalibrationSet.argtypes = [SHORT, LONG, PSHORT]
GxDmmGetCalibrationSet = _libraries['libGxDmm.so'].GxDmmGetCalibrationSet
GxDmmGetCalibrationSet.restype = None
GxDmmGetCalibrationSet.argtypes = [SHORT, PLONG, PSHORT]
GxDmmSetCalibrationMeasurements = _libraries['libGxDmm.so'].GxDmmSetCalibrationMeasurements
GxDmmSetCalibrationMeasurements.restype = None
GxDmmSetCalibrationMeasurements.argtypes = [SHORT, DWORD, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, PSHORT]
GxDmmWriteCalibrationEEPROM = _libraries['libGxDmm.so'].GxDmmWriteCalibrationEEPROM
GxDmmWriteCalibrationEEPROM.restype = None
GxDmmWriteCalibrationEEPROM.argtypes = [SHORT, PSHORT]
__all__ = ['GXDMM_RANGE_1Arms', 'GxDmmRead', 'GXDMM_PANEL_MODELESS',
           'GXDMM_CAL_Daq100mAAC', 'GT_NO_ERROR',
           'GXDMM_ERROR_INVALID_CAL_GROUP',
           'GXDMM_RESOLUTION_4_5_DIGITS', 'GT_UNABLE_REGISTER_DEVICE',
           'GxDmmMeasureEx', 'GXDMM_ERROR_READ_ONLY_COMMAND',
           'GXDMM_CAL_Daq100mADC',
           'GXDMM_ERROR_INVALID_TRIGGER_TIMER_RATE',
           'GXDMM_CAL_HiResVCalOpen', 'GXDMM_RANGE_1MOhm', 'BYTE',
           'GxDmmGetExternalTriggers', 'GT_INVALID_STRLEN',
           'GXDMM_CAL_Daq100VAC', 'GXDMM_TRIGGER_SOFTWARE',
           'GT_LVRT_UNSUPPORTED', 'GXDMM_WARNING_TIMEOUT', 'LONG',
           'GXDMM_RANGE_500mArms', 'GXDMM_AUTO_ZERO_ON',
           'GxDmmGetRange', 'GXDMM_RANGE_10MOhm',
           'GXDMM_CAL_HiRes1M_Ohms4W', 'PCSTR',
           'GXDMM_ERROR_READ_ERROR', 'GT_UNABLE_CREATE_PANEL',
           'GXDMM_ERROR_INVALID_DAQ_ARRAY',
           'GXDMM_FUNCTION_4WIRE_OHM', 'GXDMM_RANGE_1KOhm',
           'GXDMM_FUNCTION_DIODE', 'GXDMM_CAL_Daq20mAAC',
           'GXDMM_ERROR_MBOARD_NOT_PRESENT', 'PSTR',
           'GXDMM_CAL_HiRes_R_Ref', 'GXDMM_CAL_Daq2AAC',
           'GxDmmMeasure', 'GXDMM_ERROR_COMM',
           'GXDMM_RESOLUTION_3_5_DIGITS',
           'GXDMM_ERROR_INVALID_APERTURE', 'GXDMM_CAL_Daq10VDC',
           'GxDmmSetAutoRange', 'GXDMM_ERROR_TIMER_ALTER',
           'GXDMM_AC_MATH_RMS', 'CHAR', 'GXDMM_CAL_HiRes100_Ohms2W',
           'GXDMM_FUNCTION_CONTINUITY', 'DOUBLE',
           'GxDmmRestoreFactoryCalibration', 'GxDmmReadArray',
           'GXDMM_CAL_Daq100mVDC', 'PDDWORD',
           'GXDMM_CAL_HiRes100mVDC', 'GxDmmGetMinMax',
           'GXDMM_RANGE_10mArms', 'HWND',
           'GXDMM_ERROR_MIN_MAX_NOT_SET', 'GxDmmGetDriverSummary',
           'GXDMM_ERROR_INVALID_AUTO_ZERO_MODE',
           'GxDmmSetACClockDivider', 'GXDMM_CAL_Daq2ADC', 'SHORT',
           'GXDMM_ERROR_ABORTED_VALUE', 'GXDMM_RANGE_1V',
           'GXDMM_CAL_HiRes20mADC', 'GxDmmGetCalibrationSet',
           'GxDmmGetCalibrationInfo', 'GxDmmSetAutoZero',
           'GxDmmGetLineFrequency', 'GXDMM_RANGE_1mA',
           'GXDMM_FUNCTION_IDC', 'PBYTE', 'GXDMM_CAL_HiRes100mADC',
           'GXDMM_ERROR_SOFTWARE_TIMEOUT', 'GxDmmSetFunction',
           'GXDMM_RANGE_50mArms', 'DDWORD', 'GxDmmInitialize',
           'GXDMM_ERROR_DATA_NT_READ_WARN', 'GXDMM_ERROR_BUSY',
           'GXDMM_RANGE_2A', 'GXDMM_ERROR_CAL_LICENSE',
           'GxDmmSetExternalTriggers', 'GxDmmWriteCalibrationEEPROM',
           'GXDMM_ERROR_INVALID_HIRES_BUFFER_POINTER',
           'GXDMM_ERROR_CAL_SET_LENGTH_TOO_LONG',
           'GXDMM_ERROR_GENERAL_ERROR', 'GXDMM_AUTO_ZERO_OFF',
           'GXDMM_ERROR_FLASH_BAD_SIGNATURE',
           'GXDMM_ERROR_INVALID_DIGITIZER_CLOCK_DIVISOR',
           'GxDmmSetRange', 'GXDMM_CAL_HiRes1k_Ohms2W',
           'GxDmmGetResolution', 'GT_INVALID_PARAMETER',
           'GxDmmGetAperture', 'GxDmmGetFunction',
           'GXDMM_TRIGGER_TIMER', 'GXDMM_ERROR_INVALID_CAL_SET',
           'GxDmmSetTriggerMode', 'GT_NOT_CALIBRATED',
           'GXDMM_CAL_Daq1AAC', 'GXDMM_FUNCTION_VDC',
           'GxDmmGetReadArrayStatus', 'DLONG', 'GXDMM_RANGE_300V',
           'GXDMM_WARNING_OVERFLOW', 'GXDMM_TRIGGER_ARRAY',
           'GxDmmSetResolution', 'GT_VISA_GETATTRIBUTE_ERROR',
           'PDOUBLE', 'WORD', 'GxDmmGetACMath',
           'GXDMM_ERROR_CAL_SET_BAD_CHECKSUM', 'GxDmmGetErrorString',
           'GXDMM_RANGE_10KOhm', 'PSHORT', 'GxDmmGetACMinFrequency',
           'GXDMM_ERROR_WRAP_AROUND', 'GXDMM_CAL_HiRes10k_Ohms4W',
           'INT', 'GXDMM_FUNCTION_TEMPERATURE',
           'GXDMM_ERROR_INVALID_RESOLUTION', 'GT_VISA_OPEN_ERROR',
           'GXDMM_RANGE_500mVrms', 'GT_VISA_OPENDEFAULTRM_ERROR',
           'GXDMM_FUNCTION_2WIRE_OHM', 'GXDMM_CAL_Daq1VDC',
           'GXDMM_ERROR_INVALID_CAL_SET_HEADER_CHECKSUM',
           'GXDMM_ERROR_NOT_SUPPORTED', 'PLONG', 'GXDMM_RANGE_10V',
           'GXDMM_ERROR_MEM_ADDR', 'GXDMM_FUNCTION_IAC_AC_CPL',
           'GXDMM_ERROR_DEVICE_BUSY', 'GXDMM_CALSET_FOR_CALIBRATION',
           'GXDMM_ERROR_ARRAY_EMPTY', 'GXDMM_CAL_HiRes1ADC',
           'GXDMM_CAL_HiRes100k_Ohms4W', 'GT_VISA_MEMMAP_ERROR',
           'GXDMM_LINE_FREQUENCY_50HZ', 'GXDMM_ERROR_ARRAY_OUT_BNDS',
           'PBOOL', 'GXDMM_ERROR_BAD_PARAMETER',
           'GT_NOT_IN_CALIBRATION_MODE', 'GXDMM_CAL_HiRes100M_Ohms4W',
           'GXDMM_AC_MATH_PKAMP', 'GXDMM_CAL_Daq20mADC',
           'GXDMM_CALSET_USER_CALIBRATION',
           'GXDMM_FUNCTION_FREQUENCY', 'GXDMM_CAL_Daq300VDC',
           'PDWORD', 'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GXDMM_CALSET_FACTORY_CALIBRATION',
           'GXDMM_ERROR_INVALID_DAQ_BUFFER_POINTER',
           'GXDMM_CAL_HiRes10M_Ohms4W', 'GXDMM_ERROR_NOT_FOUND',
           'GXDMM_FUNCTION_BOARD_TEMP', 'GXDMM_ERROR_MEM_BHWA',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GT_INVALID_ERROR',
           'GXDMM_RANGE_10uA', 'GXDMM_CAL_HiRes100mVSHiDC',
           'GXDMM_ERROR_CAL_SET_DOES_NOT_EXIST',
           'GxDmmGetTriggerMode', 'GXDMM_CAL_HiRes100M_Ohms2W',
           'GxDmmSetCalibrationSet', 'GxDmmSetACMinFrequency',
           'GXDMM_ERROR_NO_CALIBRATION',
           'GXDMM_RESOLUTION_6_5_DIGITS', 'GXDMM_ERROR_MEM_DATA',
           'GT_WRONG_BOARD', 'GXDMM_TRIGGER_EXTERNAL',
           'GXDMM_RANGE_300Vrms', 'GxDmmGetAutoZero',
           'GXDMM_CAL_Daq100mVAC', 'GT_SLOT_NOT_CONFIG',
           'GXDMM_RANGE_100Ohm', 'GT_SYNC_CREATE',
           'GXDMM_ERROR_INVALID_FUNCTION',
           'GxDmmSetCalibrationMeasurements', 'PVOID',
           'GXDMM_ERROR_FLASH_FAIL', 'GXDMM_ERROR_GENERAL_WARNING',
           'GxDmmGetRelative', 'GXDMM_ERROR_INVALID_CAL',
           'GT_VISA_LOAD_DLL_ERROR', 'GXDMM_ERROR_CONTROLER_TIMEOUT',
           'GxDmmPanel', 'GXDMM_TRIGGER_CONTINUOUS',
           'GxDmmInitializeVisa', 'GXDMM_RANGE_50mVrms',
           'GXDMM_FUNCTION_IAC_DC_CPL', 'BOOL', 'GXDMM_AC_MATH_AVG',
           'GXDMM_CAL_Daq100VDC', 'GXDMM_FUNCTION_VAC_AC_CPL',
           'GXDMM_ERROR_INVALID_AC_LINE_FREQUENCY',
           'GXDMM_ERROR_SPI_BUSY', 'GT_VISA_VIIN_ERROR',
           'GxDmmReadEx', 'GT_BOARD_INVALID_EEPROM',
           'GXDMM_CAL_HiRes100k_Ohms2W', 'GXDMM_RANGE_50Vrms',
           'GxDmmSetLineFrequency',
           'GXDMM_ERROR_INVALID_TRIGGER_READING',
           'GXDMM_FUNCTION_VAC_DC_CPL', 'GXDMM_CAL_HiRes300VDC',
           'GXDMM_CAL_HiRes100_Ohms4W',
           'GXDMM_ERROR_INVALID_DAQ_BUFFER_COUNT',
           'GXDMM_RANGE_100KOhm', 'GXDMM_ERROR_INVALID_DAQ_MATH_TYPE',
           'GT_INVALID_SLOT', 'GT_UNABLE_TO_GETTIMER',
           'GXDMM_OVERFLOW_MEASUREMENT', 'GT_SYNC_TIMEOUT',
           'GXDMM_CAL_HiRes2ADC', 'GT_CANT_OPEN_HW',
           'GT_BOARD_NOT_EXIST', 'GXDMM_CAL_Daq300VAC',
           'GXDMM_LINE_FREQUENCY_60HZ', 'GXDMM_CAL_HiRes10M_Ohms2W',
           'GXDMM_PANEL_MODAL', 'GXDMM_CAL_DaqTempTypeC',
           'GXDMM_CAL_HiRes100VDC', 'GXDMM_CAL_DaqTempTypeE',
           'GxDmmAbortReading', 'GXDMM_RANGE_5Vrms',
           'GXDMM_CAL_Daq1VAC', 'GXDMM_CAL_HiRes10VDC', 'GxDmmReset',
           'GXDMM_CAL_DaqTempTypeK', 'GXDMM_CAL_DaqTempTypeJ',
           'GXDMM_CAL_DaqTempTypeM', 'GXDMM_CAL_DaqTempTypeN',
           'GXDMM_CAL_DaqTempTypeS', 'GXDMM_CAL_HiRes10VSHiDC',
           'GXDMM_CAL_HiRes10k_Ohms2W', 'GXDMM_CAL_DaqTempTypeT',
           'GxDmmSetAperture', 'GXDMM_CAL_HiRes1M_Ohms2W',
           'GXDMM_RESOLUTION_5_5_DIGITS',
           'GXDMM_ERROR_INVALID_HIRES_BUFFER_COUNT', 'PWORD',
           'GXDMM_CAL_HiRes1k_Ohms4W',
           'GXDMM_ERROR_INVALID_BUFFER_TYPE', 'GXDMM_AC_MATH_PP',
           'GXDMM_ERROR_INVALID_AC_MIN_FREQ', 'GxDmmSetRelative',
           'GxDmmTrig', 'GxDmmGetACClockDivider',
           'GXDMM_CAL_DaqTempTypeR', 'GXDMM_CAL_HiRes1VDC', 'DWORD',
           'GXDMM_CAL_DaqTempTypeB', 'UINT', 'GXDMM_RANGE_1A',
           'GXDMM_LINE_FREQUENCY_400HZ', 'GXDMM_ERROR_MEM_ECHB',
           'GxDmmGetBoardSummary', 'GxDmmGetReadStatus',
           'GXDMM_CAL_Daq1ADC', 'GXDMM_ERROR_INVALID_RANGE',
           'GXDMM_RANGE_100mV', 'GXDMM_ERROR_END_OF_BUFFER',
           'GXDMM_RANGE_100MOhm', 'GT_UNABLE_ALLOC_MEMORY',
           'GXDMM_RANGE_100V', 'GXDMM_RANGE_100uA',
           'GXDMM_ERROR_RUN_GTBN', 'GxDmmGetAutoRange',
           'GT_INVALID_MODE', 'GXDMM_RANGE_100mA',
           'GXDMM_AUTO_ZERO_NOW', 'GXDMM_RANGE_20mA',
           'GXDMM_CAL_HiRes1VSHiDC', 'GT_INVALID_HANDLE',
           'GXDMM_CAL_Daq10VAC', 'GxDmmSetACMath', 'GT_LICENSE']
