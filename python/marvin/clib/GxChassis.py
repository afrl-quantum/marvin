from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxChassis.so'] = CDLL('libGxChassis.so')


# VOID = void # alias
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x00000000a'
GXCHASSIS_FAN_MAX_THRESHOLD_TEMP_F = 140 # Variable c_int '140'
GXCHASSIS_TEMPERATURE_SCALE_METRIC = 0 # Variable c_int '0'
GXCHASSIS_SEGMENT_0_TO_SEGMENT_1 = 0 # Variable c_int '0'
GT_INVALID_MODE = -25 # Variable c_int '-0x000000019'
GXCHASSIS_FAN_MAX_THRESHOLD_TEMP_C = 60 # Variable c_int '60'
GXCHASSIS_INVALID_FAN_POLE = -55 # Variable c_int '-0x000000037'
GT_NO_ERROR = 0 # Variable c_int '0'
GXCHASSIS_PXI_TRIGGER_BUS_LINE_DRIVE_LOW = 1 # Variable c_int '1'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x000000005'
GXCHASSIS_ERR_ALL_BRIDGES = -64 # Variable c_int '-0x000000040'
GT_INVALID_SLOT = -22 # Variable c_int '-0x000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x000000009'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x00000000b'
GT_PARAMETER_OUT_OF_RANGE = -26 # Variable c_int '-0x00000001a'
GXCHASSIS_FAN_SPEED_MODE_AUTO = 0 # Variable c_int '0'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x000000002'
GXCHASSIS_PXI_TRIGGER_BUS_LINE_DISCONNECT = 0 # Variable c_int '0'
GXCHASSIS_UNABLE_TO_DETECT_RIGHT_BRIDGE = -67 # Variable c_int '-0x000000043'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x000000018'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x000000006'
GXCHASSIS_INVALID_TEMPERATURE = -50 # Variable c_int '-0x000000032'
GXCHASSIS_FAN_SPEED_MAX = 2 # Variable c_int '2'
GXCHASSIS_PXI_TRIGGER_BUS_LINE1 = 1 # Variable c_int '1'
GXCHASSIS_PXI_TRIGGER_BUS_LINE0 = 0 # Variable c_int '0'
GXCHASSIS_PXI_TRIGGER_BUS_LINE3 = 3 # Variable c_int '3'
GXCHASSIS_PXI_TRIGGER_BUS_LINE2 = 2 # Variable c_int '2'
GXCHASSIS_INVALID_PXI_TRIGGER_BUS_LINE_DIR = -52 # Variable c_int '-0x000000034'
GXCHASSIS_PXI_TRIGGER_BUS_LINE4 = 4 # Variable c_int '4'
GXCHASSIS_PXI_TRIGGER_BUS_LINE7 = 7 # Variable c_int '7'
GXCHASSIS_PXI_TRIGGER_BUS_LINE6 = 6 # Variable c_int '6'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x00000000d'
GXCHASSIS_PXI_TRIGGER_BUS_LINE5 = 5 # Variable c_int '5'
GT_INVALID_ERROR = -20 # Variable c_int '-0x000000014'
GXCHASSIS_FAN_SPEED_MID = 1 # Variable c_int '1'
GXCHASSIS_FAN_SPEED_MODE_FIXED_VALUE = 1 # Variable c_int '1'
GXCHASSIS_INVALID_PXI_TRIGGER_BUS_LINE = -51 # Variable c_int '-0x000000033'
GXCHASSIS_ERR_CONTROLLER_COM = -61 # Variable c_int '-0x00000003d'
GXCHASSIS_RECALL_USER_SETTINGS = 1 # Variable c_int '1'
GXCHASSIS_FAN_MIN_THRESHOLD_TEMP_F = 32 # Variable c_int '32'
GXCHASSIS_TEMPERATURE_SCALE_ENGLISH = 1 # Variable c_int '1'
GXCHASSIS_INVALID_PXI_TRIGGER_BUS_LINE_MODE = -53 # Variable c_int '-0x000000035'
GXCHASSIS_OVER_TEMPERATURE_ALARM_DISABLE = 0 # Variable c_int '0'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x000000004'
GXCHASSIS_RECALL_FACTORY_SETTINGS = 0 # Variable c_int '0'
GXCHASSIS_FAN_MIN_THRESHOLD_TEMP_C = 0 # Variable c_int '0'
GT_WRONG_BOARD = -3 # Variable c_int '-0x000000003'
GXCHASSIS_UNABLE_TO_DETECT_BRIDGES = -65 # Variable c_int '-0x000000041'
GXCHASSIS_OVER_TEMPERATURE_ALARM_ENABLE = 1 # Variable c_int '1'
GXCHASSIS_UNABLE_TO_DETECT_LEFT_BRIDGE = -66 # Variable c_int '-0x000000042'
GXCHASSIS_PANEL_MODELESS = 0 # Variable c_int '0'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x000000008'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x000000015'
GXCHASSIS_ERR_LEFT_BRIDGE = -62 # Variable c_int '-0x00000003e'
GXCHASSIS_OVER_TEMPERATURE_MODE_MAX_SLOT = 0 # Variable c_int '0'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x000000001'
GXCHASSIS_OVER_TEMPERATURE_MODE_AVERAGE_SLOTS = 1 # Variable c_int '1'
GXCHASSIS_INVALID_SEGMENT = -54 # Variable c_int '-0x000000036'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x000000017'
GXCHASSIS_ERR_CONTROLLER_TIMEOUT = -60 # Variable c_int '-0x00000003c'
GXCHASSIS_PXI_TRIGGER_BUS_LINE_DRIVE_HIGH = 2 # Variable c_int '2'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x000000007'
GXCHASSIS_PXI_TRIGGER_BUS_LINE_MONITOR = 0 # Variable c_int '0'
GXCHASSIS_ERR_RIGHT_BRIDGE = -63 # Variable c_int '-0x00000003f'
GXCHASSIS_INVALID_CHASSIS_TYPE = -56 # Variable c_int '-0x000000038'
GXCHASSIS_OVER_TEMPERATURE_ALARM_ON = 2 # Variable c_int '2'
GXCHASSIS_SEGMENT_1_TO_SEGMENT_2 = 1 # Variable c_int '1'
GXCHASSIS_PANEL_MODAL = 1 # Variable c_int '1'
GXCHASSIS_TEMPERATURE_MIN_THRESHOLD = 20 # Variable c_int '20'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x00000000c'
GXCHASSIS_OVER_TEMPERATURE_ALARM_SNOOZE = 3 # Variable c_int '3'
GXCHASSIS_TEMPERATURE_MAX_THRESHOLD = 75 # Variable c_int '75'
GXCHASSIS_UNSTABLE_ORIENTATION_READING = 10 # Variable c_int '10'
GXCHASSIS_FAN_SPEED_MIN = 0 # Variable c_int '0'
GXCHASSIS_PXI_TRIGGER_BUS_LINE_DIR_LEFT_TO_RIGHT = 1 # Variable c_int '1'
GXCHASSIS_PXI_TRIGGER_BUS_LINE_DIR_RIGHT_TO_LEFT = 2 # Variable c_int '2'
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
GxChassisGetErrorString = _libraries['libGxChassis.so'].GxChassisGetErrorString
GxChassisGetErrorString.restype = None
GxChassisGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxChassisGetDriverSummary = _libraries['libGxChassis.so'].GxChassisGetDriverSummary
GxChassisGetDriverSummary.restype = None
GxChassisGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
GxChassisInitialize = _libraries['libGxChassis.so'].GxChassisInitialize
GxChassisInitialize.restype = None
GxChassisInitialize.argtypes = [SHORT, PSHORT, PSHORT]
GxChassisPanel = _libraries['libGxChassis.so'].GxChassisPanel
GxChassisPanel.restype = None
GxChassisPanel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
GxChassisGetBoardSummary = _libraries['libGxChassis.so'].GxChassisGetBoardSummary
GxChassisGetBoardSummary.restype = None
GxChassisGetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxChassisGetAlarmMode = _libraries['libGxChassis.so'].GxChassisGetAlarmMode
GxChassisGetAlarmMode.restype = None
GxChassisGetAlarmMode.argtypes = [SHORT, PSHORT, PSHORT]
GxChassisGetAlarmTemperature = _libraries['libGxChassis.so'].GxChassisGetAlarmTemperature
GxChassisGetAlarmTemperature.restype = None
GxChassisGetAlarmTemperature.argtypes = [SHORT, PDOUBLE, PSHORT]
GxChassisGetFanSpeed = _libraries['libGxChassis.so'].GxChassisGetFanSpeed
GxChassisGetFanSpeed.restype = None
GxChassisGetFanSpeed.argtypes = [SHORT, PSHORT, PSHORT, PSHORT]
GxChassisGetFanThresholdTemperatures = _libraries['libGxChassis.so'].GxChassisGetFanThresholdTemperatures
GxChassisGetFanThresholdTemperatures.restype = None
GxChassisGetFanThresholdTemperatures.argtypes = [SHORT, PDOUBLE, PDOUBLE, PSHORT]
GxChassisGetOrientation = _libraries['libGxChassis.so'].GxChassisGetOrientation
GxChassisGetOrientation.restype = None
GxChassisGetOrientation.argtypes = [SHORT, SHORT, PSHORT, PSHORT, PSHORT]
GxChassisGetPowerSuppliesVoltages = _libraries['libGxChassis.so'].GxChassisGetPowerSuppliesVoltages
GxChassisGetPowerSuppliesVoltages.restype = None
GxChassisGetPowerSuppliesVoltages.argtypes = [SHORT, PDOUBLE, PSHORT]
GxChassisGetPxiTriggerLine = _libraries['libGxChassis.so'].GxChassisGetPxiTriggerLine
GxChassisGetPxiTriggerLine.restype = None
GxChassisGetPxiTriggerLine.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT, PSHORT, PSHORT]
GxChassisGetPxiTriggerLineLevels = _libraries['libGxChassis.so'].GxChassisGetPxiTriggerLineLevels
GxChassisGetPxiTriggerLineLevels.restype = None
GxChassisGetPxiTriggerLineLevels.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT, PSHORT]
GxChassisGetShutdownTemperature = _libraries['libGxChassis.so'].GxChassisGetShutdownTemperature
GxChassisGetShutdownTemperature.restype = None
GxChassisGetShutdownTemperature.argtypes = [SHORT, PBOOL, PDOUBLE, PSHORT]
GxChassisGetSlotTemperature = _libraries['libGxChassis.so'].GxChassisGetSlotTemperature
GxChassisGetSlotTemperature.restype = None
GxChassisGetSlotTemperature.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
GxChassisGetSlotsTemperatures = _libraries['libGxChassis.so'].GxChassisGetSlotsTemperatures
GxChassisGetSlotsTemperatures.restype = None
GxChassisGetSlotsTemperatures.argtypes = [SHORT, PDOUBLE, PSHORT]
GxChassisGetSlotsTemperaturesStates = _libraries['libGxChassis.so'].GxChassisGetSlotsTemperaturesStates
GxChassisGetSlotsTemperaturesStates.restype = None
GxChassisGetSlotsTemperaturesStates.argtypes = [SHORT, PDWORD, PSHORT]
GxChassisGetSlotsTemperaturesStatistics = _libraries['libGxChassis.so'].GxChassisGetSlotsTemperaturesStatistics
GxChassisGetSlotsTemperaturesStatistics.restype = None
GxChassisGetSlotsTemperaturesStatistics.argtypes = [SHORT, PSHORT, PDOUBLE, PSHORT, PDOUBLE, PDOUBLE, PSHORT]
GxChassisGetTemperatureScale = _libraries['libGxChassis.so'].GxChassisGetTemperatureScale
GxChassisGetTemperatureScale.restype = None
GxChassisGetTemperatureScale.argtypes = [SHORT, PSHORT, PSHORT]
GxChassisGetTemperatureThresholdMode = _libraries['libGxChassis.so'].GxChassisGetTemperatureThresholdMode
GxChassisGetTemperatureThresholdMode.restype = None
GxChassisGetTemperatureThresholdMode.argtypes = [SHORT, PSHORT, PSHORT]
GxChassisRecallSettings = _libraries['libGxChassis.so'].GxChassisRecallSettings
GxChassisRecallSettings.restype = None
GxChassisRecallSettings.argtypes = [SHORT, SHORT, PSHORT]
GxChassisResetPxiTriggerLines = _libraries['libGxChassis.so'].GxChassisResetPxiTriggerLines
GxChassisResetPxiTriggerLines.restype = None
GxChassisResetPxiTriggerLines.argtypes = [SHORT, SHORT, PSHORT]
GxChassisSetAlarmMode = _libraries['libGxChassis.so'].GxChassisSetAlarmMode
GxChassisSetAlarmMode.restype = None
GxChassisSetAlarmMode.argtypes = [SHORT, SHORT, PSHORT]
GxChassisSetAlarmTemperature = _libraries['libGxChassis.so'].GxChassisSetAlarmTemperature
GxChassisSetAlarmTemperature.restype = None
GxChassisSetAlarmTemperature.argtypes = [SHORT, DOUBLE, PSHORT]
GxChassisSetFanSpeed = _libraries['libGxChassis.so'].GxChassisSetFanSpeed
GxChassisSetFanSpeed.restype = None
GxChassisSetFanSpeed.argtypes = [SHORT, SHORT, SHORT, PSHORT]
GxChassisSetFanThresholdTemperatures = _libraries['libGxChassis.so'].GxChassisSetFanThresholdTemperatures
GxChassisSetFanThresholdTemperatures.restype = None
GxChassisSetFanThresholdTemperatures.argtypes = [SHORT, DOUBLE, DOUBLE, PSHORT]
GxChassisSetPxiTriggerLine = _libraries['libGxChassis.so'].GxChassisSetPxiTriggerLine
GxChassisSetPxiTriggerLine.restype = None
GxChassisSetPxiTriggerLine.argtypes = [SHORT, SHORT, SHORT, SHORT, SHORT, SHORT, PSHORT]
GxChassisSetShutdownTemperature = _libraries['libGxChassis.so'].GxChassisSetShutdownTemperature
GxChassisSetShutdownTemperature.restype = None
GxChassisSetShutdownTemperature.argtypes = [SHORT, BOOL, DOUBLE, PSHORT]
GxChassisSetSlotsTemperaturesStates = _libraries['libGxChassis.so'].GxChassisSetSlotsTemperaturesStates
GxChassisSetSlotsTemperaturesStates.restype = None
GxChassisSetSlotsTemperaturesStates.argtypes = [SHORT, DWORD, PSHORT]
GxChassisSetTemperatureScale = _libraries['libGxChassis.so'].GxChassisSetTemperatureScale
GxChassisSetTemperatureScale.restype = None
GxChassisSetTemperatureScale.argtypes = [SHORT, SHORT, PSHORT]
GxChassisSetTemperatureThresholdMode = _libraries['libGxChassis.so'].GxChassisSetTemperatureThresholdMode
GxChassisSetTemperatureThresholdMode.restype = None
GxChassisSetTemperatureThresholdMode.argtypes = [SHORT, SHORT, PSHORT]
__all__ = ['GxChassisResetPxiTriggerLines', 'PDWORD',
           'GXCHASSIS_INVALID_FAN_POLE', 'GT_NO_ERROR',
           'GT_UNABLE_REGISTER_DEVICE',
           'GxChassisSetFanThresholdTemperatures',
           'GxChassisGetFanSpeed', 'GT_INVALID_STRLEN',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE_MONITOR', 'LONG',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE1',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE0',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE3',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE2',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE5',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE4',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE7',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE6',
           'GT_UNABLE_CREATE_PANEL',
           'GxChassisGetSlotsTemperaturesStates',
           'GxChassisGetPxiTriggerLine', 'GXCHASSIS_FAN_SPEED_MIN',
           'GXCHASSIS_FAN_SPEED_MODE_FIXED_VALUE',
           'GT_UNABLE_ALLOC_MEMORY',
           'GXCHASSIS_INVALID_PXI_TRIGGER_BUS_LINE',
           'GxChassisGetAlarmTemperature',
           'GxChassisGetShutdownTemperature', 'GxChassisSetAlarmMode',
           'GXCHASSIS_OVER_TEMPERATURE_MODE_AVERAGE_SLOTS',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE_DIR_RIGHT_TO_LEFT',
           'GXCHASSIS_ERR_RIGHT_BRIDGE',
           'GXCHASSIS_UNABLE_TO_DETECT_LEFT_BRIDGE',
           'GXCHASSIS_PANEL_MODELESS', 'PSTR',
           'GxChassisGetSlotsTemperatures', 'DOUBLE',
           'GxChassisInitialize',
           'GXCHASSIS_INVALID_PXI_TRIGGER_BUS_LINE_MODE',
           'GXCHASSIS_UNSTABLE_ORIENTATION_READING',
           'GXCHASSIS_TEMPERATURE_MIN_THRESHOLD', 'PLONG', 'SHORT',
           'GXCHASSIS_INVALID_SEGMENT',
           'GxChassisSetTemperatureScale', 'GxChassisGetAlarmMode',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE_DISCONNECT',
           'GXCHASSIS_UNABLE_TO_DETECT_RIGHT_BRIDGE',
           'GxChassisSetPxiTriggerLine',
           'GxChassisSetAlarmTemperature', 'GxChassisPanel',
           'GXCHASSIS_INVALID_PXI_TRIGGER_BUS_LINE_DIR',
           'GXCHASSIS_UNABLE_TO_DETECT_BRIDGES',
           'GT_INVALID_PARAMETER', 'PBOOL', 'GxChassisGetOrientation',
           'GXCHASSIS_FAN_MIN_THRESHOLD_TEMP_F',
           'GxChassisGetErrorString',
           'GXCHASSIS_FAN_MIN_THRESHOLD_TEMP_C',
           'GXCHASSIS_OVER_TEMPERATURE_ALARM_ENABLE',
           'GxChassisSetShutdownTemperature', 'PDOUBLE',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GxChassisRecallSettings',
           'GXCHASSIS_ERR_CONTROLLER_TIMEOUT', 'INT',
           'GxChassisGetTemperatureThresholdMode',
           'GXCHASSIS_SEGMENT_1_TO_SEGMENT_2',
           'GxChassisGetSlotsTemperaturesStatistics',
           'GxChassisSetSlotsTemperaturesStates',
           'GXCHASSIS_FAN_MAX_THRESHOLD_TEMP_F', 'GT_INVALID_MODE',
           'GXCHASSIS_FAN_MAX_THRESHOLD_TEMP_C', 'PCSTR', 'CHAR',
           'GxChassisGetFanThresholdTemperatures',
           'GT_NOT_IN_CALIBRATION_MODE',
           'GXCHASSIS_FAN_SPEED_MODE_AUTO',
           'GXCHASSIS_RECALL_USER_SETTINGS', 'WORD',
           'GXCHASSIS_FAN_SPEED_MAX', 'GxChassisGetDriverSummary',
           'GxChassisGetPowerSuppliesVoltages',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GT_INVALID_ERROR',
           'GXCHASSIS_FAN_SPEED_MID',
           'GXCHASSIS_TEMPERATURE_SCALE_ENGLISH',
           'GXCHASSIS_OVER_TEMPERATURE_ALARM_DISABLE',
           'GT_SLOT_NOT_CONFIG', 'GT_WRONG_BOARD',
           'GxChassisSetTemperatureThresholdMode', 'BYTE',
           'GXCHASSIS_ERR_LEFT_BRIDGE',
           'GxChassisGetPxiTriggerLineLevels',
           'GxChassisGetSlotTemperature', 'BOOL',
           'GXCHASSIS_OVER_TEMPERATURE_ALARM_ON', 'GT_NOT_CALIBRATED',
           'GXCHASSIS_RECALL_FACTORY_SETTINGS',
           'GXCHASSIS_TEMPERATURE_MAX_THRESHOLD',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE_DIR_LEFT_TO_RIGHT',
           'GT_BOARD_INVALID_EEPROM',
           'GXCHASSIS_TEMPERATURE_SCALE_METRIC',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE_DRIVE_LOW',
           'GT_INVALID_SLOT', 'GT_UNABLE_TO_GETTIMER',
           'GXCHASSIS_SEGMENT_0_TO_SEGMENT_1',
           'GT_PARAMETER_OUT_OF_RANGE', 'GT_CANT_OPEN_HW', 'DWORD',
           'GXCHASSIS_ERR_CONTROLLER_COM',
           'GxChassisGetTemperatureScale',
           'GXCHASSIS_INVALID_TEMPERATURE', 'GxChassisSetFanSpeed',
           'HWND', 'GXCHASSIS_ERR_ALL_BRIDGES', 'PSHORT',
           'GxChassisGetBoardSummary', 'UINT',
           'GXCHASSIS_OVER_TEMPERATURE_MODE_MAX_SLOT', 'PVOID',
           'GXCHASSIS_PXI_TRIGGER_BUS_LINE_DRIVE_HIGH',
           'GXCHASSIS_OVER_TEMPERATURE_ALARM_SNOOZE', 'PBYTE',
           'GXCHASSIS_INVALID_CHASSIS_TYPE', 'GT_BOARD_NOT_EXIST',
           'GXCHASSIS_PANEL_MODAL', 'PWORD', 'GT_INVALID_HANDLE']
