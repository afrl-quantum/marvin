from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxPs.so'] = CDLL('libGxPs.so')


GXPS_USER_CAL_STEP6 = 6
GXPS_USER_CAL_STEP9 = 9
GXPS_USER_CAL_STEP8 = 8
GXPS_USER_CAL_STEP7 = 7
GXPS_USER_CAL_STEP2 = 2
GXPS_USER_CAL_STEP1 = 1
# VOID = void # alias
GXPS_USER_CAL_STEP5 = 5
GXPS_USER_CAL_STEP4 = 4
GXPS_USER_CAL_STEP3 = 3
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x00000000a'
GXPS_INVALID_VOLTAGE_SETTING_MODE = -85 # Variable c_int '-0x000000055'
GXPS_OUPUT_STANDBY = 1 # Variable c_int '1'
GT_SYNC_TIMEOUT = -38 # Variable c_int '-0x000000026'
GT_INVALID_MODE = -25 # Variable c_int '-0x000000019'
GT_FIRMWARE_UPGRADE_MODE_SYNC = 0 # Variable c_int '0'
GXPS_INVALID_DAC_VOLTAGE = -81 # Variable c_int '-0x000000051'
GXPS_INVALID_ERROR = -99 # Variable c_int '-0x000000063'
GXPS_TYPE_PMC28 = 7 # Variable c_int '7'
GT_VISA_MEMMAP_ERROR = -35 # Variable c_int '-0x000000023'
GXPS_CAL_BY_USER_INVALID_STEP = -74 # Variable c_int '-0x00000004a'
GXPS_AC_POWER_OFF = 2 # Variable c_int '2'
GXPS_ERR_TIMEOUT_ADC_READ = -61 # Variable c_int '-0x00000003d'
GT_INVALID_SLOT = -22 # Variable c_int '-0x000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x000000009'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x00000000b'
GT_PARAMETER_OUT_OF_RANGE = -26 # Variable c_int '-0x00000001a'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x000000001'
GXPS_USERCAL_INVALID_VALUE = -73 # Variable c_int '-0x000000049'
GXPS_ERR_TIMEOUT_SET_DAC_VOLTAGE = -62 # Variable c_int '-0x00000003e'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x000000018'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x000000006'
GXPS_AC_OFF = 0 # Variable c_int '0'
GXPS_TYPE_PMP15 = 8 # Variable c_int '8'
GT_LVRT_UNSUPPORTED = -39 # Variable c_int '-0x000000027'
GXPS_INVALID_CHANNEL = -80 # Variable c_int '-0x000000050'
GXPS_SET_VOLTAGE_TIMEOUT = -60 # Variable c_int '-0x00000003c'
GXPS_EEPROM_GAIN_ERROR = -54 # Variable c_int '-0x000000036'
GXPS_TIMEOUT = -83 # Variable c_int '-0x000000053'
GXPS_TYPE_PMP30 = 1 # Variable c_int '1'
GXPS_TYPE_PMC3 = 3 # Variable c_int '3'
GT_VISA_GETATTRIBUTE_ERROR = -33 # Variable c_int '-0x000000021'
GXPS_PS_NOT_FOUND = -51 # Variable c_int '-0x000000033'
GXPS_CHANNEL_NOT_INSTALLED = -84 # Variable c_int '-0x000000054'
GXPS_TYPE_PMC5 = 4 # Variable c_int '4'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x00000000d'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x000000008'
GXPS_EEPROM_OFFSET_ERROR = -53 # Variable c_int '-0x000000035'
GT_NO_ERROR = 0 # Variable c_int '0'
GXPS_OUPUT_ON = 0 # Variable c_int '0'
GXPS_CHANNEL_NOT_SET_ON = -59 # Variable c_int '-0x00000003b'
GXPS_MODE_ERROR = -50 # Variable c_int '-0x000000032'
GXPS_INVALID_DAC_AMPERAGE = -82 # Variable c_int '-0x000000052'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x000000002'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x00000000c'
GXPS_ERR_TIMEOUT_SET_DAC_CURRENT = -63 # Variable c_int '-0x00000003f'
GXPS_TYPE_PMC12 = 5 # Variable c_int '5'
GXPS_CAL_LOW_VOLTAGE = 0 # Variable c_int '0'
GXPS_TYPE_PMC15 = 6 # Variable c_int '6'
GXPS_SET_STANDBY_FAIL = -57 # Variable c_int '-0x000000039'
GT_WRONG_BOARD = -3 # Variable c_int '-0x000000003'
GXPS_PANEL_MODAL = 1 # Variable c_int '1'
GXPS_USERCAL_SEQUENCE = -71 # Variable c_int '-0x000000047'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x000000004'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x000000015'
GT_VISA_VIIN_ERROR = -34 # Variable c_int '-0x000000022'
GT_SYNC_CREATE = -37 # Variable c_int '-0x000000025'
GXPS_SET_ON_FAIL = -56 # Variable c_int '-0x000000038'
GT_INVALID_ERROR = -20 # Variable c_int '-0x000000014'
GXPS_DAC_SOURCE_ERROR = -52 # Variable c_int '-0x000000034'
GXPS_CAL_HIGH_VOLTAGE = 1 # Variable c_int '1'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x000000005'
GXPS_TYPE_PMP60 = 2 # Variable c_int '2'
GXPS_CHANNEL_INHIBIT = 1 # Variable c_int '1'
GT_FIRMWARE_UPGRADE_MODE_ASYNC = 1 # Variable c_int '1'
GXPS_CAL_MIN_LOAD_VALUE = 64 # Variable c_int '64'
GXPS_CHANNEL2 = 2 # Variable c_int '2'
GT_VISA_LOAD_DLL_ERROR = -30 # Variable c_int '-0x00000001e'
GXPS_USERCAL_INVALID_FIXED_MODULE = -72 # Variable c_int '-0x000000048'
GXPS_EEPROM_NOT_CALIBRATED = -55 # Variable c_int '-0x000000037'
GT_VISA_OPEN_ERROR = -32 # Variable c_int '-0x000000020'
GXPS_PANEL_MODELESS = 0 # Variable c_int '0'
GT_VISA_OPENDEFAULTRM_ERROR = -31 # Variable c_int '-0x00000001f'
GXPS_CAL_NOT_STARTED = -75 # Variable c_int '-0x00000004b'
GXPS_AC_ON = 1 # Variable c_int '1'
GXPS_USERCAL_INVALID_LOAD_VALUE = -70 # Variable c_int '-0x000000046'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x000000007'
GXPS_TYPE_NONE = 0 # Variable c_int '0'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x000000017'
GXPS_CHANNEL_FAIL = -58 # Variable c_int '-0x00000003a'
GXPS_CHANNEL1 = 1 # Variable c_int '1'
GT_LICENSE = -40 # Variable c_int '-0x000000028'
CHAR = c_char
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
HWND = c_void_p
PCSTR = STRING
GxPsInitialize = _libraries['libGxPs.so'].GxPsInitialize
GxPsInitialize.restype = None
GxPsInitialize.argtypes = [SHORT, PSHORT, PSHORT]
GxPsInitializeVisa = _libraries['libGxPs.so'].GxPsInitializeVisa
GxPsInitializeVisa.restype = None
GxPsInitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
GxPsReset = _libraries['libGxPs.so'].GxPsReset
GxPsReset.restype = None
GxPsReset.argtypes = [SHORT, PSHORT]
GxPsPanel = _libraries['libGxPs.so'].GxPsPanel
GxPsPanel.restype = None
GxPsPanel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
GxPsGetErrorString = _libraries['libGxPs.so'].GxPsGetErrorString
GxPsGetErrorString.restype = None
GxPsGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxPsGetDriverSummary = _libraries['libGxPs.so'].GxPsGetDriverSummary
GxPsGetDriverSummary.restype = None
GxPsGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
GxPsGetBoardSummary = _libraries['libGxPs.so'].GxPsGetBoardSummary
GxPsGetBoardSummary.restype = None
GxPsGetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxPsGetExtendedSerialNumber = _libraries['libGxPs.so'].GxPsGetExtendedSerialNumber
GxPsGetExtendedSerialNumber.restype = None
GxPsGetExtendedSerialNumber.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxPsGetCalibrationInfo = _libraries['libGxPs.so'].GxPsGetCalibrationInfo
GxPsGetCalibrationInfo.restype = None
GxPsGetCalibrationInfo.argtypes = [SHORT, PSTR, SHORT, PSHORT, PSHORT]
GxPsSetCurrentLimit = _libraries['libGxPs.so'].GxPsSetCurrentLimit
GxPsSetCurrentLimit.restype = None
GxPsSetCurrentLimit.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
GxPsSetVoltage = _libraries['libGxPs.so'].GxPsSetVoltage
GxPsSetVoltage.restype = None
GxPsSetVoltage.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
GxPsSetVoltageAndWaitUntilReady = _libraries['libGxPs.so'].GxPsSetVoltageAndWaitUntilReady
GxPsSetVoltageAndWaitUntilReady.restype = None
GxPsSetVoltageAndWaitUntilReady.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
GxPsSetStandby = _libraries['libGxPs.so'].GxPsSetStandby
GxPsSetStandby.restype = None
GxPsSetStandby.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxPsSetStandbyImmediate = _libraries['libGxPs.so'].GxPsSetStandbyImmediate
GxPsSetStandbyImmediate.restype = None
GxPsSetStandbyImmediate.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxPsGetAcPowerState = _libraries['libGxPs.so'].GxPsGetAcPowerState
GxPsGetAcPowerState.restype = None
GxPsGetAcPowerState.argtypes = [SHORT, PSHORT, PSHORT]
GxPsGetCalibrationDate = _libraries['libGxPs.so'].GxPsGetCalibrationDate
GxPsGetCalibrationDate.restype = None
GxPsGetCalibrationDate.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxPsGetChannelCalibrationDate = _libraries['libGxPs.so'].GxPsGetChannelCalibrationDate
GxPsGetChannelCalibrationDate.restype = None
GxPsGetChannelCalibrationDate.argtypes = [SHORT, SHORT, PSTR, SHORT, PSHORT]
GxPsGetCurrent = _libraries['libGxPs.so'].GxPsGetCurrent
GxPsGetCurrent.restype = None
GxPsGetCurrent.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
GxPsGetCurrentLimit = _libraries['libGxPs.so'].GxPsGetCurrentLimit
GxPsGetCurrentLimit.restype = None
GxPsGetCurrentLimit.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
GxPsGetStandby = _libraries['libGxPs.so'].GxPsGetStandby
GxPsGetStandby.restype = None
GxPsGetStandby.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxPsGetState = _libraries['libGxPs.so'].GxPsGetState
GxPsGetState.restype = None
GxPsGetState.argtypes = [SHORT, SHORT, PSHORT]
GxPsGetType = _libraries['libGxPs.so'].GxPsGetType
GxPsGetType.restype = None
GxPsGetType.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
GxPsGetVoltage = _libraries['libGxPs.so'].GxPsGetVoltage
GxPsGetVoltage.restype = None
GxPsGetVoltage.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
GxPsRecallSettings = _libraries['libGxPs.so'].GxPsRecallSettings
GxPsRecallSettings.restype = None
GxPsRecallSettings.argtypes = [SHORT, SHORT, PSHORT]
GxPsStoreSettings = _libraries['libGxPs.so'].GxPsStoreSettings
GxPsStoreSettings.restype = None
GxPsStoreSettings.argtypes = [SHORT, SHORT, PSHORT]
GxPsUpgradeFirmware = _libraries['libGxPs.so'].GxPsUpgradeFirmware
GxPsUpgradeFirmware.restype = None
GxPsUpgradeFirmware.argtypes = [SHORT, PCSTR, SHORT, PSHORT]
GxPsUpgradeFirmwareStatus = _libraries['libGxPs.so'].GxPsUpgradeFirmwareStatus
GxPsUpgradeFirmwareStatus.restype = None
GxPsUpgradeFirmwareStatus.argtypes = [SHORT, PSTR, SHORT, PSHORT, PBOOL, PSHORT]

# values for unnamed enumeration
GxPsUserCalSetup = _libraries['libGxPs.so'].GxPsUserCalSetup
GxPsUserCalSetup.restype = None
GxPsUserCalSetup.argtypes = [SHORT, SHORT, DOUBLE, SHORT, PSHORT]
GxPsUserCalSetupForMeasurement = _libraries['libGxPs.so'].GxPsUserCalSetupForMeasurement
GxPsUserCalSetupForMeasurement.restype = None
GxPsUserCalSetupForMeasurement.argtypes = [SHORT, SHORT, PSHORT]
GxPsUserCalWriteMeasuredVal = _libraries['libGxPs.so'].GxPsUserCalWriteMeasuredVal
GxPsUserCalWriteMeasuredVal.restype = None
GxPsUserCalWriteMeasuredVal.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
GxPsUserCalReadMeasuredVal = _libraries['libGxPs.so'].GxPsUserCalReadMeasuredVal
GxPsUserCalReadMeasuredVal.restype = None
GxPsUserCalReadMeasuredVal.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
GxPsUserCalStoreCalibrationData = _libraries['libGxPs.so'].GxPsUserCalStoreCalibrationData
GxPsUserCalStoreCalibrationData.restype = None
GxPsUserCalStoreCalibrationData.argtypes = [SHORT, PSHORT]
GxPsUserCalRestoreFactoryCalibration = _libraries['libGxPs.so'].GxPsUserCalRestoreFactoryCalibration
GxPsUserCalRestoreFactoryCalibration.restype = None
GxPsUserCalRestoreFactoryCalibration.argtypes = [SHORT, SHORT, PSHORT]
__all__ = ['GxPsUserCalReadMeasuredVal', 'GxPsGetType',
           'GXPS_OUPUT_STANDBY', 'GxPsUpgradeFirmwareStatus',
           'GT_FIRMWARE_UPGRADE_MODE_SYNC', 'PDWORD', 'GT_NO_ERROR',
           'GXPS_AC_POWER_OFF', 'GT_UNABLE_REGISTER_DEVICE',
           'GXPS_USERCAL_INVALID_VALUE', 'GXPS_TYPE_PMP30',
           'GxPsReset', 'GxPsSetStandbyImmediate',
           'GT_INVALID_STRLEN', 'GT_LVRT_UNSUPPORTED',
           'GXPS_CHANNEL_FAIL', 'GXPS_INVALID_CHANNEL',
           'GxPsGetAcPowerState', 'LONG',
           'GxPsUserCalRestoreFactoryCalibration',
           'GT_UNABLE_CREATE_PANEL', 'GXPS_EEPROM_OFFSET_ERROR',
           'GXPS_CHANNEL_NOT_SET_ON', 'GXPS_CAL_HIGH_VOLTAGE',
           'GXPS_SET_STANDBY_FAIL', 'GxPsGetDriverSummary',
           'GxPsSetVoltage', 'PSTR', 'GxPsGetBoardSummary',
           'GT_FIRMWARE_UPGRADE_MODE_ASYNC',
           'GXPS_CAL_MIN_LOAD_VALUE', 'DOUBLE',
           'GXPS_USERCAL_INVALID_FIXED_MODULE',
           'GXPS_EEPROM_NOT_CALIBRATED', 'GXPS_PANEL_MODELESS',
           'GXPS_TIMEOUT', 'HWND', 'GXPS_TYPE_NONE',
           'GxPsUserCalWriteMeasuredVal', 'PLONG', 'SHORT',
           'GxPsGetExtendedSerialNumber', 'GxPsInitializeVisa',
           'GXPS_CAL_BY_USER_INVALID_STEP', 'GXPS_OUPUT_ON',
           'GxPsGetErrorString', 'GXPS_PANEL_MODAL',
           'GXPS_EEPROM_GAIN_ERROR',
           'GXPS_ERR_TIMEOUT_SET_DAC_VOLTAGE',
           'GXPS_CHANNEL_NOT_INSTALLED', 'GT_INVALID_PARAMETER',
           'GxPsGetState', 'GXPS_INVALID_DAC_AMPERAGE', 'PBOOL',
           'GXPS_ERR_TIMEOUT_SET_DAC_CURRENT', 'GXPS_TYPE_PMC12',
           'GXPS_CAL_LOW_VOLTAGE', 'GXPS_TYPE_PMC15',
           'GxPsRecallSettings', 'GT_VISA_GETATTRIBUTE_ERROR',
           'PDOUBLE', 'WORD', 'GXPS_SET_ON_FAIL', 'PSHORT',
           'GxPsUserCalStoreCalibrationData', 'GXPS_CHANNEL_INHIBIT',
           'INT', 'GXPS_CHANNEL2', 'GXPS_CHANNEL1',
           'GT_VISA_OPEN_ERROR', 'GT_VISA_OPENDEFAULTRM_ERROR',
           'GxPsGetStandby', 'GxPsStoreSettings',
           'GxPsGetChannelCalibrationDate', 'GT_INVALID_MODE',
           'PCSTR', 'GXPS_INVALID_ERROR', 'GXPS_TYPE_PMC28',
           'GT_VISA_MEMMAP_ERROR', 'CHAR',
           'GXPS_ERR_TIMEOUT_ADC_READ', 'GxPsGetCurrentLimit',
           'GT_NOT_IN_CALIBRATION_MODE', 'GxPsUpgradeFirmware',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GXPS_INVALID_VOLTAGE_SETTING_MODE', 'GxPsSetStandby',
           'GXPS_INVALID_DAC_VOLTAGE', 'GXPS_TYPE_PMC3',
           'GXPS_PS_NOT_FOUND', 'GXPS_TYPE_PMC5',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GT_INVALID_ERROR',
           'GT_SLOT_NOT_CONFIG', 'GT_WRONG_BOARD',
           'GXPS_CAL_NOT_STARTED', 'GXPS_USERCAL_SEQUENCE',
           'GT_SYNC_CREATE', 'GXPS_DAC_SOURCE_ERROR',
           'GxPsUserCalSetup', 'GxPsGetCalibrationDate',
           'GXPS_TYPE_PMP60', 'GxPsGetCalibrationInfo', 'GxPsPanel',
           'GT_VISA_LOAD_DLL_ERROR', 'BOOL', 'GT_NOT_CALIBRATED',
           'GxPsUserCalSetupForMeasurement', 'GXPS_MODE_ERROR',
           'GT_VISA_VIIN_ERROR', 'GT_BOARD_INVALID_EEPROM',
           'GxPsInitialize', 'GxPsSetVoltageAndWaitUntilReady',
           'GT_INVALID_SLOT', 'GT_UNABLE_TO_GETTIMER',
           'GT_SYNC_TIMEOUT', 'GT_PARAMETER_OUT_OF_RANGE',
           'GT_CANT_OPEN_HW', 'GT_BOARD_NOT_EXIST', 'GxPsGetVoltage',
           'GXPS_USER_CAL_STEP9', 'GXPS_USER_CAL_STEP8',
           'GXPS_TYPE_PMP15', 'GXPS_USER_CAL_STEP5',
           'GXPS_USER_CAL_STEP4', 'GXPS_USER_CAL_STEP7',
           'GXPS_USER_CAL_STEP6', 'GXPS_USER_CAL_STEP1',
           'GXPS_USER_CAL_STEP3', 'GXPS_USER_CAL_STEP2',
           'GXPS_SET_VOLTAGE_TIMEOUT', 'PWORD', 'DWORD',
           'GxPsGetCurrent', 'UINT', 'GxPsSetCurrentLimit', 'PVOID',
           'GXPS_AC_OFF', 'GT_UNABLE_ALLOC_MEMORY', 'GXPS_AC_ON',
           'GXPS_USERCAL_INVALID_LOAD_VALUE', 'GT_INVALID_HANDLE',
           'GT_LICENSE']
