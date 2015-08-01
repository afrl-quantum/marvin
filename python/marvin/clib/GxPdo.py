from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxPdo.so'] = CDLL('libGxPdo.so')


# VOID = void # alias
GX3348_RAIL_SOURCE_EXTERNAL_AMPLIFIED = 3 # Variable c_int '3'
GT_NO_ERROR = 0 # Variable c_int '0'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x000000005'
GXPDO_UNABLE_TO_SET_DAC = -70 # Variable c_int '-0x000000046'
GX3348_CAL_MODE_DISABLED = 0 # Variable c_int '0'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x000000018'
GX3348_RAIL_GND = 3 # Variable c_int '3'
GT_LVRT_UNSUPPORTED = -39 # Variable c_int '-0x000000027'
GX3348_RAIL_NONE = -1 # Variable c_int '-0x000000001'
GX3348_CAL_MODE_ENABLED = 1 # Variable c_int '1'
GX3348_RAIL_B = 1 # Variable c_int '1'
GX3348_RAIL_C = 2 # Variable c_int '2'
GX3348_RAIL_A = 0 # Variable c_int '0'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x000000008'
GX3348_RAIL_DAC_C = 2 # Variable c_int '2'
GX3348_RAIL_DAC_B = 1 # Variable c_int '1'
GX3348_RAIL_DAC_A = 0 # Variable c_int '0'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x000000002'
GXPDO_INVALID_GROUP = -56 # Variable c_int '-0x000000038'
GX1838_SOURCE_EXTERNAL = 2 # Variable c_int '2'
GX1838_DAC_MAX_VOLTAGE = 32.0 # Variable c_double '3.2e+1'
GXPDO_INVALID_OFFSET_VAL = -58 # Variable c_int '-0x00000003a'
GX1838_DAC_C = 2 # Variable c_int '2'
GX1838_DAC_B = 1 # Variable c_int '1'
GX1838_DAC_A = 0 # Variable c_int '0'
GX1838_CAL_LOW_VOLTAGE = 0 # Variable c_int '0'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x00000000b'
GX1838_CAL_MIN_LOAD_VALUE = 64 # Variable c_int '64'
GXPDO_INVALID_RAIL_SOURCE = -55 # Variable c_int '-0x000000037'
GX3348_DAC_RAIL_A = 0 # Variable c_int '0'
GX3348_DAC_RAIL_C = 2 # Variable c_int '2'
GX3348_DAC_RAIL_B = 1 # Variable c_int '1'
GX1838_CAL_HIGH_VOLTAGE = 1 # Variable c_int '1'
GX3348_CAL_DAC_VOLTAGE_POINT_NEGATIVE = 1 # Variable c_int '1'
GXPDO_INVALID_DAC_VOLTAGE = -53 # Variable c_int '-0x000000035'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x000000015'
GXPDO_CAL_BY_USER_ERR_SEQUENCE = -80 # Variable c_int '-0x000000050'
GX1838_SOURCE_INTERNAL = 1 # Variable c_int '1'
GXPDO_CAL_BY_USER_INVALID_CALIBRATION_DATA = -81 # Variable c_int '-0x000000051'
GT_VISA_GETATTRIBUTE_ERROR = -33 # Variable c_int '-0x000000021'
GXPDO_INVALID_RAIL = -54 # Variable c_int '-0x000000036'
GX3348_CAL_DAC_VOLTAGE_POINT_POSITIVE = 2 # Variable c_int '2'
GX3348_RAIL_SOURCE_INTERNAL_5V = 2 # Variable c_int '2'
GT_VISA_OPEN_ERROR = -32 # Variable c_int '-0x000000020'
GT_VISA_OPENDEFAULTRM_ERROR = -31 # Variable c_int '-0x00000001f'
GXPDO_INVALID_CHANNEL = -50 # Variable c_int '-0x000000032'
GT_INVALID_MODE = -25 # Variable c_int '-0x000000019'
GT_VISA_MEMMAP_ERROR = -35 # Variable c_int '-0x000000023'
GX3348_CAL_DAC_VOLTAGE_POINT_ZERO = 0 # Variable c_int '0'
GX1838_SOURCE_OPEN = 0 # Variable c_int '0'
GX1838_CAL_DATA_FACTORY = 1 # Variable c_int '1'
GXPDO_ADC_MEASURE_TIMEOUT = -61 # Variable c_int '-0x00000003d'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x000000006'
GX1838_CAL_DATA_USER_VOLATILE = 4 # Variable c_int '4'
GXPDO_INVALID_CHANNEL_RAIL = -51 # Variable c_int '-0x000000033'
GX3348_RAIL_SOURCE_EXTERNAL = 1 # Variable c_int '1'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x00000000d'
GT_INVALID_ERROR = -20 # Variable c_int '-0x000000014'
GX1838_DAC_MIN_VOLTAGE = -10.0 # Variable c_double '-1.0e+1'
GX1838_RAIL_B = 2 # Variable c_int '2'
GX1838_RAIL_C = 3 # Variable c_int '3'
GX1838_RAIL_A = 1 # Variable c_int '1'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x000000004'
GX1838_SOURCE_PROGRAMMABLE_LOAD = 3 # Variable c_int '3'
GT_WRONG_BOARD = -3 # Variable c_int '-0x000000003'
GT_SYNC_CREATE = -37 # Variable c_int '-0x000000025'
GXPDO_CAL_BY_USER_ERROR_CHANGE_CAL_SOURCE = -83 # Variable c_int '-0x000000053'
GX1838_SOURCE_FIXED_LOAD = 4 # Variable c_int '4'
GT_VISA_LOAD_DLL_ERROR = -30 # Variable c_int '-0x00000001e'
GX3348_RAIL_GROUND = 3 # Variable c_int '3'
GX3348_RAIL_SOURCE_INTERNAL_DAC = 0 # Variable c_int '0'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x00000000c'
GXPDO_CAL_BY_USER_INVALID_LOAD_VALUE = -82 # Variable c_int '-0x000000052'
GT_VISA_VIIN_ERROR = -34 # Variable c_int '-0x000000022'
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x00000000a'
GXPDO_PANEL_MODELESS = 0 # Variable c_int '0'
GT_INVALID_SLOT = -22 # Variable c_int '-0x000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x000000009'
GT_SYNC_TIMEOUT = -38 # Variable c_int '-0x000000026'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x000000001'
GXPDO_INVALID_CALIBRATION_DATA_SOURCE = -59 # Variable c_int '-0x00000003b'
GX3348_GROUP_B = 1 # Variable c_int '1'
GX3348_GROUP_C = 2 # Variable c_int '2'
GXPDO_INVALID_GAIN_VAL = -57 # Variable c_int '-0x000000039'
GX1838_CAL_DATA_USER_NONVOLATILE = 2 # Variable c_int '2'
GX1838_RAIL_NONE = 0 # Variable c_int '0'
GX3348_GROUP_A = 0 # Variable c_int '0'
GXPDO_INVALID_DAC = -52 # Variable c_int '-0x000000034'
GX3348_GROUP_D = 3 # Variable c_int '3'
GXPDO_PANEL_MODAL = 1 # Variable c_int '1'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x000000007'
GXPDO_EEPROM_BUSY_TIMEOUT = -60 # Variable c_int '-0x00000003c'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x000000017'
GT_LICENSE = -40 # Variable c_int '-0x000000028'
CHAR = c_char
BYTE = c_ubyte
SHORT = c_short
WORD = c_ushort
INT = c_int
UINT = c_uint
LONG = c_long
LPLONG = POINTER(c_long)
DWORD = c_ulong
PULONG = POINTER(c_ulong)
ULONG = c_ulong
LPDWORD = POINTER(c_ulong)
DOUBLE = c_double
BOOL = c_int
PBOOL = POINTER(BOOL)
PBYTE = POINTER(BYTE)
PSHORT = POINTER(SHORT)
PWORD = POINTER(WORD)
PLONG = POINTER(c_long)
PDWORD = POINTER(c_ulong)
PDOUBLE = POINTER(DOUBLE)
PVOID = c_void_p
PSTR = STRING
HWND = c_void_p
PCSTR = STRING
GxPdoGetErrorString = _libraries['libGxPdo.so'].GxPdoGetErrorString
GxPdoGetErrorString.restype = None
GxPdoGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxPdoGetDriverSummary = _libraries['libGxPdo.so'].GxPdoGetDriverSummary
GxPdoGetDriverSummary.restype = None
GxPdoGetDriverSummary.argtypes = [PSTR, SHORT, POINTER(DWORD), PSHORT]
Gx1838Initialize = _libraries['libGxPdo.so'].Gx1838Initialize
Gx1838Initialize.restype = None
Gx1838Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx1838InitializeVisa = _libraries['libGxPdo.so'].Gx1838InitializeVisa
Gx1838InitializeVisa.restype = None
Gx1838InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx1838Reset = _libraries['libGxPdo.so'].Gx1838Reset
Gx1838Reset.restype = None
Gx1838Reset.argtypes = [SHORT, PSHORT]
Gx1838GetBoardSummary = _libraries['libGxPdo.so'].Gx1838GetBoardSummary
Gx1838GetBoardSummary.restype = None
Gx1838GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx1838GetCalibrationInfo = _libraries['libGxPdo.so'].Gx1838GetCalibrationInfo
Gx1838GetCalibrationInfo.restype = None
Gx1838GetCalibrationInfo.argtypes = [SHORT, PSTR, SHORT, PSHORT, PSHORT]
Gx1838GetChannelRail = _libraries['libGxPdo.so'].Gx1838GetChannelRail
Gx1838GetChannelRail.restype = None
Gx1838GetChannelRail.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx1838GetDacOutputRange = _libraries['libGxPdo.so'].Gx1838GetDacOutputRange
Gx1838GetDacOutputRange.restype = None
Gx1838GetDacOutputRange.argtypes = [SHORT, SHORT, PDOUBLE, PDOUBLE, PSHORT]
Gx1838GetDacVoltage = _libraries['libGxPdo.so'].Gx1838GetDacVoltage
Gx1838GetDacVoltage.restype = None
Gx1838GetDacVoltage.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx1838GetRailSource = _libraries['libGxPdo.so'].Gx1838GetRailSource
Gx1838GetRailSource.restype = None
Gx1838GetRailSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx1838SetChannelRail = _libraries['libGxPdo.so'].Gx1838SetChannelRail
Gx1838SetChannelRail.restype = None
Gx1838SetChannelRail.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx1838SetDacVoltage = _libraries['libGxPdo.so'].Gx1838SetDacVoltage
Gx1838SetDacVoltage.restype = None
Gx1838SetDacVoltage.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
Gx1838SetRailSource = _libraries['libGxPdo.so'].Gx1838SetRailSource
Gx1838SetRailSource.restype = None
Gx1838SetRailSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx1838GetDacCalibrationDataSource = _libraries['libGxPdo.so'].Gx1838GetDacCalibrationDataSource
Gx1838GetDacCalibrationDataSource.restype = None
Gx1838GetDacCalibrationDataSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx1838GetDacCalibrationDataSources = _libraries['libGxPdo.so'].Gx1838GetDacCalibrationDataSources
Gx1838GetDacCalibrationDataSources.restype = None
Gx1838GetDacCalibrationDataSources.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx1838GetDacCalibrationDataString = _libraries['libGxPdo.so'].Gx1838GetDacCalibrationDataString
Gx1838GetDacCalibrationDataString.restype = None
Gx1838GetDacCalibrationDataString.argtypes = [SHORT, SHORT, SHORT, PSTR, SHORT, PSHORT]
Gx1838SetDacCalibrationDataSource = _libraries['libGxPdo.so'].Gx1838SetDacCalibrationDataSource
Gx1838SetDacCalibrationDataSource.restype = None
Gx1838SetDacCalibrationDataSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx1838CalByUserDeleteClibration = _libraries['libGxPdo.so'].Gx1838CalByUserDeleteClibration
Gx1838CalByUserDeleteClibration.restype = None
Gx1838CalByUserDeleteClibration.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx1838CalByUserReadMeasuredVoltage = _libraries['libGxPdo.so'].Gx1838CalByUserReadMeasuredVoltage
Gx1838CalByUserReadMeasuredVoltage.restype = None
Gx1838CalByUserReadMeasuredVoltage.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx1838CalByUserSetupDacForMeasurement = _libraries['libGxPdo.so'].Gx1838CalByUserSetupDacForMeasurement
Gx1838CalByUserSetupDacForMeasurement.restype = None
Gx1838CalByUserSetupDacForMeasurement.argtypes = [SHORT, SHORT, PSHORT]
Gx1838CalByUserSetup = _libraries['libGxPdo.so'].Gx1838CalByUserSetup
Gx1838CalByUserSetup.restype = None
Gx1838CalByUserSetup.argtypes = [SHORT, SHORT, SHORT, SHORT, DOUBLE, PSHORT]
Gx1838CalByUserStoreDacCalibrationData = _libraries['libGxPdo.so'].Gx1838CalByUserStoreDacCalibrationData
Gx1838CalByUserStoreDacCalibrationData.restype = None
Gx1838CalByUserStoreDacCalibrationData.argtypes = [SHORT, PSHORT]
Gx1838CalByUserWriteMeasuredVoltage = _libraries['libGxPdo.so'].Gx1838CalByUserWriteMeasuredVoltage
Gx1838CalByUserWriteMeasuredVoltage.restype = None
Gx1838CalByUserWriteMeasuredVoltage.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
Gx3348Initialize = _libraries['libGxPdo.so'].Gx3348Initialize
Gx3348Initialize.restype = None
Gx3348Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx3348InitializeVisa = _libraries['libGxPdo.so'].Gx3348InitializeVisa
Gx3348InitializeVisa.restype = None
Gx3348InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx3348Reset = _libraries['libGxPdo.so'].Gx3348Reset
Gx3348Reset.restype = None
Gx3348Reset.argtypes = [SHORT, PSHORT]
Gx3348GetBoardSummary = _libraries['libGxPdo.so'].Gx3348GetBoardSummary
Gx3348GetBoardSummary.restype = None
Gx3348GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx3348GetCalibrationInfo = _libraries['libGxPdo.so'].Gx3348GetCalibrationInfo
Gx3348GetCalibrationInfo.restype = None
Gx3348GetCalibrationInfo.argtypes = [SHORT, PSTR, SHORT, PSHORT, PSHORT]
Gx3348SetDac = _libraries['libGxPdo.so'].Gx3348SetDac
Gx3348SetDac.restype = None
Gx3348SetDac.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
Gx3348GetDac = _libraries['libGxPdo.so'].Gx3348GetDac
Gx3348GetDac.restype = None
Gx3348GetDac.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx3348SetRailSource = _libraries['libGxPdo.so'].Gx3348SetRailSource
Gx3348SetRailSource.restype = None
Gx3348SetRailSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx3348GetRailSource = _libraries['libGxPdo.so'].Gx3348GetRailSource
Gx3348GetRailSource.restype = None
Gx3348GetRailSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx3348SetChannelRail = _libraries['libGxPdo.so'].Gx3348SetChannelRail
Gx3348SetChannelRail.restype = None
Gx3348SetChannelRail.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx3348GetChannelRail = _libraries['libGxPdo.so'].Gx3348GetChannelRail
Gx3348GetChannelRail.restype = None
Gx3348GetChannelRail.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx3348Measure = _libraries['libGxPdo.so'].Gx3348Measure
Gx3348Measure.restype = None
Gx3348Measure.argtypes = [SHORT, SHORT, SHORT, PDOUBLE, PSHORT]
Gx3348SetDacVoltage = _libraries['libGxPdo.so'].Gx3348SetDacVoltage
Gx3348SetDacVoltage.restype = None
Gx3348SetDacVoltage.argtypes = [SHORT, SHORT, DOUBLE, BOOL, PSHORT]
Gx3348GetDacVoltage = _libraries['libGxPdo.so'].Gx3348GetDacVoltage
Gx3348GetDacVoltage.restype = None
Gx3348GetDacVoltage.argtypes = [SHORT, SHORT, PDOUBLE, PBOOL, PSHORT]
Gx3348SetRelay = _libraries['libGxPdo.so'].Gx3348SetRelay
Gx3348SetRelay.restype = None
Gx3348SetRelay.argtypes = [SHORT, SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx3348GetRelay = _libraries['libGxPdo.so'].Gx3348GetRelay
Gx3348GetRelay.restype = None
Gx3348GetRelay.argtypes = [SHORT, SHORT, SHORT, SHORT, PBOOL, PSHORT]
Gx3348SetDigitalOutputs = _libraries['libGxPdo.so'].Gx3348SetDigitalOutputs
Gx3348SetDigitalOutputs.restype = None
Gx3348SetDigitalOutputs.argtypes = [SHORT, DWORD, DWORD, PSHORT]
Gx3348GetDigitalOutputs = _libraries['libGxPdo.so'].Gx3348GetDigitalOutputs
Gx3348GetDigitalOutputs.restype = None
Gx3348GetDigitalOutputs.argtypes = [SHORT, POINTER(DWORD), POINTER(DWORD), PSHORT]
Gx3348GetDigitalInputs = _libraries['libGxPdo.so'].Gx3348GetDigitalInputs
Gx3348GetDigitalInputs.restype = None
Gx3348GetDigitalInputs.argtypes = [SHORT, POINTER(DWORD), PSHORT]
Gx3348CalSetMode = _libraries['libGxPdo.so'].Gx3348CalSetMode
Gx3348CalSetMode.restype = None
Gx3348CalSetMode.argtypes = [SHORT, SHORT, PSHORT]
Gx3348CalSetDacVoltagePoint = _libraries['libGxPdo.so'].Gx3348CalSetDacVoltagePoint
Gx3348CalSetDacVoltagePoint.restype = None
Gx3348CalSetDacVoltagePoint.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx3348CalAdc = _libraries['libGxPdo.so'].Gx3348CalAdc
Gx3348CalAdc.restype = None
Gx3348CalAdc.argtypes = [SHORT, SHORT, SHORT, DOUBLE, DOUBLE, DOUBLE, DOUBLE, PSHORT]
Gx3348CalDac = _libraries['libGxPdo.so'].Gx3348CalDac
Gx3348CalDac.restype = None
Gx3348CalDac.argtypes = [SHORT, SHORT, DOUBLE, DOUBLE, DOUBLE, PSHORT]
Gx3348CalWriteEEPROM = _libraries['libGxPdo.so'].Gx3348CalWriteEEPROM
Gx3348CalWriteEEPROM.restype = None
Gx3348CalWriteEEPROM.argtypes = [SHORT, PSHORT]
Gx3348SelfTest = _libraries['libGxPdo.so'].Gx3348SelfTest
Gx3348SelfTest.restype = None
Gx3348SelfTest.argtypes = [SHORT, PBOOL, PSTR, PSHORT]
__all__ = ['GX3348_RAIL_SOURCE_EXTERNAL_AMPLIFIED', 'PDWORD',
           'GT_NO_ERROR', 'GxPdoGetErrorString',
           'Gx1838SetDacCalibrationDataSource',
           'GT_UNABLE_REGISTER_DEVICE', 'GXPDO_UNABLE_TO_SET_DAC',
           'GX3348_CAL_MODE_DISABLED', 'BYTE',
           'Gx1838CalByUserWriteMeasuredVoltage', 'GT_INVALID_STRLEN',
           'Gx3348GetDigitalOutputs', 'GX3348_RAIL_GND',
           'GT_LVRT_UNSUPPORTED', 'LONG', 'GX3348_RAIL_NONE',
           'GX3348_CAL_MODE_ENABLED', 'GX3348_RAIL_B',
           'GX3348_RAIL_C', 'GX3348_RAIL_A', 'GT_UNABLE_CREATE_PANEL',
           'GX3348_RAIL_DAC_C', 'GX3348_RAIL_DAC_B',
           'GX3348_RAIL_DAC_A', 'Gx3348SetDigitalOutputs',
           'Gx1838Reset', 'GT_BOARD_NOT_EXIST',
           'Gx1838SetChannelRail',
           'Gx1838GetDacCalibrationDataSource', 'GXPDO_INVALID_GROUP',
           'GX1838_SOURCE_EXTERNAL', 'GX1838_DAC_MAX_VOLTAGE',
           'Gx1838GetRailSource', 'BOOL', 'GXPDO_INVALID_OFFSET_VAL',
           'PSTR', 'Gx3348CalWriteEEPROM', 'GX1838_DAC_C',
           'GX1838_DAC_B', 'GX1838_DAC_A', 'GX1838_CAL_LOW_VOLTAGE',
           'Gx1838GetCalibrationInfo', 'Gx1838SetDacVoltage',
           'DOUBLE', 'Gx3348InitializeVisa', 'Gx3348GetRelay',
           'PLONG', 'Gx3348CalSetDacVoltagePoint', 'SHORT',
           'GT_NOT_IN_CALIBRATION_MODE', 'Gx3348GetCalibrationInfo',
           'GX1838_CAL_MIN_LOAD_VALUE', 'Gx3348SetDac',
           'GXPDO_INVALID_RAIL_SOURCE', 'GX3348_DAC_RAIL_A',
           'GX3348_DAC_RAIL_C', 'GX3348_DAC_RAIL_B', 'Gx3348CalAdc',
           'Gx1838Initialize', 'ULONG', 'GX1838_CAL_HIGH_VOLTAGE',
           'GX3348_CAL_DAC_VOLTAGE_POINT_NEGATIVE',
           'Gx1838CalByUserDeleteClibration',
           'Gx1838CalByUserSetupDacForMeasurement',
           'Gx3348GetDacVoltage', 'GXPDO_INVALID_DAC_VOLTAGE',
           'GT_INVALID_PARAMETER', 'GXPDO_CAL_BY_USER_ERR_SEQUENCE',
           'GX1838_SOURCE_INTERNAL', 'PBOOL',
           'GXPDO_CAL_BY_USER_INVALID_CALIBRATION_DATA',
           'Gx1838GetDacVoltage', 'GT_VISA_GETATTRIBUTE_ERROR',
           'PDOUBLE', 'WORD', 'GXPDO_INVALID_RAIL',
           'GX3348_CAL_DAC_VOLTAGE_POINT_POSITIVE', 'INT',
           'GX3348_RAIL_SOURCE_INTERNAL_5V', 'GT_VISA_OPEN_ERROR',
           'HWND', 'GT_VISA_OPENDEFAULTRM_ERROR', 'PULONG',
           'Gx1838CalByUserSetup', 'GXPDO_INVALID_CHANNEL',
           'GT_INVALID_MODE', 'PCSTR', 'GT_VISA_MEMMAP_ERROR', 'CHAR',
           'Gx1838CalByUserStoreDacCalibrationData',
           'GX3348_CAL_DAC_VOLTAGE_POINT_ZERO', 'GX1838_SOURCE_OPEN',
           'Gx3348Reset', 'Gx3348CalSetMode', 'GxPdoGetDriverSummary',
           'Gx3348SetDacVoltage', 'GX1838_CAL_DATA_FACTORY',
           'GXPDO_ADC_MEASURE_TIMEOUT',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GX1838_CAL_DATA_USER_VOLATILE',
           'GXPDO_INVALID_CHANNEL_RAIL',
           'GX3348_RAIL_SOURCE_EXTERNAL', 'Gx1838GetBoardSummary',
           'Gx1838CalByUserReadMeasuredVoltage', 'Gx3348CalDac',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GT_INVALID_ERROR',
           'GX1838_DAC_MIN_VOLTAGE', 'GX1838_RAIL_B', 'GX1838_RAIL_C',
           'Gx1838GetChannelRail', 'GX1838_RAIL_A',
           'GT_SLOT_NOT_CONFIG', 'Gx3348SetRailSource',
           'GX1838_SOURCE_PROGRAMMABLE_LOAD', 'GT_WRONG_BOARD',
           'GT_SYNC_CREATE',
           'GXPDO_CAL_BY_USER_ERROR_CHANGE_CAL_SOURCE',
           'Gx3348GetBoardSummary', 'GX1838_SOURCE_FIXED_LOAD',
           'Gx3348GetRailSource', 'GT_VISA_LOAD_DLL_ERROR',
           'GX3348_RAIL_GROUND', 'LPDWORD', 'Gx3348SelfTest',
           'GX3348_RAIL_SOURCE_INTERNAL_DAC', 'Gx3348SetRelay',
           'GT_NOT_CALIBRATED', 'Gx1838SetRailSource', 'Gx3348GetDac',
           'GXPDO_CAL_BY_USER_INVALID_LOAD_VALUE',
           'GT_VISA_VIIN_ERROR', 'GT_BOARD_INVALID_EEPROM',
           'GXPDO_PANEL_MODELESS',
           'Gx1838GetDacCalibrationDataString', 'LPLONG',
           'GT_INVALID_SLOT', 'GT_UNABLE_TO_GETTIMER',
           'GT_SYNC_TIMEOUT', 'GT_CANT_OPEN_HW', 'DWORD',
           'Gx1838GetDacCalibrationDataSources',
           'GXPDO_INVALID_CALIBRATION_DATA_SOURCE', 'GX3348_GROUP_B',
           'GX3348_GROUP_C', 'GXPDO_INVALID_GAIN_VAL',
           'Gx1838GetDacOutputRange', 'Gx3348GetDigitalInputs',
           'GX1838_CAL_DATA_USER_NONVOLATILE', 'Gx1838InitializeVisa',
           'Gx3348SetChannelRail', 'GX1838_RAIL_NONE',
           'Gx3348Measure', 'Gx3348Initialize', 'GX3348_GROUP_A',
           'PSHORT', 'UINT', 'GXPDO_INVALID_DAC', 'GX3348_GROUP_D',
           'Gx3348GetChannelRail', 'GXPDO_PANEL_MODAL', 'PVOID',
           'GT_UNABLE_ALLOC_MEMORY', 'PBYTE',
           'GXPDO_EEPROM_BUSY_TIMEOUT', 'PWORD', 'GT_INVALID_HANDLE',
           'GT_LICENSE']
