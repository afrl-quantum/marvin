from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxSw.so'] = CDLL('libGxSw.so')


# VOID = void # alias
GX6062_CONNECT_BREAKALL_BEFORE_MAKE = 0 # Variable c_int '0'
GX6377_FORM_C_LAST_CHANNEL = 4 # Variable c_int '4'
GX6616_COLUMN_LAST = 15 # Variable c_int '15'
GX6377_ROW_0 = 0 # Variable c_int '0'
GX6377_ROW_1 = 1 # Variable c_int '1'
GX6384_GROUP_B = 1 # Variable c_int '1'
GX6384_GROUP_A = 0 # Variable c_int '0'
GXSW_INVALID_COLUMN = -85 # Variable c_int '-0x00000000000000055'
GT_NO_ERROR = 0 # Variable c_int '0'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x00000000000000005'
GX6384_LAST_COLUMN_CONFIG_AS_ONE_GROUP = 63 # Variable c_int '63'
GX6021_GROUP_LAST = 3 # Variable c_int '3'
GX6264_SECTION0 = 0 # Variable c_int '0'
GX6315_RELAY_TYPE_DRIVER = 1 # Variable c_int '1'
GXSW_ERROR_CLOSED_RELAYS_OVER_LIMIT = -67 # Variable c_int '-0x00000000000000043'
GX6264_BUS_Y0 = 1 # Variable c_int '1'
GX6264_BUS_NOT_IN_USE = 0 # Variable c_int '0'
GX6384_ROW_4 = 4 # Variable c_int '4'
GX6315_CHANNEL_FIRST_HIGH_CURRENT = 1 # Variable c_int '1'
GX6021_GROUP_FIRST = 0 # Variable c_int '0'
GT_LVRT_UNSUPPORTED = -39 # Variable c_int '-0x00000000000000027'
GX6021_DISCONNECT_BREAKALL = 0 # Variable c_int '0'
GXSW_INVALID_RELAY_CYCLES_ARRAY_SIZE = -64 # Variable c_int '-0x00000000000000040'
GX6264_GROUP_H = 7 # Variable c_int '7'
GX6256_GROUP_L = 11 # Variable c_int '11'
GXSW_STATE_OPEN = 0 # Variable c_int '0'
GX6377_GROUP_A = 0 # Variable c_int '0'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x00000000000000008'
GX6021_CONNECT_MAKE_BEFORE_BREAK = 2 # Variable c_int '2'
GX6377_GROUP_B = 1 # Variable c_int '1'
GX6264_GROUP_D = 3 # Variable c_int '3'
GX6192_MUX_MODE_SINGLE_CONNECTION = 0 # Variable c_int '0'
GX6264_GROUP_F = 5 # Variable c_int '5'
GX6264_GROUP_G = 6 # Variable c_int '6'
GX6256_INPUT_13 = 13 # Variable c_int '13'
GX6616_BIT_MODE_ADAPTER_DETECTION = 0 # Variable c_int '0'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x00000000000000007'
GX6192_INPUT_15 = 15 # Variable c_int '15'
GX6062_GROUP_RELAY_TO_NEXT_GROUP = 5 # Variable c_int '5'
GX6256_BLOCK_SR = 2 # Variable c_int '2'
GX6264_GROUP_MODE_MATRIX = 1 # Variable c_int '1'
GX6062_CONNECT_MAKE = 3 # Variable c_int '3'
GX6264_BUS_SINGLE_ENDED_LO_TO_GROUP_LO = 4 # Variable c_int '4'
GXSW_INVALID_RELAYS_CYCLES_LIMIT = -63 # Variable c_int '-0x0000000000000003f'
GX6115_CHANNEL_FIRST_HIGH_CURRENT = 1 # Variable c_int '1'
GT_VISA_VIIN_ERROR = -34 # Variable c_int '-0x00000000000000022'
GX6021_CONNECT_MAKE = 3 # Variable c_int '3'
GX6256_GROUP_E = 4 # Variable c_int '4'
GX6315_CHANNEL_LAST_HIGH_CURRENT = 45 # Variable c_int '45'
GX6062_CHANNEL_LAST = 60 # Variable c_int '60'
GX6192_GROUP_B = 1 # Variable c_int '1'
GT_NOT_PXI_BOARD = -18 # Variable c_int '-0x00000000000000012'
GX6384_CONFIG_AS_TWO_GROUPS_32_CHANNELS = 0 # Variable c_int '0'
GX6115_CHANNEL_LAST_DRIVER = 9 # Variable c_int '9'
GX6256_BIT_MODE_RTM = 4 # Variable c_int '4'
GX6338_CHANNEL_FIRST = 1 # Variable c_int '1'
GX6138_CHANNEL_LAST = 38 # Variable c_int '38'
GXSW_EEPROM_CHECKSUM_INVALID = -97 # Variable c_int '-0x00000000000000061'
GX6256_MUX_MODE_MULTI_CONNECTION = 1 # Variable c_int '1'
GXSW_INVALID_GROUP = -83 # Variable c_int '-0x00000000000000053'
GX6325_CHANNEL_FIRST = 1 # Variable c_int '1'
GX6256_INTERRUPT_2 = 4 # Variable c_int '4'
GX6256_INTERRUPT_1 = 2 # Variable c_int '2'
GX6062_GROUP_RELAY3 = 2 # Variable c_int '2'
GX6264_BUS_SINGLE_ENDED_LO = 3 # Variable c_int '3'
GXSW_INVALID_SIGNAL_TYPE = -92 # Variable c_int '-0x0000000000000005c'
GT_ERROR_FILE_NOT_EXIST = -16 # Variable c_int '-0x00000000000000010'
GX6377_FORM_A_FIRST_CHANNEL = 1 # Variable c_int '1'
GX6377_FORM_A_LAST_CHANNEL = 4 # Variable c_int '4'
GXSW_PANEL_MODELESS = 0 # Variable c_int '0'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x00000000000000001'
GT_EVENT_WAIT_TIMEOUT = -43 # Variable c_int '-0x0000000000000002b'
GX6021_DISCONNECT_BREAK = 1 # Variable c_int '1'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x0000000000000000b'
GX6256_INPUT_8 = 8 # Variable c_int '8'
GX6256_INPUT_9 = 9 # Variable c_int '9'
GX6256_INPUT_6 = 6 # Variable c_int '6'
GX6256_INPUT_7 = 7 # Variable c_int '7'
GX6256_INPUT_4 = 4 # Variable c_int '4'
GX6256_INPUT_5 = 5 # Variable c_int '5'
GX6256_INPUT_2 = 2 # Variable c_int '2'
GX6256_INPUT_3 = 3 # Variable c_int '3'
GX6256_INPUT_0 = 0 # Variable c_int '0'
GX6256_INPUT_1 = 1 # Variable c_int '1'
GX6256_BIT_MODE_ALL = 7 # Variable c_int '7'
GX6062_GROUP_LAST = 11 # Variable c_int '11'
GXSW_BIT_SWITCH_OTHER = -54 # Variable c_int '-0x00000000000000036'
GX6256_BLOCK_RTM = 1 # Variable c_int '1'
GX6256_GROUP_G = 6 # Variable c_int '6'
GX6115_RELAY_TYPE_DRIVER = 1 # Variable c_int '1'
GX6264_BUS_Y1 = 3 # Variable c_int '3'
GX6062_CONNECT_MAKE_BEFORE_BREAK = 2 # Variable c_int '2'
GX6192_INPUT_10 = 10 # Variable c_int '10'
GXSW_BIT_ADAPTOR_NOT_CONNECTED = -50 # Variable c_int '-0x00000000000000032'
GX6192_INPUT_0 = 0 # Variable c_int '0'
GX6256_GROUP_D = 3 # Variable c_int '3'
GXSW_ERROR_OVER_LIMIT_RELAY_REPLACEMENT = -65 # Variable c_int '-0x00000000000000041'
GX6315_RELAY_TYPE_HIGH_CURRENT = 0 # Variable c_int '0'
GX6062_CONNECT_BREAK_BEFORE_MAKE = 1 # Variable c_int '1'
GT_DMA_MEM_ALLOC_FAILED = -45 # Variable c_int '-0x0000000000000002d'
GX6062_DISCONNECT_BREAKALL = 0 # Variable c_int '0'
GX6384_ROW_1 = 1 # Variable c_int '1'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x00000000000000015'
GXSW_INVALID_CHANNEL = -81 # Variable c_int '-0x00000000000000051'
GX6264_GROUP_MODE_SCANNER = 0 # Variable c_int '0'
GX6377_MATRIX_CONFIG_TWO_GROUPS_2X16 = 0 # Variable c_int '0'
GXSW_BIT_CLOSE_OPEN = -52 # Variable c_int '-0x00000000000000034'
GX6256_GROUP_H = 7 # Variable c_int '7'
GX6616_BIT_MODE_NO_ADAPTER_DETECTION = 1 # Variable c_int '1'
GX6192_INPUT_7 = 7 # Variable c_int '7'
GX6256_SELECTOR_MODE_MATRIX_AND_EXTERNAL = 3 # Variable c_int '3'
GX6256_GROUP_O = 14 # Variable c_int '14'
GX6062_DAISY_CHAIN_VIA_FIRST_GROUP = 1 # Variable c_int '1'
GXSW_ERROR_SET_RELAYS_TIMEOUT = -68 # Variable c_int '-0x00000000000000044'
GX6315_CHANNEL_LAST_DRIVER = 9 # Variable c_int '9'
GX6256_PATH_PRIMARY = 0 # Variable c_int '0'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x00000000000000018'
GX6384_ROW_2 = 2 # Variable c_int '2'
GX6192_INPUT_8 = 8 # Variable c_int '8'
GTSW_ERROR_CLOSED_LOOP = -60 # Variable c_int '-0x0000000000000003c'
GX6338_CHANNEL_LAST = 114 # Variable c_int '114'
GX6256_MUX_MODE_SINGLE_CONNECTION = 0 # Variable c_int '0'
GX6264_CHANNEL_LAST = 7 # Variable c_int '7'
GX6125_CHANNEL_FIRST = 1 # Variable c_int '1'
GX6264_BUS_X1 = 2 # Variable c_int '2'
GX6021_GROUP_RELAY5 = 4 # Variable c_int '4'
GX6021_GROUP_RELAY4 = 3 # Variable c_int '3'
GX6256_INTERRUPT_0 = 1 # Variable c_int '1'
GX6338_GROUP_B = 1 # Variable c_int '1'
GX6338_GROUP_C = 2 # Variable c_int '2'
GX6021_GROUP_RELAY3 = 2 # Variable c_int '2'
GX6338_GROUP_A = 0 # Variable c_int '0'
GX6256_RESET_ALL = -1 # Variable c_int '-0x00000000000000001'
GX6115_CHANNEL_LAST_HIGH_CURRENT = 15 # Variable c_int '15'
GX6325_GROUP_C = 2 # Variable c_int '2'
GX6256_SELECTOR_MODE_MATRIX_ONLY = 1 # Variable c_int '1'
GX6616_ROW_0 = 0 # Variable c_int '0'
GX6616_ROW_1 = 1 # Variable c_int '1'
GT_VISA_OPEN_ERROR = -32 # Variable c_int '-0x00000000000000020'
GX6264_RELAY_FP2 = 1 # Variable c_int '1'
GX6264_RELAY_MILITARY412 = 2 # Variable c_int '2'
GX6062_DAISY_CHAIN_NONE = 0 # Variable c_int '0'
GXSW_INVALID_RELAY_NUMBER = -61 # Variable c_int '-0x0000000000000003d'
GT_EVENT_WAIT_ERROR = -44 # Variable c_int '-0x0000000000000002c'
GX6021_CHANNEL_FIRST = 1 # Variable c_int '1'
GX6115_RELAY_TYPE_HIGH_CURRENT = 0 # Variable c_int '0'
GT_FILE_EXTENSION_NOT_SUPPORTED = -27 # Variable c_int '-0x0000000000000001b'
GT_INVALID_CALIBRATION_TIME_STAMP = -29 # Variable c_int '-0x0000000000000001d'
GX6062_GROUP_RELAY_TO_EXTERNAL_COAX = 6 # Variable c_int '6'
GXSW_INVALID_ROW = -84 # Variable c_int '-0x00000000000000054'
GX6256_BIT_MODE_MUX = 1 # Variable c_int '1'
GXSW_INVALID_BLOCK = -95 # Variable c_int '-0x0000000000000005f'
GX6315_GROUP_A = 0 # Variable c_int '0'
GT_VISA_GETATTRIBUTE_ERROR = -33 # Variable c_int '-0x00000000000000021'
GX6264_BUS_DIFFERENTIAL = 1 # Variable c_int '1'
GT_VISA_MEMMAP_ERROR = -35 # Variable c_int '-0x00000000000000023'
GX6616_GROUP_B = 1 # Variable c_int '1'
GX6062_GROUP_RELAY1 = 0 # Variable c_int '0'
GX6062_GROUP_RELAY2 = 1 # Variable c_int '1'
GX6115_CHANNEL_FIRST_DRIVER = 1 # Variable c_int '1'
GX6062_GROUP_RELAY4 = 3 # Variable c_int '3'
GX6062_GROUP_RELAY5 = 4 # Variable c_int '4'
GXSW_EEPROM_BUSY_TIMEOUT = -66 # Variable c_int '-0x00000000000000042'
GT_INVALID_ERROR = -20 # Variable c_int '-0x00000000000000014'
GX6256_SELECTOR_MODE_NONE = 0 # Variable c_int '0'
GX6315_GROUP_B = 1 # Variable c_int '1'
GX6256_INPUT_10 = 10 # Variable c_int '10'
GT_UNABLE_TO_OPEN_FILE = -15 # Variable c_int '-0x0000000000000000f'
GX6315_CHANNEL_FIRST_DRIVER = 1 # Variable c_int '1'
GX6192_SELECTOR_MODE_MATRIX_AND_DIGITAL = 3 # Variable c_int '3'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x00000000000000006'
GXSW_INVALID_DAISY_CHAIN_MODE = -87 # Variable c_int '-0x00000000000000057'
GX6256_SELECTOR_MODE_MATRIX_ISOLATED = 4 # Variable c_int '4'
GXSW_REPORT_FORMAT_TXT = 0 # Variable c_int '0'
GX6021_CONNECT_BREAK_BEFORE_MAKE = 1 # Variable c_int '1'
GX6325_GROUP_B = 1 # Variable c_int '1'
GX6315_GROUP_C = 2 # Variable c_int '2'
GX6062_DISCONNECT_BREAK = 1 # Variable c_int '1'
GX6192_INPUT_14 = 14 # Variable c_int '14'
GX6325_GROUP_A = 0 # Variable c_int '0'
GX6377_FORM_C_FIRST_CHANNEL = 1 # Variable c_int '1'
GX6384_CONFIG_AS_ONE_GROUP_64_CHANNELS = 1 # Variable c_int '1'
GX6264_BUS_X0 = 0 # Variable c_int '0'
GX6384_FIRST_COLUMN = 0 # Variable c_int '0'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x0000000000000000d'
GXSW_BIT_CLOSE_COLUMN = -53 # Variable c_int '-0x00000000000000035'
GX6264_SECTION1 = 1 # Variable c_int '1'
GT_VISA_LOAD_DLL_ERROR = -30 # Variable c_int '-0x0000000000000001e'
GXSW_SIMULATION_INI_FILE_READ_ERROR = -94 # Variable c_int '-0x0000000000000005e'
GT_EVENT_ENABLE_FAILED = -41 # Variable c_int '-0x00000000000000029'
GX6062_DAISY_CHAIN_VIA_LAST_GROUP = 2 # Variable c_int '2'
GX6192_SELECTOR_MODE_MATRIX_ONLY = 1 # Variable c_int '1'
GX6192_GROUP_M = 12 # Variable c_int '12'
GX6264_CHANNEL_FIRST = 0 # Variable c_int '0'
GXSW_STATE_CLOSE = 1 # Variable c_int '1'
GX6377_MATRIX_CONFIG_ONE_GROUP_2X32 = 1 # Variable c_int '1'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x00000000000000004'
GT_WRONG_BOARD = -3 # Variable c_int '-0x00000000000000003'
GX6264_CONNECT_ONLY = 0 # Variable c_int '0'
GX6264_GROUP_A = 0 # Variable c_int '0'
GXSW_INVALID_INPUT = -93 # Variable c_int '-0x0000000000000005d'
GX6021_GROUP_RELAY1 = 0 # Variable c_int '0'
GT_SYNC_CREATE = -37 # Variable c_int '-0x00000000000000025'
GX6192_RESET_ALL = -1 # Variable c_int '-0x00000000000000001'
GX6377_HIGH_CURRENT_LAST_CHANNEL = 5 # Variable c_int '5'
GXSW_INVALID_NUMBER_OF_RELAYS = -62 # Variable c_int '-0x0000000000000003e'
GXSW_INVALID_RELAY = -86 # Variable c_int '-0x00000000000000056'
GX6256_GROUP_K = 10 # Variable c_int '10'
GX6021_DAISY_CHAIN_VIA_LAST_GROUP = 2 # Variable c_int '2'
GXSW_BIT_COMPARATOR = -51 # Variable c_int '-0x00000000000000033'
GX6377_RELAY_TYPE_HIGH_CURRENT = 0 # Variable c_int '0'
GX6021_GROUP_RELAY2 = 1 # Variable c_int '1'
GX6138_CHANNEL_FIRST = 1 # Variable c_int '1'
GX6264_GROUP_E = 4 # Variable c_int '4'
GX6192_INPUT_1 = 1 # Variable c_int '1'
GXSW_INVALID_GROUP_MODE = -89 # Variable c_int '-0x00000000000000059'
GX6192_INPUT_3 = 3 # Variable c_int '3'
GX6192_INPUT_2 = 2 # Variable c_int '2'
GX6192_INPUT_5 = 5 # Variable c_int '5'
GX6192_INPUT_4 = 4 # Variable c_int '4'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x0000000000000000c'
GX6192_INPUT_6 = 6 # Variable c_int '6'
GX6192_INPUT_9 = 9 # Variable c_int '9'
GX6264_CONNECT_COMBINED = 1 # Variable c_int '1'
GT_ERR_CHECKSUM = -48 # Variable c_int '-0x00000000000000030'
GX6264_BUS_SINGLE_ENDED_HI = 2 # Variable c_int '2'
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x0000000000000000a'
GX6264_GROUP_C = 2 # Variable c_int '2'
GXSW_INVALID_PATH = -91 # Variable c_int '-0x0000000000000005b'
GX6264_GROUP_B = 1 # Variable c_int '1'
GT_SYNC_TIMEOUT = -38 # Variable c_int '-0x00000000000000026'
GX6021_GROUP_RELAY_TO_EXTERNAL_COAX = 6 # Variable c_int '6'
GX6062_DAISY_CHAIN_VIA_FIRST_AND_LAST_GROUP = 3 # Variable c_int '3'
GX6021_DAISY_CHAIN_VIA_FIRST_AND_LAST_GROUP = 3 # Variable c_int '3'
GX6377_RELAY_TYPE_FORM_A = 1 # Variable c_int '1'
GX6377_RELAY_TYPE_FORM_C = 2 # Variable c_int '2'
GX6192_GROUP_A = 0 # Variable c_int '0'
GT_NOT_GEOTEST_BOARD = -14 # Variable c_int '-0x0000000000000000e'
GT_INVALID_SLOT = -22 # Variable c_int '-0x00000000000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x00000000000000009'
GXSW_REPORT_FORMAT_CSV = 1 # Variable c_int '1'
GXSW_INVALID_ERROR = -99 # Variable c_int '-0x00000000000000063'
GT_PARAMETER_OUT_OF_RANGE = -26 # Variable c_int '-0x0000000000000001a'
GX6616_GROUP_C = 2 # Variable c_int '2'
GX6384_ROW_5 = 5 # Variable c_int '5'
GX6616_GROUP_A = 0 # Variable c_int '0'
GXSW_INVALID_RELAY_TYPE = -88 # Variable c_int '-0x00000000000000058'
GX6192_SELECTOR_MODE_DIGITAL_ONLY = 2 # Variable c_int '2'
GX6616_GROUP_F = 5 # Variable c_int '5'
GX6616_GROUP_E = 4 # Variable c_int '4'
GX6616_GROUP_D = 3 # Variable c_int '3'
GXSW_INVALID_BUS = -82 # Variable c_int '-0x00000000000000052'
GXSW_INVALID_SECTION = -90 # Variable c_int '-0x0000000000000005a'
GX6616_COLUMN_FIRST = 0 # Variable c_int '0'
GT_ERR_DMA_MEM_FREE = -47 # Variable c_int '-0x0000000000000002f'
GX6192_MUX_MODE_MULTI_CONNECTION = 1 # Variable c_int '1'
GX6062_CHANNEL_FIRST = 1 # Variable c_int '1'
GX6384_ROW_0 = 0 # Variable c_int '0'
GX6021_CHANNEL_LAST = 20 # Variable c_int '20'
GT_VISA_OPENDEFAULTRM_ERROR = -31 # Variable c_int '-0x0000000000000001f'
GX6021_DAISY_CHAIN_VIA_FIRST_GROUP = 1 # Variable c_int '1'
GX6256_BLOCK_BOARD = 0 # Variable c_int '0'
GXSW_INVALID_CONFIGURATION = -80 # Variable c_int '-0x00000000000000050'
GX6256_BIT_MODE_MATRIX = 2 # Variable c_int '2'
GX6264_RELAY_MILITARY172 = 3 # Variable c_int '3'
GX6021_CONNECT_BREAKALL_BEFORE_MAKE = 0 # Variable c_int '0'
GX6021_DAISY_CHAIN_NONE = 0 # Variable c_int '0'
GX6021_GROUP_RELAY_TO_NEXT_GROUP = 5 # Variable c_int '5'
GX6384_ROW_3 = 3 # Variable c_int '3'
GX6264_RELAY_REED = 0 # Variable c_int '0'
GX6256_GROUP_C = 2 # Variable c_int '2'
GX6256_GROUP_B = 1 # Variable c_int '1'
GX6256_GROUP_A = 0 # Variable c_int '0'
GX6192_GROUP_E = 4 # Variable c_int '4'
GX6192_INPUT_11 = 11 # Variable c_int '11'
GX6256_GROUP_F = 5 # Variable c_int '5'
GX6192_INPUT_13 = 13 # Variable c_int '13'
GX6192_INPUT_12 = 12 # Variable c_int '12'
GT_EVENT_DISABLE_FAILED = -42 # Variable c_int '-0x0000000000000002a'
GX6256_GROUP_J = 9 # Variable c_int '9'
GX6256_GROUP_I = 8 # Variable c_int '8'
GXSW_ERROR_BIT_STILL_RUNNING = -96 # Variable c_int '-0x00000000000000060'
GT_ERR_DMA_MEM_UN_MAP = -46 # Variable c_int '-0x0000000000000002e'
GX6256_GROUP_N = 13 # Variable c_int '13'
GX6256_GROUP_M = 12 # Variable c_int '12'
GT_INVALID_CHASSIS_NUMBER = -28 # Variable c_int '-0x0000000000000001c'
GX6256_GROUP_P = 15 # Variable c_int '15'
GX6256_PATH_SECONDARY = 1 # Variable c_int '1'
GX6384_LAST_COLUMN_CONFIG_AS_TWO_GROUPS = 31 # Variable c_int '31'
GT_ERR_MODE_NOT_SUPPORTED_BY_SLOT = -17 # Variable c_int '-0x00000000000000011'
GX6192_SELECTOR_MODE_NONE = 0 # Variable c_int '0'
GXSW_PANEL_MODAL = 1 # Variable c_int '1'
GT_NOT_PCI_BOARD = -19 # Variable c_int '-0x00000000000000013'
GX6192_GROUP_L = 11 # Variable c_int '11'
GX6192_GROUP_F = 5 # Variable c_int '5'
GX6192_GROUP_N = 13 # Variable c_int '13'
GX6192_GROUP_O = 14 # Variable c_int '14'
GX6192_GROUP_H = 7 # Variable c_int '7'
GX6192_GROUP_I = 8 # Variable c_int '8'
GX6192_GROUP_J = 9 # Variable c_int '9'
GX6192_GROUP_K = 10 # Variable c_int '10'
GX6192_GROUP_D = 3 # Variable c_int '3'
GX6192_GROUP_P = 15 # Variable c_int '15'
GX6062_GROUP_FIRST = 0 # Variable c_int '0'
GX6192_GROUP_G = 6 # Variable c_int '6'
GXSW_BIT_PARTIAL = -55 # Variable c_int '-0x00000000000000037'
GX6125_CHANNEL_LAST = 25 # Variable c_int '25'
GX6192_GROUP_C = 2 # Variable c_int '2'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x00000000000000002'
GT_INVALID_MODE = -25 # Variable c_int '-0x00000000000000019'
GX6256_SELECTOR_MODE_EXTERNAL_ONLY = 2 # Variable c_int '2'
GX6325_CHANNEL_LAST = 75 # Variable c_int '75'
GX6377_HIGH_CURRENT_FIRST_CHANNEL = 1 # Variable c_int '1'
GX6256_INPUT_14 = 14 # Variable c_int '14'
GX6256_INPUT_15 = 15 # Variable c_int '15'
GXSW_BIT_OK = 1 # Variable c_int '1'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x00000000000000017'
GX6377_MATRIX_FIRST_COLUMN = 0 # Variable c_int '0'
GX6256_INPUT_11 = 11 # Variable c_int '11'
GX6256_INPUT_12 = 12 # Variable c_int '12'
GT_LICENSE = -40 # Variable c_int '-0x00000000000000028'
CHAR = c_char
BYTE = c_ubyte
SHORT = c_short
WORD = c_ushort
INT = c_int
UINT = c_uint
LPLONG = POINTER(c_int)
LONG = c_int
DWORD = c_uint
PULONG = POINTER(c_uint)
ULONG = c_uint
LPDWORD = POINTER(c_uint)
DOUBLE = c_double
BOOL = c_int
PBOOL = POINTER(BOOL)
PBYTE = POINTER(BYTE)
PSHORT = POINTER(SHORT)
PWORD = POINTER(WORD)
PLONG = POINTER(c_int)
PDWORD = POINTER(c_uint)
PDOUBLE = POINTER(DOUBLE)
PVOID = c_void_p
PSTR = STRING
HWND = c_void_p
PCSTR = STRING
GxSWGetErrorString = _libraries['libGxSw.so'].GxSWGetErrorString
GxSWGetErrorString.restype = None
GxSWGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxSWGetDriverSummary = _libraries['libGxSw.so'].GxSWGetDriverSummary
GxSWGetDriverSummary.restype = None
GxSWGetDriverSummary.argtypes = [PSTR, SHORT, POINTER(DWORD), PSHORT]
Gt_EventCallback = CFUNCTYPE(LONG, SHORT, SHORT, PVOID)
Gx6021Initialize = _libraries['libGxSw.so'].Gx6021Initialize
Gx6021Initialize.restype = None
Gx6021Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6021InitializeVisa = _libraries['libGxSw.so'].Gx6021InitializeVisa
Gx6021InitializeVisa.restype = None
Gx6021InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6021Reset = _libraries['libGxSw.so'].Gx6021Reset
Gx6021Reset.restype = None
Gx6021Reset.argtypes = [SHORT, PSHORT]
Gx6021GetBoardSummary = _libraries['libGxSw.so'].Gx6021GetBoardSummary
Gx6021GetBoardSummary.restype = None
Gx6021GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6021ConnectChannels = _libraries['libGxSw.so'].Gx6021ConnectChannels
Gx6021ConnectChannels.restype = None
Gx6021ConnectChannels.argtypes = [SHORT, SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx6021DisconnectChannels = _libraries['libGxSw.so'].Gx6021DisconnectChannels
Gx6021DisconnectChannels.restype = None
Gx6021DisconnectChannels.argtypes = [SHORT, SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx6021GetChannel = _libraries['libGxSw.so'].Gx6021GetChannel
Gx6021GetChannel.restype = None
Gx6021GetChannel.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6021Close = _libraries['libGxSw.so'].Gx6021Close
Gx6021Close.restype = None
Gx6021Close.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6021Open = _libraries['libGxSw.so'].Gx6021Open
Gx6021Open.restype = None
Gx6021Open.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6021SetGroupRelays = _libraries['libGxSw.so'].Gx6021SetGroupRelays
Gx6021SetGroupRelays.restype = None
Gx6021SetGroupRelays.argtypes = [SHORT, SHORT, BYTE, PSHORT]
Gx6021GetGroupRelays = _libraries['libGxSw.so'].Gx6021GetGroupRelays
Gx6021GetGroupRelays.restype = None
Gx6021GetGroupRelays.argtypes = [SHORT, SHORT, PBYTE, PSHORT]
Gx6021ConnectGroupToExternalCoax = _libraries['libGxSw.so'].Gx6021ConnectGroupToExternalCoax
Gx6021ConnectGroupToExternalCoax.restype = None
Gx6021ConnectGroupToExternalCoax.argtypes = [SHORT, SHORT, PSHORT]
Gx6021DisconnectGroupToExternalCoax = _libraries['libGxSw.so'].Gx6021DisconnectGroupToExternalCoax
Gx6021DisconnectGroupToExternalCoax.restype = None
Gx6021DisconnectGroupToExternalCoax.argtypes = [SHORT, SHORT, PSHORT]
Gx6021GetDaisyChainMode = _libraries['libGxSw.so'].Gx6021GetDaisyChainMode
Gx6021GetDaisyChainMode.restype = None
Gx6021GetDaisyChainMode.argtypes = [SHORT, PSHORT, PSHORT]
Gx6021SetDaisyChainMode = _libraries['libGxSw.so'].Gx6021SetDaisyChainMode
Gx6021SetDaisyChainMode.restype = None
Gx6021SetDaisyChainMode.argtypes = [SHORT, SHORT, PSHORT]
Gx6062Initialize = _libraries['libGxSw.so'].Gx6062Initialize
Gx6062Initialize.restype = None
Gx6062Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6062InitializeVisa = _libraries['libGxSw.so'].Gx6062InitializeVisa
Gx6062InitializeVisa.restype = None
Gx6062InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6062Reset = _libraries['libGxSw.so'].Gx6062Reset
Gx6062Reset.restype = None
Gx6062Reset.argtypes = [SHORT, PSHORT]
Gx6062GetBoardSummary = _libraries['libGxSw.so'].Gx6062GetBoardSummary
Gx6062GetBoardSummary.restype = None
Gx6062GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6062ConnectChannels = _libraries['libGxSw.so'].Gx6062ConnectChannels
Gx6062ConnectChannels.restype = None
Gx6062ConnectChannels.argtypes = [SHORT, SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx6062DisconnectChannels = _libraries['libGxSw.so'].Gx6062DisconnectChannels
Gx6062DisconnectChannels.restype = None
Gx6062DisconnectChannels.argtypes = [SHORT, SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx6062GetChannel = _libraries['libGxSw.so'].Gx6062GetChannel
Gx6062GetChannel.restype = None
Gx6062GetChannel.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6062Close = _libraries['libGxSw.so'].Gx6062Close
Gx6062Close.restype = None
Gx6062Close.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6062Open = _libraries['libGxSw.so'].Gx6062Open
Gx6062Open.restype = None
Gx6062Open.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6062SetGroupRelays = _libraries['libGxSw.so'].Gx6062SetGroupRelays
Gx6062SetGroupRelays.restype = None
Gx6062SetGroupRelays.argtypes = [SHORT, SHORT, BYTE, PSHORT]
Gx6062GetGroupRelays = _libraries['libGxSw.so'].Gx6062GetGroupRelays
Gx6062GetGroupRelays.restype = None
Gx6062GetGroupRelays.argtypes = [SHORT, SHORT, PBYTE, PSHORT]
Gx6062ConnectGroupToExternalCoax = _libraries['libGxSw.so'].Gx6062ConnectGroupToExternalCoax
Gx6062ConnectGroupToExternalCoax.restype = None
Gx6062ConnectGroupToExternalCoax.argtypes = [SHORT, SHORT, PSHORT]
Gx6062DisconnectGroupToExternalCoax = _libraries['libGxSw.so'].Gx6062DisconnectGroupToExternalCoax
Gx6062DisconnectGroupToExternalCoax.restype = None
Gx6062DisconnectGroupToExternalCoax.argtypes = [SHORT, SHORT, PSHORT]
Gx6062GetDaisyChainMode = _libraries['libGxSw.so'].Gx6062GetDaisyChainMode
Gx6062GetDaisyChainMode.restype = None
Gx6062GetDaisyChainMode.argtypes = [SHORT, PSHORT, PSHORT]
Gx6062SetDaisyChainMode = _libraries['libGxSw.so'].Gx6062SetDaisyChainMode
Gx6062SetDaisyChainMode.restype = None
Gx6062SetDaisyChainMode.argtypes = [SHORT, SHORT, PSHORT]
Gx6115Initialize = _libraries['libGxSw.so'].Gx6115Initialize
Gx6115Initialize.restype = None
Gx6115Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6115InitializeVisa = _libraries['libGxSw.so'].Gx6115InitializeVisa
Gx6115InitializeVisa.restype = None
Gx6115InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6115Reset = _libraries['libGxSw.so'].Gx6115Reset
Gx6115Reset.restype = None
Gx6115Reset.argtypes = [SHORT, PSHORT]
Gx6115GetBoardSummary = _libraries['libGxSw.so'].Gx6115GetBoardSummary
Gx6115GetBoardSummary.restype = None
Gx6115GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6115Close = _libraries['libGxSw.so'].Gx6115Close
Gx6115Close.restype = None
Gx6115Close.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6115Open = _libraries['libGxSw.so'].Gx6115Open
Gx6115Open.restype = None
Gx6115Open.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6115GetChannel = _libraries['libGxSw.so'].Gx6115GetChannel
Gx6115GetChannel.restype = None
Gx6115GetChannel.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx6115SetChannels = _libraries['libGxSw.so'].Gx6115SetChannels
Gx6115SetChannels.restype = None
Gx6115SetChannels.argtypes = [SHORT, LONG, PSHORT]
Gx6115GetChannels = _libraries['libGxSw.so'].Gx6115GetChannels
Gx6115GetChannels.restype = None
Gx6115GetChannels.argtypes = [SHORT, POINTER(LONG), PSHORT]
Gx6125Initialize = _libraries['libGxSw.so'].Gx6125Initialize
Gx6125Initialize.restype = None
Gx6125Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6125InitializeVisa = _libraries['libGxSw.so'].Gx6125InitializeVisa
Gx6125InitializeVisa.restype = None
Gx6125InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6125Reset = _libraries['libGxSw.so'].Gx6125Reset
Gx6125Reset.restype = None
Gx6125Reset.argtypes = [SHORT, PSHORT]
Gx6125GetBoardSummary = _libraries['libGxSw.so'].Gx6125GetBoardSummary
Gx6125GetBoardSummary.restype = None
Gx6125GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6125Close = _libraries['libGxSw.so'].Gx6125Close
Gx6125Close.restype = None
Gx6125Close.argtypes = [SHORT, SHORT, PSHORT]
Gx6125Open = _libraries['libGxSw.so'].Gx6125Open
Gx6125Open.restype = None
Gx6125Open.argtypes = [SHORT, SHORT, PSHORT]
Gx6125GetChannel = _libraries['libGxSw.so'].Gx6125GetChannel
Gx6125GetChannel.restype = None
Gx6125GetChannel.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6125SetChannels = _libraries['libGxSw.so'].Gx6125SetChannels
Gx6125SetChannels.restype = None
Gx6125SetChannels.argtypes = [SHORT, LONG, PSHORT]
Gx6125GetChannels = _libraries['libGxSw.so'].Gx6125GetChannels
Gx6125GetChannels.restype = None
Gx6125GetChannels.argtypes = [SHORT, POINTER(LONG), PSHORT]
Gx6138Initialize = _libraries['libGxSw.so'].Gx6138Initialize
Gx6138Initialize.restype = None
Gx6138Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6138InitializeVisa = _libraries['libGxSw.so'].Gx6138InitializeVisa
Gx6138InitializeVisa.restype = None
Gx6138InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6138Reset = _libraries['libGxSw.so'].Gx6138Reset
Gx6138Reset.restype = None
Gx6138Reset.argtypes = [SHORT, PSHORT]
Gx6138GetBoardSummary = _libraries['libGxSw.so'].Gx6138GetBoardSummary
Gx6138GetBoardSummary.restype = None
Gx6138GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6138Close = _libraries['libGxSw.so'].Gx6138Close
Gx6138Close.restype = None
Gx6138Close.argtypes = [SHORT, SHORT, PSHORT]
Gx6138Open = _libraries['libGxSw.so'].Gx6138Open
Gx6138Open.restype = None
Gx6138Open.argtypes = [SHORT, SHORT, PSHORT]
Gx6138GetChannel = _libraries['libGxSw.so'].Gx6138GetChannel
Gx6138GetChannel.restype = None
Gx6138GetChannel.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6138SetChannels = _libraries['libGxSw.so'].Gx6138SetChannels
Gx6138SetChannels.restype = None
Gx6138SetChannels.argtypes = [SHORT, LONG, LONG, PSHORT]
Gx6138GetChannels = _libraries['libGxSw.so'].Gx6138GetChannels
Gx6138GetChannels.restype = None
Gx6138GetChannels.argtypes = [SHORT, POINTER(LONG), POINTER(LONG), PSHORT]
Gx6196Initialize = _libraries['libGxSw.so'].Gx6196Initialize
Gx6196Initialize.restype = None
Gx6196Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6196InitializeVisa = _libraries['libGxSw.so'].Gx6196InitializeVisa
Gx6196InitializeVisa.restype = None
Gx6196InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6196Reset = _libraries['libGxSw.so'].Gx6196Reset
Gx6196Reset.restype = None
Gx6196Reset.argtypes = [SHORT, PSHORT]
Gx6196GetBoardSummary = _libraries['libGxSw.so'].Gx6196GetBoardSummary
Gx6196GetBoardSummary.restype = None
Gx6196GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6196Close = _libraries['libGxSw.so'].Gx6196Close
Gx6196Close.restype = None
Gx6196Close.argtypes = [SHORT, SHORT, PSHORT]
Gx6196Open = _libraries['libGxSw.so'].Gx6196Open
Gx6196Open.restype = None
Gx6196Open.argtypes = [SHORT, SHORT, PSHORT]
Gx6196GetChannel = _libraries['libGxSw.so'].Gx6196GetChannel
Gx6196GetChannel.restype = None
Gx6196GetChannel.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6196WritePio = _libraries['libGxSw.so'].Gx6196WritePio
Gx6196WritePio.restype = None
Gx6196WritePio.argtypes = [SHORT, BYTE, PSHORT]
Gx6196ReadPio = _libraries['libGxSw.so'].Gx6196ReadPio
Gx6196ReadPio.restype = None
Gx6196ReadPio.argtypes = [SHORT, PBYTE, PSHORT]
Gx6196GetPio = _libraries['libGxSw.so'].Gx6196GetPio
Gx6196GetPio.restype = None
Gx6196GetPio.argtypes = [SHORT, PBYTE, PSHORT]
Gx6196SetPioOutputEnable = _libraries['libGxSw.so'].Gx6196SetPioOutputEnable
Gx6196SetPioOutputEnable.restype = None
Gx6196SetPioOutputEnable.argtypes = [SHORT, BYTE, PSHORT]
Gx6196GetPioOutputEnable = _libraries['libGxSw.so'].Gx6196GetPioOutputEnable
Gx6196GetPioOutputEnable.restype = None
Gx6196GetPioOutputEnable.argtypes = [SHORT, PBYTE, PSHORT]
Gx6196SendReceiveModule = _libraries['libGxSw.so'].Gx6196SendReceiveModule
Gx6196SendReceiveModule.restype = None
Gx6196SendReceiveModule.argtypes = [SHORT, SHORT, PWORD, PWORD, LONG, PSHORT]
Gx6264Initialize = _libraries['libGxSw.so'].Gx6264Initialize
Gx6264Initialize.restype = None
Gx6264Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6264InitializeVisa = _libraries['libGxSw.so'].Gx6264InitializeVisa
Gx6264InitializeVisa.restype = None
Gx6264InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6264Reset = _libraries['libGxSw.so'].Gx6264Reset
Gx6264Reset.restype = None
Gx6264Reset.argtypes = [SHORT, PSHORT]
Gx6264GetBoardSummary = _libraries['libGxSw.so'].Gx6264GetBoardSummary
Gx6264GetBoardSummary.restype = None
Gx6264GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6264ResetBus = _libraries['libGxSw.so'].Gx6264ResetBus
Gx6264ResetBus.restype = None
Gx6264ResetBus.argtypes = [SHORT, SHORT, PSHORT]
Gx6264ResetGroup = _libraries['libGxSw.so'].Gx6264ResetGroup
Gx6264ResetGroup.restype = None
Gx6264ResetGroup.argtypes = [SHORT, SHORT, PSHORT]
Gx6264ResetSection = _libraries['libGxSw.so'].Gx6264ResetSection
Gx6264ResetSection.restype = None
Gx6264ResetSection.argtypes = [SHORT, SHORT, PSHORT]
Gx6264ConnectBus = _libraries['libGxSw.so'].Gx6264ConnectBus
Gx6264ConnectBus.restype = None
Gx6264ConnectBus.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6264ConnectChannel = _libraries['libGxSw.so'].Gx6264ConnectChannel
Gx6264ConnectChannel.restype = None
Gx6264ConnectChannel.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6264GetBusMode = _libraries['libGxSw.so'].Gx6264GetBusMode
Gx6264GetBusMode.restype = None
Gx6264GetBusMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6264SetBusMode = _libraries['libGxSw.so'].Gx6264SetBusMode
Gx6264SetBusMode.restype = None
Gx6264SetBusMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6264RemoveBus = _libraries['libGxSw.so'].Gx6264RemoveBus
Gx6264RemoveBus.restype = None
Gx6264RemoveBus.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6264RemoveSectionsBus = _libraries['libGxSw.so'].Gx6264RemoveSectionsBus
Gx6264RemoveSectionsBus.restype = None
Gx6264RemoveSectionsBus.argtypes = [SHORT, SHORT, PSHORT]
Gx6264ConnectSectionsBus = _libraries['libGxSw.so'].Gx6264ConnectSectionsBus
Gx6264ConnectSectionsBus.restype = None
Gx6264ConnectSectionsBus.argtypes = [SHORT, SHORT, PSHORT]
Gx6264GetGroup = _libraries['libGxSw.so'].Gx6264GetGroup
Gx6264GetGroup.restype = None
Gx6264GetGroup.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6264GetRelayType = _libraries['libGxSw.so'].Gx6264GetRelayType
Gx6264GetRelayType.restype = None
Gx6264GetRelayType.argtypes = [SHORT, PSHORT, PSHORT]
Gx6264GetSectionsBus = _libraries['libGxSw.so'].Gx6264GetSectionsBus
Gx6264GetSectionsBus.restype = None
Gx6264GetSectionsBus.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6264SetGroupMode = _libraries['libGxSw.so'].Gx6264SetGroupMode
Gx6264SetGroupMode.restype = None
Gx6264SetGroupMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6264GetGroupMode = _libraries['libGxSw.so'].Gx6264GetGroupMode
Gx6264GetGroupMode.restype = None
Gx6264GetGroupMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6264RemoveChannel = _libraries['libGxSw.so'].Gx6264RemoveChannel
Gx6264RemoveChannel.restype = None
Gx6264RemoveChannel.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6264SetGroupChannels = _libraries['libGxSw.so'].Gx6264SetGroupChannels
Gx6264SetGroupChannels.restype = None
Gx6264SetGroupChannels.argtypes = [SHORT, SHORT, BYTE, PSHORT]
Gx6264GetGroupChannels = _libraries['libGxSw.so'].Gx6264GetGroupChannels
Gx6264GetGroupChannels.restype = None
Gx6264GetGroupChannels.argtypes = [SHORT, SHORT, PBYTE, PSHORT]
Gx6315Initialize = _libraries['libGxSw.so'].Gx6315Initialize
Gx6315Initialize.restype = None
Gx6315Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6315InitializeVisa = _libraries['libGxSw.so'].Gx6315InitializeVisa
Gx6315InitializeVisa.restype = None
Gx6315InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6315Reset = _libraries['libGxSw.so'].Gx6315Reset
Gx6315Reset.restype = None
Gx6315Reset.argtypes = [SHORT, PSHORT]
Gx6315GetBoardSummary = _libraries['libGxSw.so'].Gx6315GetBoardSummary
Gx6315GetBoardSummary.restype = None
Gx6315GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6315Close = _libraries['libGxSw.so'].Gx6315Close
Gx6315Close.restype = None
Gx6315Close.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6315Open = _libraries['libGxSw.so'].Gx6315Open
Gx6315Open.restype = None
Gx6315Open.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6315GetChannel = _libraries['libGxSw.so'].Gx6315GetChannel
Gx6315GetChannel.restype = None
Gx6315GetChannel.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx6315SetGroupChannels = _libraries['libGxSw.so'].Gx6315SetGroupChannels
Gx6315SetGroupChannels.restype = None
Gx6315SetGroupChannels.argtypes = [SHORT, SHORT, LONG, PSHORT]
Gx6315GetGroupChannels = _libraries['libGxSw.so'].Gx6315GetGroupChannels
Gx6315GetGroupChannels.restype = None
Gx6315GetGroupChannels.argtypes = [SHORT, SHORT, POINTER(LONG), PSHORT]
Gx6325Initialize = _libraries['libGxSw.so'].Gx6325Initialize
Gx6325Initialize.restype = None
Gx6325Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6325InitializeVisa = _libraries['libGxSw.so'].Gx6325InitializeVisa
Gx6325InitializeVisa.restype = None
Gx6325InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6325Reset = _libraries['libGxSw.so'].Gx6325Reset
Gx6325Reset.restype = None
Gx6325Reset.argtypes = [SHORT, PSHORT]
Gx6325GetBoardSummary = _libraries['libGxSw.so'].Gx6325GetBoardSummary
Gx6325GetBoardSummary.restype = None
Gx6325GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6325GroupReset = _libraries['libGxSw.so'].Gx6325GroupReset
Gx6325GroupReset.restype = None
Gx6325GroupReset.argtypes = [SHORT, SHORT, PSHORT]
Gx6325Close = _libraries['libGxSw.so'].Gx6325Close
Gx6325Close.restype = None
Gx6325Close.argtypes = [SHORT, SHORT, PSHORT]
Gx6325Open = _libraries['libGxSw.so'].Gx6325Open
Gx6325Open.restype = None
Gx6325Open.argtypes = [SHORT, SHORT, PSHORT]
Gx6325GetChannel = _libraries['libGxSw.so'].Gx6325GetChannel
Gx6325GetChannel.restype = None
Gx6325GetChannel.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6325SetGroupChannels = _libraries['libGxSw.so'].Gx6325SetGroupChannels
Gx6325SetGroupChannels.restype = None
Gx6325SetGroupChannels.argtypes = [SHORT, SHORT, LONG, PSHORT]
Gx6325GetGroupChannels = _libraries['libGxSw.so'].Gx6325GetGroupChannels
Gx6325GetGroupChannels.restype = None
Gx6325GetGroupChannels.argtypes = [SHORT, SHORT, POINTER(LONG), PSHORT]
Gx6338Initialize = _libraries['libGxSw.so'].Gx6338Initialize
Gx6338Initialize.restype = None
Gx6338Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6338InitializeVisa = _libraries['libGxSw.so'].Gx6338InitializeVisa
Gx6338InitializeVisa.restype = None
Gx6338InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6338Reset = _libraries['libGxSw.so'].Gx6338Reset
Gx6338Reset.restype = None
Gx6338Reset.argtypes = [SHORT, PSHORT]
Gx6338GetBoardSummary = _libraries['libGxSw.so'].Gx6338GetBoardSummary
Gx6338GetBoardSummary.restype = None
Gx6338GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6338GroupReset = _libraries['libGxSw.so'].Gx6338GroupReset
Gx6338GroupReset.restype = None
Gx6338GroupReset.argtypes = [SHORT, SHORT, PSHORT]
Gx6338Close = _libraries['libGxSw.so'].Gx6338Close
Gx6338Close.restype = None
Gx6338Close.argtypes = [SHORT, SHORT, PSHORT]
Gx6338Open = _libraries['libGxSw.so'].Gx6338Open
Gx6338Open.restype = None
Gx6338Open.argtypes = [SHORT, SHORT, PSHORT]
Gx6338GetChannel = _libraries['libGxSw.so'].Gx6338GetChannel
Gx6338GetChannel.restype = None
Gx6338GetChannel.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6338SetGroupChannels = _libraries['libGxSw.so'].Gx6338SetGroupChannels
Gx6338SetGroupChannels.restype = None
Gx6338SetGroupChannels.argtypes = [SHORT, SHORT, LONG, LONG, PSHORT]
Gx6338GetGroupChannels = _libraries['libGxSw.so'].Gx6338GetGroupChannels
Gx6338GetGroupChannels.restype = None
Gx6338GetGroupChannels.argtypes = [SHORT, SHORT, POINTER(LONG), POINTER(LONG), PSHORT]
Gx6377Initialize = _libraries['libGxSw.so'].Gx6377Initialize
Gx6377Initialize.restype = None
Gx6377Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6377InitializeVisa = _libraries['libGxSw.so'].Gx6377InitializeVisa
Gx6377InitializeVisa.restype = None
Gx6377InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6377Reset = _libraries['libGxSw.so'].Gx6377Reset
Gx6377Reset.restype = None
Gx6377Reset.argtypes = [SHORT, PSHORT]
Gx6377GetBoardSummary = _libraries['libGxSw.so'].Gx6377GetBoardSummary
Gx6377GetBoardSummary.restype = None
Gx6377GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6377RelayClose = _libraries['libGxSw.so'].Gx6377RelayClose
Gx6377RelayClose.restype = None
Gx6377RelayClose.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6377RelayOpen = _libraries['libGxSw.so'].Gx6377RelayOpen
Gx6377RelayOpen.restype = None
Gx6377RelayOpen.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6377RelayGetChannel = _libraries['libGxSw.so'].Gx6377RelayGetChannel
Gx6377RelayGetChannel.restype = None
Gx6377RelayGetChannel.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx6377RelayGetChannels = _libraries['libGxSw.so'].Gx6377RelayGetChannels
Gx6377RelayGetChannels.restype = None
Gx6377RelayGetChannels.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx6377RelaySetChannels = _libraries['libGxSw.so'].Gx6377RelaySetChannels
Gx6377RelaySetChannels.restype = None
Gx6377RelaySetChannels.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx6377MatrixClose = _libraries['libGxSw.so'].Gx6377MatrixClose
Gx6377MatrixClose.restype = None
Gx6377MatrixClose.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6377MatrixOpen = _libraries['libGxSw.so'].Gx6377MatrixOpen
Gx6377MatrixOpen.restype = None
Gx6377MatrixOpen.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6377MatrixGetChannel = _libraries['libGxSw.so'].Gx6377MatrixGetChannel
Gx6377MatrixGetChannel.restype = None
Gx6377MatrixGetChannel.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx6377MatrixSetRow = _libraries['libGxSw.so'].Gx6377MatrixSetRow
Gx6377MatrixSetRow.restype = None
Gx6377MatrixSetRow.argtypes = [SHORT, SHORT, SHORT, DWORD, PSHORT]
Gx6377MatrixGetRow = _libraries['libGxSw.so'].Gx6377MatrixGetRow
Gx6377MatrixGetRow.restype = None
Gx6377MatrixGetRow.argtypes = [SHORT, SHORT, SHORT, POINTER(DWORD), PSHORT]
Gx6377MatrixSetConfiguration = _libraries['libGxSw.so'].Gx6377MatrixSetConfiguration
Gx6377MatrixSetConfiguration.restype = None
Gx6377MatrixSetConfiguration.argtypes = [SHORT, SHORT, PSHORT]
Gx6377MatrixGetConfiguration = _libraries['libGxSw.so'].Gx6377MatrixGetConfiguration
Gx6377MatrixGetConfiguration.restype = None
Gx6377MatrixGetConfiguration.argtypes = [SHORT, PSHORT, PSHORT]
Gx6384Initialize = _libraries['libGxSw.so'].Gx6384Initialize
Gx6384Initialize.restype = None
Gx6384Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6384InitializeVisa = _libraries['libGxSw.so'].Gx6384InitializeVisa
Gx6384InitializeVisa.restype = None
Gx6384InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6384Reset = _libraries['libGxSw.so'].Gx6384Reset
Gx6384Reset.restype = None
Gx6384Reset.argtypes = [SHORT, PSHORT]
Gx6384GetBoardSummary = _libraries['libGxSw.so'].Gx6384GetBoardSummary
Gx6384GetBoardSummary.restype = None
Gx6384GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6384ResetGroup = _libraries['libGxSw.so'].Gx6384ResetGroup
Gx6384ResetGroup.restype = None
Gx6384ResetGroup.argtypes = [SHORT, SHORT, PSHORT]
Gx6384Close = _libraries['libGxSw.so'].Gx6384Close
Gx6384Close.restype = None
Gx6384Close.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6384Open = _libraries['libGxSw.so'].Gx6384Open
Gx6384Open.restype = None
Gx6384Open.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6384GetChannel = _libraries['libGxSw.so'].Gx6384GetChannel
Gx6384GetChannel.restype = None
Gx6384GetChannel.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx6384SetGroupRow32Columns = _libraries['libGxSw.so'].Gx6384SetGroupRow32Columns
Gx6384SetGroupRow32Columns.restype = None
Gx6384SetGroupRow32Columns.argtypes = [SHORT, SHORT, SHORT, DWORD, PSHORT]
Gx6384GetGroupRow32Columns = _libraries['libGxSw.so'].Gx6384GetGroupRow32Columns
Gx6384GetGroupRow32Columns.restype = None
Gx6384GetGroupRow32Columns.argtypes = [SHORT, SHORT, SHORT, POINTER(DWORD), PSHORT]
Gx6384SetGroupRow64Columns = _libraries['libGxSw.so'].Gx6384SetGroupRow64Columns
Gx6384SetGroupRow64Columns.restype = None
Gx6384SetGroupRow64Columns.argtypes = [SHORT, SHORT, DWORD, DWORD, PSHORT]
Gx6384GetGroupRow64Columns = _libraries['libGxSw.so'].Gx6384GetGroupRow64Columns
Gx6384GetGroupRow64Columns.restype = None
Gx6384GetGroupRow64Columns.argtypes = [SHORT, SHORT, POINTER(DWORD), POINTER(DWORD), PSHORT]
Gx6384SetGroupsConfiguration = _libraries['libGxSw.so'].Gx6384SetGroupsConfiguration
Gx6384SetGroupsConfiguration.restype = None
Gx6384SetGroupsConfiguration.argtypes = [SHORT, SHORT, PSHORT]
Gx6384GetGroupsConfiguration = _libraries['libGxSw.so'].Gx6384GetGroupsConfiguration
Gx6384GetGroupsConfiguration.restype = None
Gx6384GetGroupsConfiguration.argtypes = [SHORT, PSHORT, PSHORT]
Gx6384SwitchCyclesReport = _libraries['libGxSw.so'].Gx6384SwitchCyclesReport
Gx6384SwitchCyclesReport.restype = None
Gx6384SwitchCyclesReport.argtypes = [SHORT, PCSTR, PSHORT]
Gx6616Initialize = _libraries['libGxSw.so'].Gx6616Initialize
Gx6616Initialize.restype = None
Gx6616Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx6616InitializeVisa = _libraries['libGxSw.so'].Gx6616InitializeVisa
Gx6616InitializeVisa.restype = None
Gx6616InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx6616Reset = _libraries['libGxSw.so'].Gx6616Reset
Gx6616Reset.restype = None
Gx6616Reset.argtypes = [SHORT, PSHORT]
Gx6616GetBoardSummary = _libraries['libGxSw.so'].Gx6616GetBoardSummary
Gx6616GetBoardSummary.restype = None
Gx6616GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6616Close = _libraries['libGxSw.so'].Gx6616Close
Gx6616Close.restype = None
Gx6616Close.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6616Open = _libraries['libGxSw.so'].Gx6616Open
Gx6616Open.restype = None
Gx6616Open.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6616GetChannel = _libraries['libGxSw.so'].Gx6616GetChannel
Gx6616GetChannel.restype = None
Gx6616GetChannel.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx6616SetRow = _libraries['libGxSw.so'].Gx6616SetRow
Gx6616SetRow.restype = None
Gx6616SetRow.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx6616GetRow = _libraries['libGxSw.so'].Gx6616GetRow
Gx6616GetRow.restype = None
Gx6616GetRow.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx6616BIT = _libraries['libGxSw.so'].Gx6616BIT
Gx6616BIT.restype = None
Gx6616BIT.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx6616BITSetMode = _libraries['libGxSw.so'].Gx6616BITSetMode
Gx6616BITSetMode.restype = None
Gx6616BITSetMode.argtypes = [SHORT, SHORT, PSHORT]
__all__ = ['Gx6325Initialize', 'Gx6138Reset', 'BYTE',
           'GX6315_CHANNEL_FIRST_HIGH_CURRENT', 'GX6021_GROUP_FIRST',
           'GT_LVRT_UNSUPPORTED', 'GX6264_RELAY_FP2',
           'GXSW_INVALID_RELAY_CYCLES_ARRAY_SIZE', 'Gx6338Open',
           'Gx6325GetGroupChannels', 'Gx6021ConnectChannels',
           'GX6192_MUX_MODE_SINGLE_CONNECTION', 'GXSW_INVALID_BUS',
           'Gx6616GetBoardSummary', 'PSTR', 'GX6256_BIT_MODE_RTM',
           'Gx6377MatrixGetConfiguration', 'Gx6384SwitchCyclesReport',
           'Gx6377RelayOpen', 'Gx6062SetGroupRelays',
           'GXSW_INVALID_SIGNAL_TYPE', 'GT_ERROR_FILE_NOT_EXIST',
           'GXSW_INVALID_NUMBER_OF_RELAYS', 'GT_EVENT_WAIT_TIMEOUT',
           'Gx6196SendReceiveModule', 'Gx6616Close',
           'GX6062_CONNECT_MAKE_BEFORE_BREAK', 'Gx6325GroupReset',
           'Gx6384Reset', 'Gx6021GetGroupRelays',
           'GX6315_RELAY_TYPE_HIGH_CURRENT',
           'GX6264_BUS_DIFFERENTIAL', 'Gx6138GetChannel',
           'GX6062_DISCONNECT_BREAKALL',
           'Gx6021ConnectGroupToExternalCoax',
           'GX6264_GROUP_MODE_SCANNER', 'Gx6616GetRow',
           'GX6021_DISCONNECT_BREAK',
           'GX6256_SELECTOR_MODE_MATRIX_AND_EXTERNAL',
           'Gx6384GetChannel', 'GX6256_PATH_PRIMARY',
           'Gx6264GetBusMode', 'Gx6616Reset', 'GX6264_BUS_X0',
           'GX6264_BUS_X1', 'GX6021_GROUP_RELAY5',
           'GX6021_GROUP_RELAY4', 'GX6021_GROUP_RELAY1',
           'GX6021_GROUP_RELAY3', 'GX6021_GROUP_RELAY2', 'INT',
           'GX6256_SELECTOR_MODE_MATRIX_ONLY',
           'GT_VISA_OPENDEFAULTRM_ERROR', 'GXSW_INVALID_RELAY_NUMBER',
           'GX6021_CHANNEL_FIRST', 'GXSW_INVALID_BLOCK',
           'Gx6021SetGroupRelays', 'GxSWGetDriverSummary',
           'GX6115_CHANNEL_FIRST_DRIVER',
           'GX6315_CHANNEL_FIRST_DRIVER', 'Gx6196WritePio',
           'GX6192_SELECTOR_MODE_MATRIX_AND_DIGITAL',
           'GX6256_SELECTOR_MODE_MATRIX_ISOLATED',
           'GX6062_DISCONNECT_BREAK', 'GXSW_INVALID_DAISY_CHAIN_MODE',
           'Gx6115Initialize',
           'GX6384_CONFIG_AS_ONE_GROUP_64_CHANNELS',
           'GX6264_SECTION0', 'GX6264_SECTION1', 'Gx6062Initialize',
           'Gx6264GetRelayType', 'GX6062_DAISY_CHAIN_VIA_LAST_GROUP',
           'GXSW_STATE_CLOSE', 'GT_SLOT_NOT_CONFIG', 'GT_WRONG_BOARD',
           'Gx6062GetChannel', 'GXSW_INVALID_RELAY',
           'GT_VISA_LOAD_DLL_ERROR', 'GX6192_INPUT_1',
           'GX6192_INPUT_0', 'GX6192_INPUT_3', 'GX6192_INPUT_2',
           'GX6192_INPUT_5', 'GX6192_INPUT_4', 'GX6192_INPUT_7',
           'GX6192_INPUT_6', 'GX6192_INPUT_9', 'GX6192_INPUT_8',
           'GT_VISA_VIIN_ERROR', 'Gx6138SetChannels',
           'GX6377_RELAY_TYPE_FORM_A', 'GX6377_RELAY_TYPE_FORM_C',
           'Gx6196Reset', 'GT_CANT_OPEN_HW', 'Gx6377MatrixOpen',
           'GX6384_ROW_4', 'GX6384_ROW_5',
           'GX6192_SELECTOR_MODE_DIGITAL_ONLY', 'GX6384_ROW_1',
           'GX6384_ROW_2', 'GX6384_ROW_3', 'GX6384_ROW_0',
           'Gx6384GetBoardSummary', 'GX6256_BLOCK_BOARD',
           'GXSW_INVALID_CONFIGURATION', 'Gx6325SetGroupChannels',
           'Gx6377GetBoardSummary', 'Gx6264ResetBus',
           'GX6377_FORM_C_FIRST_CHANNEL', 'GX6125_CHANNEL_LAST',
           'Gx6264RemoveBus', 'PSHORT', 'GT_EVENT_WAIT_ERROR',
           'GT_ERR_MODE_NOT_SUPPORTED_BY_SLOT',
           'Gx6021GetDaisyChainMode', 'GT_EVENT_ENABLE_FAILED',
           'Gx6196GetPio', 'Gx6021DisconnectGroupToExternalCoax',
           'GXSW_BIT_CLOSE_OPEN', 'Gx6115Reset',
           'GX6377_HIGH_CURRENT_FIRST_CHANNEL', 'GX6256_INPUT_14',
           'GX6256_INPUT_15', 'GX6256_INPUT_10', 'GX6256_INPUT_11',
           'GX6256_INPUT_12', 'GX6384_FIRST_COLUMN',
           'GX6062_CONNECT_BREAKALL_BEFORE_MAKE',
           'GX6377_FORM_C_LAST_CHANNEL', 'Gx6338SetGroupChannels',
           'Gx6377MatrixClose', 'Gx6196SetPioOutputEnable',
           'Gx6264RemoveChannel', 'GX6315_RELAY_TYPE_DRIVER',
           'Gx6315GetGroupChannels', 'GX6264_BUS_NOT_IN_USE',
           'GX6021_DISCONNECT_BREAKALL', 'LONG', 'GX6264_GROUP_H',
           'Gx6338GetGroupChannels', 'GT_UNABLE_CREATE_PANEL',
           'GX6264_GROUP_B', 'GX6264_GROUP_C', 'GX6264_GROUP_D',
           'GX6264_GROUP_E', 'GX6264_GROUP_F', 'GX6264_GROUP_G',
           'Gx6115GetBoardSummary', 'GT_UNABLE_ALLOC_MEMORY',
           'GX6062_CONNECT_MAKE', 'Gx6616BIT', 'Gx6616Initialize',
           'Gx6062Reset', 'GX6062_CHANNEL_LAST', 'Gx6377RelayClose',
           'GXSW_EEPROM_CHECKSUM_INVALID', 'GXSW_INVALID_GROUP',
           'Gx6138Open', 'GT_NOT_IN_CALIBRATION_MODE',
           'GX6256_INPUT_8', 'GX6256_INPUT_9', 'GX6256_INPUT_6',
           'GX6256_INPUT_7', 'GX6256_INPUT_4', 'GX6256_INPUT_5',
           'GX6256_INPUT_2', 'GX6256_INPUT_3', 'GX6256_INPUT_0',
           'GX6256_INPUT_1', 'Gx6062Close', 'Gx6115Close',
           'Gx6196GetBoardSummary',
           'GXSW_ERROR_OVER_LIMIT_RELAY_REPLACEMENT',
           'Gx6384GetGroupRow64Columns', 'GXSW_INVALID_CHANNEL',
           'GX6256_GROUP_H', 'Gx6338GetBoardSummary',
           'GX6062_DAISY_CHAIN_VIA_FIRST_GROUP', 'Gx6264Initialize',
           'Gt_EventCallback', 'Gx6021GetChannel',
           'GT_VISA_GETATTRIBUTE_ERROR', 'PDOUBLE',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GTSW_ERROR_CLOSED_LOOP', 'GX6125_CHANNEL_FIRST',
           'GX6338_GROUP_B', 'GX6338_GROUP_C', 'Gx6616BITSetMode',
           'GX6338_GROUP_A', 'GX6256_RESET_ALL', 'GX6616_ROW_0',
           'GX6616_ROW_1', 'Gx6315GetBoardSummary', 'UINT',
           'GT_FILE_EXTENSION_NOT_SUPPORTED',
           'GT_INVALID_CALIBRATION_TIME_STAMP',
           'GX6062_GROUP_RELAY_TO_EXTERNAL_COAX',
           'Gx6062ConnectGroupToExternalCoax', 'GX6315_GROUP_A',
           'CHAR', 'GX6138_CHANNEL_LAST', 'Gx6264InitializeVisa',
           'Gx6021Close', 'WORD', 'GXSW_REPORT_FORMAT_TXT',
           'GX6021_CONNECT_BREAK_BEFORE_MAKE', 'GX6315_GROUP_C',
           'GX6315_GROUP_B', 'GX6325_GROUP_A', 'GX6325_GROUP_B',
           'GX6325_GROUP_C', 'Gx6325GetChannel',
           'GX6377_MATRIX_CONFIG_ONE_GROUP_2X32',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GXSW_BIT_CLOSE_COLUMN',
           'Gx6196ReadPio', 'Gx6384Initialize',
           'GXSW_SIMULATION_INI_FILE_READ_ERROR', 'Gx6021Initialize',
           'Gx6264ConnectBus', 'GXSW_ERROR_CLOSED_RELAYS_OVER_LIMIT',
           'GT_INVALID_ERROR', 'GX6021_CONNECT_MAKE',
           'GX6021_DAISY_CHAIN_VIA_LAST_GROUP',
           'Gx6264GetGroupChannels', 'GXSW_PANEL_MODELESS',
           'GX6138_CHANNEL_FIRST',
           'GX6616_BIT_MODE_ADAPTER_DETECTION',
           'GXSW_ERROR_SET_RELAYS_TIMEOUT', 'GT_ERR_CHECKSUM',
           'GX6021_DAISY_CHAIN_VIA_FIRST_AND_LAST_GROUP',
           'GT_INVALID_SLOT', 'GT_UNABLE_TO_GETTIMER',
           'GT_SYNC_TIMEOUT', 'LPLONG', 'DWORD', 'GX6616_GROUP_A',
           'GX6616_GROUP_F', 'GX6616_GROUP_E', 'GX6616_GROUP_D',
           'Gx6315Open', 'Gx6377MatrixSetConfiguration',
           'Gx6325Close', 'GX6192_MUX_MODE_MULTI_CONNECTION',
           'Gx6062GetGroupRelays', 'GX6256_BIT_MODE_MATRIX',
           'Gx6377RelayGetChannel', 'Gx6616InitializeVisa',
           'GX6021_GROUP_RELAY_TO_NEXT_GROUP', 'Gx6315GetChannel',
           'GX6115_RELAY_TYPE_HIGH_CURRENT', 'Gx6264GetGroupMode',
           'Gx6384ResetGroup', 'Gx6196Open', 'Gx6338InitializeVisa',
           'PBYTE', 'GXSW_BIT_PARTIAL', 'Gx6062ConnectChannels',
           'Gx6062Open', 'PWORD', 'GX6256_INPUT_13',
           'GX6377_MATRIX_FIRST_COLUMN', 'GT_LICENSE',
           'GX6021_GROUP_LAST', 'Gx6325Reset', 'GX6384_GROUP_B',
           'GX6384_GROUP_A', 'GXSW_INVALID_COLUMN',
           'Gx6021InitializeVisa', 'GT_UNABLE_REGISTER_DEVICE',
           'GX6384_LAST_COLUMN_CONFIG_AS_ONE_GROUP',
           'GxSWGetErrorString', 'Gx6264SetBusMode',
           'GXSW_BIT_SWITCH_OTHER', 'Gx6196InitializeVisa',
           'GXSW_STATE_OPEN', 'GX6377_GROUP_A',
           'Gx6384InitializeVisa', 'GX6021_CONNECT_MAKE_BEFORE_BREAK',
           'GX6377_GROUP_B', 'Gx6125Close',
           'GX6062_GROUP_RELAY_TO_NEXT_GROUP',
           'GX6264_GROUP_MODE_MATRIX',
           'GX6264_BUS_SINGLE_ENDED_LO_TO_GROUP_LO',
           'GX6115_CHANNEL_FIRST_HIGH_CURRENT',
           'Gx6196GetPioOutputEnable',
           'GX6315_CHANNEL_LAST_HIGH_CURRENT',
           'GX6384_CONFIG_AS_TWO_GROUPS_32_CHANNELS',
           'GXSW_INVALID_RELAYS_CYCLES_LIMIT', 'GX6338_CHANNEL_FIRST',
           'GX6256_MUX_MODE_MULTI_CONNECTION', 'GX6256_INTERRUPT_2',
           'GX6256_INTERRUPT_1', 'GX6256_INTERRUPT_0',
           'GX6264_BUS_SINGLE_ENDED_LO', 'Gx6616GetChannel',
           'Gx6315InitializeVisa', 'GX6115_CHANNEL_LAST_HIGH_CURRENT',
           'SHORT', 'GX6256_BIT_MODE_ALL', 'Gx6021Open',
           'GX6062_GROUP_LAST', 'Gx6338GetChannel', 'Gx6264Reset',
           'GT_INVALID_PARAMETER', 'Gx6264RemoveSectionsBus',
           'GX6315_CHANNEL_LAST_DRIVER', 'GX6264_CHANNEL_LAST',
           'Gx6384Close', 'Gx6377MatrixSetRow', 'Gx6138Initialize',
           'GX6264_RELAY_MILITARY412', 'GX6062_DAISY_CHAIN_NONE',
           'Gx6338Initialize', 'GX6256_BIT_MODE_MUX', 'Gx6115Open',
           'Gx6264GetGroup', 'Gx6062GetDaisyChainMode',
           'Gx6196GetChannel', 'Gx6125Open', 'Gx6196Close',
           'Gx6062DisconnectGroupToExternalCoax',
           'GX6062_CHANNEL_FIRST', 'Gx6125GetChannels',
           'GX6264_GROUP_A', 'GXSW_INVALID_INPUT', 'GT_SYNC_CREATE',
           'Gx6264ResetSection', 'GXSW_BIT_OK', 'Gx6115GetChannel',
           'LPDWORD', 'Gx6264ConnectChannel', 'GX6192_RESET_ALL',
           'Gx6138GetBoardSummary',
           'GX6377_MATRIX_CONFIG_TWO_GROUPS_2X16',
           'GT_NOT_CALIBRATED', 'GX6264_BUS_SINGLE_ENDED_HI',
           'GT_BOARD_INVALID_EEPROM', 'Gx6264GetSectionsBus',
           'Gx6125GetBoardSummary', 'Gx6384Open',
           'GX6021_GROUP_RELAY_TO_EXTERNAL_COAX', 'GX6616_GROUP_C',
           'GXSW_REPORT_FORMAT_CSV', 'Gx6062InitializeVisa',
           'GX6616_GROUP_B', 'GT_NOT_GEOTEST_BOARD',
           'GX6021_DAISY_CHAIN_VIA_FIRST_GROUP',
           'GT_ERR_DMA_MEM_FREE', 'GX6377_FORM_A_FIRST_CHANNEL',
           'GX6256_BLOCK_SR', 'Gx6384SetGroupRow64Columns',
           'GX6021_DAISY_CHAIN_NONE', 'GX6264_RELAY_REED',
           'GX6256_GROUP_C', 'GX6256_GROUP_B', 'GX6256_GROUP_A',
           'GX6256_GROUP_G', 'GX6256_GROUP_F', 'GX6256_GROUP_E',
           'GX6256_GROUP_D', 'GX6256_GROUP_K', 'GX6256_GROUP_J',
           'GX6256_GROUP_I', 'GXSW_ERROR_BIT_STILL_RUNNING',
           'GX6256_GROUP_O', 'GX6256_GROUP_N', 'GX6256_GROUP_M',
           'GX6256_GROUP_L', 'GX6256_GROUP_P',
           'GX6256_PATH_SECONDARY',
           'GX6384_LAST_COLUMN_CONFIG_AS_TWO_GROUPS',
           'GXSW_PANEL_MODAL', 'GX6192_GROUP_L', 'GX6192_GROUP_M',
           'GX6192_GROUP_N', 'GX6192_GROUP_O', 'GX6192_GROUP_H',
           'GX6192_GROUP_I', 'GX6192_GROUP_J', 'GX6192_GROUP_K',
           'GX6192_GROUP_D', 'GX6192_GROUP_E', 'GX6192_GROUP_F',
           'GX6192_GROUP_G', 'GX6192_GROUP_A', 'GX6192_GROUP_B',
           'GX6192_GROUP_C', 'GX6325_CHANNEL_LAST',
           'Gx6021DisconnectChannels', 'Gx6384GetGroupsConfiguration',
           'GT_NOT_PCI_BOARD', 'GX6192_GROUP_P', 'Gx6138GetChannels',
           'Gx6125Reset', 'GX6377_ROW_0', 'GX6377_ROW_1',
           'Gx6377Reset', 'PDWORD', 'GT_NO_ERROR',
           'Gx6138InitializeVisa', 'Gx6115SetChannels',
           'Gx6125GetChannel', 'Gx6338Reset', 'GT_INVALID_STRLEN',
           'Gx6377MatrixGetRow', 'Gx6338Close', 'GT_BOARD_NOT_EXIST',
           'Gx6325InitializeVisa', 'GX6616_COLUMN_LAST',
           'GT_NOT_PXI_BOARD', 'Gx6338GroupReset',
           'GX6115_CHANNEL_LAST_DRIVER', 'Gx6616Open', 'DOUBLE',
           'GX6325_CHANNEL_FIRST', 'Gx6377Initialize', 'HWND',
           'Gx6315Initialize', 'GX6377_FORM_A_LAST_CHANNEL', 'PLONG',
           'GX6256_BLOCK_RTM', 'GX6115_RELAY_TYPE_DRIVER',
           'GX6264_BUS_Y1', 'GX6264_BUS_Y0',
           'GXSW_BIT_ADAPTOR_NOT_CONNECTED', 'ULONG', 'Gx6315Reset',
           'GX6062_CONNECT_BREAK_BEFORE_MAKE',
           'GT_DMA_MEM_ALLOC_FAILED',
           'GX6616_BIT_MODE_NO_ADAPTER_DETECTION', 'PBOOL',
           'Gx6062GetBoardSummary', 'Gx6384GetGroupRow32Columns',
           'Gx6125InitializeVisa', 'GX6338_CHANNEL_LAST',
           'GX6256_MUX_MODE_SINGLE_CONNECTION', 'Gx6325Open',
           'GT_VISA_OPEN_ERROR', 'PULONG', 'Gx6115InitializeVisa',
           'GXSW_INVALID_ROW', 'GT_INVALID_MODE', 'PCSTR',
           'GT_VISA_MEMMAP_ERROR', 'GX6062_GROUP_RELAY1',
           'GX6062_GROUP_RELAY2', 'GX6062_GROUP_RELAY3',
           'GX6062_GROUP_RELAY4', 'GX6062_GROUP_RELAY5',
           'GXSW_EEPROM_BUSY_TIMEOUT', 'GX6256_SELECTOR_MODE_NONE',
           'Gx6377RelayGetChannels', 'Gx6264ConnectSectionsBus',
           'Gx6264ResetGroup', 'Gx6196Initialize',
           'Gx6021GetBoardSummary',
           'GX6377_HIGH_CURRENT_LAST_CHANNEL', 'Gx6315Close',
           'GXSW_INVALID_SECTION', 'GX6192_SELECTOR_MODE_MATRIX_ONLY',
           'GX6264_CHANNEL_FIRST', 'Gx6264SetGroupChannels',
           'Gx6315SetGroupChannels', 'Gx6264SetGroupMode',
           'GXSW_BIT_COMPARATOR', 'GX6377_RELAY_TYPE_HIGH_CURRENT',
           'Gx6384SetGroupRow32Columns', 'Gx6021Reset',
           'Gx6125SetChannels', 'BOOL', 'Gx6125Initialize',
           'GX6264_CONNECT_COMBINED', 'Gx6062SetDaisyChainMode',
           'GT_UNABLE_TO_OPEN_FILE', 'GXSW_INVALID_PATH',
           'Gx6377InitializeVisa',
           'GX6062_DAISY_CHAIN_VIA_FIRST_AND_LAST_GROUP',
           'GX6264_CONNECT_ONLY', 'GXSW_INVALID_ERROR',
           'GT_PARAMETER_OUT_OF_RANGE', 'GXSW_INVALID_RELAY_TYPE',
           'GX6616_COLUMN_FIRST', 'Gx6377RelaySetChannels',
           'GX6021_CHANNEL_LAST', 'Gx6377MatrixGetChannel',
           'Gx6021SetDaisyChainMode', 'Gx6264GetBoardSummary',
           'GX6264_RELAY_MILITARY172',
           'GX6021_CONNECT_BREAKALL_BEFORE_MAKE', 'GX6192_INPUT_15',
           'GX6192_INPUT_14', 'GX6192_INPUT_11', 'GX6192_INPUT_10',
           'GX6192_INPUT_13', 'GX6192_INPUT_12',
           'GT_EVENT_DISABLE_FAILED', 'GT_ERR_DMA_MEM_UN_MAP',
           'GT_INVALID_CHASSIS_NUMBER', 'Gx6616SetRow',
           'Gx6384SetGroupsConfiguration',
           'GX6192_SELECTOR_MODE_NONE', 'Gx6325GetBoardSummary',
           'PVOID', 'GXSW_INVALID_GROUP_MODE', 'GX6062_GROUP_FIRST',
           'Gx6062DisconnectChannels',
           'GX6256_SELECTOR_MODE_EXTERNAL_ONLY', 'Gx6138Close',
           'GT_INVALID_HANDLE', 'Gx6115GetChannels']
