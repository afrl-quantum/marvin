from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libGxPio.so'] = CDLL('libGxPio.so')


# VOID = void # alias
GX5641_PXI_TRIGGER_LINE7 = 7 # Variable c_int '7'
GX5641_PXI_TRIGGER_LINE6 = 6 # Variable c_int '6'
GX5641_PXI_TRIGGER_LINE5 = 5 # Variable c_int '5'
GX5641_PXI_TRIGGER_LINE4 = 4 # Variable c_int '4'
GX5641_PXI_TRIGGER_LINE3 = 3 # Variable c_int '3'
GX5733_DIGITAL_PORT_IO = 5714 # Variable c_int '5714'
GX5641_PXI_TRIGGER_LINE1 = 1 # Variable c_int '1'
GX5641_PXI_TRIGGER_LINE0 = 0 # Variable c_int '0'
GX5733_MAX_CLOCK_DIVIDER = 268435456 # Variable c_int '268435456'
GX5731_MODULE_INTERNAL_STROBE_NOT_CONNECTED = 0 # Variable c_int '0'
GX5641_PXI_TRIGGER_LINE2 = 2 # Variable c_int '2'
GX5733_RS422_TTL_BIDIRECTIONAL_CONVERTER = 5712 # Variable c_int '5712'
GX5731_PORT_IN_ONLY = 5715 # Variable c_int '5715'
GX5641_CHANNEL_CONVERT_DIFFERENTIAL_TO_TTL = 0 # Variable c_int '0'
GX5731_MODULE_GROUP0 = 0 # Variable c_int '0'
GX5731_MODULE_GROUP1 = 1 # Variable c_int '1'
GXPIO_INVALID_STROBE_POLARITY = -55 # Variable c_int '-0x00000000000000037'
GX5733_INTERNAL_CLOCK0_T0_PXI_CLOCK_10MHZ = 2 # Variable c_int '2'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER0 = 7 # Variable c_int '7'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER1 = 8 # Variable c_int '8'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER2 = 9 # Variable c_int '9'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER3 = 10 # Variable c_int '10'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER4 = 11 # Variable c_int '11'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER5 = 12 # Variable c_int '12'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER6 = 13 # Variable c_int '13'
GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER7 = 14 # Variable c_int '14'
GXPIO_INVALID_CHANNEL_PORT_DIRECTION = -61 # Variable c_int '-0x0000000000000003d'
GX5732_INTERNAL_CLOCK_T0_USER_LINE4 = 6 # Variable c_int '6'
GX5732_INTERNAL_CLOCK_T0_USER_LINE5 = 7 # Variable c_int '7'
GX5732_INTERNAL_CLOCK_T0_USER_LINE2 = 4 # Variable c_int '4'
GX5732_INTERNAL_CLOCK_T0_USER_LINE3 = 5 # Variable c_int '5'
GX5732_INTERNAL_CLOCK_T0_USER_LINE0 = 2 # Variable c_int '2'
GX5732_INTERNAL_CLOCK_T0_USER_LINE1 = 3 # Variable c_int '3'
GX5733_PORT_HIGH_WORD = 1 # Variable c_int '1'
GX5731_MODULE_TERMINATION_ON = 1 # Variable c_int '1'
GX5642_PXI_TRIGGER_LINE0 = 0 # Variable c_int '0'
GX5733_PORT2 = 2 # Variable c_int '2'
GX5731_EXT_TRIGGER_LINE2 = 2 # Variable c_int '2'
GX5731_EXT_TRIGGER_LINE1 = 1 # Variable c_int '1'
GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN4 = 5 # Variable c_int '5'
GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN5 = 6 # Variable c_int '6'
GXPIO_INVALID_BYTE = -42 # Variable c_int '-0x0000000000000002a'
GX5731_EXT_TRIGGER_LINE0 = 0 # Variable c_int '0'
GX5733_MAX_BUFFER_SIZE = 4096 # Variable c_int '4096'
GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN2 = 3 # Variable c_int '3'
GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN3 = 4 # Variable c_int '4'
GX5731_EXT_TRIGGER_LINE7 = 7 # Variable c_int '7'
GX5642_PXI_TRIGGER_LINE5 = 5 # Variable c_int '5'
GX5642_PXI_TRIGGER_LINE6 = 6 # Variable c_int '6'
GX5642_CHANNEL_OUTPUT_DISABLE = 0 # Variable c_int '0'
GX5642_PXI_TRIGGER_LINE7 = 7 # Variable c_int '7'
GX5733_MODULE_INTERNAL_STROBE_NOT_CONNECTED = 0 # Variable c_int '0'
GX5733_PXI_TRIGGER_LINE1 = 1 # Variable c_int '1'
GX5731_MODULE_OPERATION_PORT_IO = 1 # Variable c_int '1'
GX5733_RS422_PORT_IO = 5709 # Variable c_int '5709'
GXPIO_INVALID_DIRECTION = -58 # Variable c_int '-0x0000000000000003a'
GX5731_MODULE_BUFFER_MODE_HALF_FULL = 1 # Variable c_int '1'
GT_SLOT_NOT_CONFIG = -4 # Variable c_int '-0x00000000000000004'
GT_WRONG_BOARD = -3 # Variable c_int '-0x00000000000000003'
GX5731_MIN_CLOCK_DIVIDER = 1 # Variable c_int '1'
GX5733_MODULE_GROUP0 = 0 # Variable c_int '0'
GX5733_MODULE_GROUP1 = 1 # Variable c_int '1'
GXPIO_MODULE_BUFFER_OVERFLOW = 20 # Variable c_int '20'
GX5733_CLOCK1 = 1 # Variable c_int '1'
GX5733_CLOCK0 = 0 # Variable c_int '0'
GX5731_EXT_TRIGGER_LINE3 = 3 # Variable c_int '3'
GX5642_PXI_TRIGGER_LINE1 = 1 # Variable c_int '1'
GX5642_PXI_TRIGGER_LINE2 = 2 # Variable c_int '2'
GX5642_PXI_TRIGGER_LINE3 = 3 # Variable c_int '3'
GX5642_PXI_TRIGGER_LINE4 = 4 # Variable c_int '4'
GX5731_EXT_TRIGGER_LINE6 = 6 # Variable c_int '6'
GX5731_EXT_TRIGGER_LINE5 = 5 # Variable c_int '5'
GX5731_EXT_TRIGGER_LINE4 = 4 # Variable c_int '4'
GXPIO_INVALID_BIT = -43 # Variable c_int '-0x0000000000000002b'
GX5731_MAX_BUFFER_SIZE = 4096 # Variable c_int '4096'
GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE2 = 4 # Variable c_int '4'
GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE3 = 5 # Variable c_int '5'
GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE0 = 2 # Variable c_int '2'
GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE1 = 3 # Variable c_int '3'
GXPIO_INVALID_CLOCK_SOURCE = -48 # Variable c_int '-0x00000000000000030'
GX5731_MODULE_STATE_RUN = 1 # Variable c_int '1'
GXPIO_INVALID_COUNTER_OR_ALL_TERMINAL_COUNT_AND_CLOCKS = -46 # Variable c_int '-0x0000000000000002e'
GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE4 = 6 # Variable c_int '6'
GX5733_MODULE_OUTPUT_DISABLE = 0 # Variable c_int '0'
GX5731_PORT_LOW_WORD = 0 # Variable c_int '0'
GX5731_PORT_DIRECTION_OUT = 1 # Variable c_int '1'
GX5733_PORT_IN_ONLY = 5715 # Variable c_int '5715'
GX5733_MODULE_STATE_HALT = 0 # Variable c_int '0'
GXPIO_INVALID_CHANNEL_MODE = -60 # Variable c_int '-0x0000000000000003c'
GX5732_TERMINAL_COUNT_OUPUT_COUNTER2 = 2 # Variable c_int '2'
GX5732_TERMINAL_COUNT_OUPUT_COUNTER3 = 3 # Variable c_int '3'
GX5732_TERMINAL_COUNT_OUPUT_COUNTER0 = 0 # Variable c_int '0'
GX5732_TERMINAL_COUNT_OUPUT_COUNTER1 = 1 # Variable c_int '1'
GX5732_COUNTER_GATE_CARRY_COUNTER1 = 1 # Variable c_int '1'
GX5731_DISABLE_INTERNAL_CLOCK = 0 # Variable c_int '0'
GX5733_MODULE_BUFFER_MODE_HALF_FULL = 1 # Variable c_int '1'
GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE5 = 7 # Variable c_int '7'
GX5732_MAX_CLOCK_DIVIDER = 16777216 # Variable c_int '16777216'
GX5731_MODULE_STROBE_POSITIVE_EDGE = 0 # Variable c_int '0'
GX5731_PORT2 = 2 # Variable c_int '2'
GX5731_PORT1 = 1 # Variable c_int '1'
GX5731_PORT0 = 0 # Variable c_int '0'
GX5731_MODULE_DIRECTION_OUTPUT = 1 # Variable c_int '1'
GX5731_PORT6 = 6 # Variable c_int '6'
GX5731_PORT5 = 5 # Variable c_int '5'
GX5731_PORT4 = 4 # Variable c_int '4'
GX5641_CHANNEL_DIFFERENTIAL_PORT = 1 # Variable c_int '1'
GT_INVALID_MODE = -25 # Variable c_int '-0x00000000000000019'
GXPIO_INVALID_WORD = -41 # Variable c_int '-0x00000000000000029'
GX5733_MODULE_MAX_VTHRESHOLD = 30.0 # Variable c_double '3.0e+1'
GT_UNABLE_CREATE_PANEL = -8 # Variable c_int '-0x00000000000000008'
GX5733_INTERNAL_CLOCK0_T0_PCI_CLOCK_33MHZ = 1 # Variable c_int '1'
GXPIO_BUFFER_WRITE_FAIL = -83 # Variable c_int '-0x00000000000000053'
GX5733_MODULE_STROBE_INTERNAL = 0 # Variable c_int '0'
GX5733_MODULE_HANDSHAKE_OUTPUT_DISABLE = 0 # Variable c_int '0'
GX5731_MODULE_DIRECTION_SOURCE_EXTERNAL = 1 # Variable c_int '1'
GX5731_MIN_BUFFER_SIZE = 1 # Variable c_int '1'
GX5732_COUNTER_TO_USER_LINE4 = 6 # Variable c_int '6'
GX5732_COUNTER_TO_USER_LINE5 = 7 # Variable c_int '7'
GX5732_COUNTER_TO_USER_LINE2 = 4 # Variable c_int '4'
GX5732_COUNTER_TO_USER_LINE3 = 5 # Variable c_int '5'
GX5732_COUNTER_TO_USER_LINE0 = 2 # Variable c_int '2'
GX5732_COUNTER_TO_USER_LINE1 = 3 # Variable c_int '3'
GX5731_MODULE_DIRECTION_DIFFERENTIAL_TO_TTL = 0 # Variable c_int '0'
GX5731_MODULE_BUFFER_EMPTY = 0 # Variable c_int '0'
GX5731_MODULE_HANDSHAKE_OUTPUT_DISABLE = 0 # Variable c_int '0'
GX5731_NO_MODULE_INSTALLED = 5700 # Variable c_int '5700'
GX5733_PORT_DIRECTION_OUT = 1 # Variable c_int '1'
GX5731_MODULE_MIN_STROBE_WIDTH = 50 # Variable c_int '50'
GX5733_DIGITAL_INPUT_LATCH = 5701 # Variable c_int '5701'
GX5733_MODULE_MIN_VTHRESHOLD = -30.0 # Variable c_double '-3.0e+1'
GX5733_MODULE_STATE_RUN = 1 # Variable c_int '1'
GX5731_ENABLE_INTERNAL_CLOCK = 1 # Variable c_int '1'
GX5642_FIRST_CHANNEL = 0 # Variable c_int '0'
GX5731_RS422_TTL_BIDIRECTIONAL_CONVERTER = 5712 # Variable c_int '5712'
GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER5 = 5 # Variable c_int '5'
GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER4 = 4 # Variable c_int '4'
GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER7 = 7 # Variable c_int '7'
GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER6 = 6 # Variable c_int '6'
GX5731_MODULE_OUTPUT_ENABLE = 1 # Variable c_int '1'
GX5732_TERMINAL_COUNT_POS_PULSE = 0 # Variable c_int '0'
GXPIO_INVALID_DIVIDER = -52 # Variable c_int '-0x00000000000000034'
GT_UNABLE_ALLOC_DEVICE_RESOURCE = -6 # Variable c_int '-0x00000000000000006'
GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK1 = 2 # Variable c_int '2'
GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK0 = 1 # Variable c_int '1'
GXPIO_INVALID_GATE_SOURCE = -51 # Variable c_int '-0x00000000000000033'
GX5731_MODULE_HANDSHAKE_OUTPUT_ENABLE = 1 # Variable c_int '1'
GX5642_CHANNEL_PORT_INPUT = 0 # Variable c_int '0'
GX5731_INTERNAL_CLOCK1_T0_PXI_CLOCK_10MHZ = 2 # Variable c_int '2'
GX5733_PORT_DIRECTION_IN = 0 # Variable c_int '0'
GX5733_INTERNAL_CLOCK0_NOT_CONNECTED = 0 # Variable c_int '0'
GXPIO_INVALID_PORT = -40 # Variable c_int '-0x00000000000000028'
GXPIO_INVALID_CLOCK_INTERNAL_SOURCE = -50 # Variable c_int '-0x00000000000000032'
GX5733_LVDS_TTL_BIDIRECTIONAL_CONVERTER = 5711 # Variable c_int '5711'
GX5731_DIGITAL_POWER_OUTPUT_LATCH = 5704 # Variable c_int '5704'
GT_ERR_FUNCTION_NOT_SUPPORTED = -13 # Variable c_int '-0x0000000000000000d'
GT_INVALID_ERROR = -20 # Variable c_int '-0x00000000000000014'
GX5731_INTERNAL_CLOCK1_T0_CLOCK_IN1 = 0 # Variable c_int '0'
GX5733_MODULE_DIRECTION_SOURCE_EXTERNAL = 1 # Variable c_int '1'
GX5731_INTERNAL_CLOCK0_T0_PXI_CLOCK_10MHZ = 2 # Variable c_int '2'
GX5641_CHANNEL_MODE_CONVERSION = 0 # Variable c_int '0'
GX5732_COUNTER2 = 2 # Variable c_int '2'
GX5732_COUNTER3 = 3 # Variable c_int '3'
GX5732_COUNTER0 = 0 # Variable c_int '0'
GX5732_COUNTER1 = 1 # Variable c_int '1'
GX5642_CHANNEL_CONVERT_DIFFERENTIAL_TO_TTL = 0 # Variable c_int '0'
GXPIO_COUNTER_PORT_NOT_INPUT = -80 # Variable c_int '-0x00000000000000050'
GX5733_MODULE_INTERNAL_STROBE_T0_CLOCK1 = 2 # Variable c_int '2'
GX5733_MODULE_INTERNAL_STROBE_T0_CLOCK0 = 1 # Variable c_int '1'
GT_INVALID_SLOT = -22 # Variable c_int '-0x00000000000000016'
GT_UNABLE_TO_GETTIMER = -9 # Variable c_int '-0x00000000000000009'
GX5731_DIGITAL_INPUT_LATCH = 5701 # Variable c_int '5701'
GX5731_MODULE_DIRECTION_INPUT = 0 # Variable c_int '0'
GX5732_COUNTER_GATE_ENABLE_ALWAYS = 0 # Variable c_int '0'
GX5732_PORT0 = 0 # Variable c_int '0'
GX5732_PORT1 = 1 # Variable c_int '1'
GX5732_PORT2 = 2 # Variable c_int '2'
GX5732_PORT3 = 3 # Variable c_int '3'
GX5732_PORT4 = 4 # Variable c_int '4'
GX5732_PORT5 = 5 # Variable c_int '5'
GX5732_PORT6 = 6 # Variable c_int '6'
GXPIO_INVALID_PXI_TRIGGER_LINE = -64 # Variable c_int '-0x00000000000000040'
GX5732_INTERNAL_CLOCK_T0_PCI_CLOCK_33MHZ = 0 # Variable c_int '0'
GX5733_PORT_BYTE1 = 1 # Variable c_int '1'
GX5733_PORT_BYTE0 = 0 # Variable c_int '0'
GX5733_PORT_BYTE3 = 3 # Variable c_int '3'
GX5733_PORT_BYTE2 = 2 # Variable c_int '2'
GX5641_GROUP0 = 0 # Variable c_int '0'
GX5641_GROUP1 = 1 # Variable c_int '1'
GX5642_CHANNEL_MODE_STATIC_IO = 1 # Variable c_int '1'
GX5731_MODULE_STROBE_EXTERNAL = 1 # Variable c_int '1'
GT_UNABLE_REGISTER_DEVICE = -5 # Variable c_int '-0x00000000000000005'
GX5731_LVDS_TTL_BIDIRECTIONAL_CONVERTER = 5711 # Variable c_int '5711'
GX5733_PORT1 = 1 # Variable c_int '1'
GX5733_PORT0 = 0 # Variable c_int '0'
GX5733_PORT3 = 3 # Variable c_int '3'
GX5732_TERMINAL_COUNT_NEG_PULSE = 1 # Variable c_int '1'
GX5733_PXI_TRIGGER_LINE5 = 5 # Variable c_int '5'
GX5733_PXI_TRIGGER_LINE4 = 4 # Variable c_int '4'
GX5733_PXI_TRIGGER_LINE7 = 7 # Variable c_int '7'
GX5733_PXI_TRIGGER_LINE6 = 6 # Variable c_int '6'
GX5732_NEGATIVE_EDGE = 1 # Variable c_int '1'
GX5733_PXI_TRIGGER_LINE0 = 0 # Variable c_int '0'
GX5733_PXI_TRIGGER_LINE3 = 3 # Variable c_int '3'
GX5733_PXI_TRIGGER_LINE2 = 2 # Variable c_int '2'
GX5733_NO_MODULE_INSTALLED = 5700 # Variable c_int '5700'
GX5732_TERMINAL_COUNT_OUPUT_ALLCOUNTERS_AND_CLOCKS = 4 # Variable c_int '4'
GX5733_PXI_TRIGGER_LINE_DISCONNECTED = 0 # Variable c_int '0'
GX5731_PORT3 = 3 # Variable c_int '3'
GX5642_CHANNEL_OUTPUT_ENABLE = 1 # Variable c_int '1'
GXPIO_INVALID_CLOCK = -49 # Variable c_int '-0x00000000000000031'
GX5731_MODULE_DIRECTION_TTL_TO_DIFFERENTIAL = 1 # Variable c_int '1'
GX5731_DIGITAL_PORT_IO = 5714 # Variable c_int '5714'
GX5641_CHANNEL_TTL_PORT = 0 # Variable c_int '0'
GX5733_MODULE_OPERATION_PORT_IO = 1 # Variable c_int '1'
GX5732_COUNTER_PORT_DIRECTION_IN = 0 # Variable c_int '0'
GX5733_ENABLE_INTERNAL_CLOCK = 1 # Variable c_int '1'
GX5733_INTERNAL_CLOCK1_T0_STAR_TRIGGER = 3 # Variable c_int '3'
GXPIO_UNABLE_TO_EMPTY_BUFFER = -81 # Variable c_int '-0x00000000000000051'
GX5733_MODULE_DIRECTION_TTL_TO_DIFFERENTIAL = 1 # Variable c_int '1'
GX5733_MODULE_TERMINATION_ON = 1 # Variable c_int '1'
GX5731_MODULE_OPERATION_BUFFERED = 0 # Variable c_int '0'
GT_INVALID_PARAMETER = -21 # Variable c_int '-0x00000000000000015'
GX5641_CHANNEL_MODE_STATIC_IO = 1 # Variable c_int '1'
GX5732_COUNTER_GATE_USER_LINE2 = 4 # Variable c_int '4'
GX5732_COUNTER_GATE_USER_LINE3 = 5 # Variable c_int '5'
GX5732_COUNTER_GATE_USER_LINE0 = 2 # Variable c_int '2'
GX5732_COUNTER_GATE_USER_LINE1 = 3 # Variable c_int '3'
GX5732_COUNTER_GATE_USER_LINE4 = 6 # Variable c_int '6'
GX5732_COUNTER_GATE_USER_LINE5 = 7 # Variable c_int '7'
GX5733_MIN_CLOCK_DIVIDER = 1 # Variable c_int '1'
GX5641_CHANNEL_OUTPUT_ENABLE = 1 # Variable c_int '1'
GXPIO_INVALID_STROBE_SOURCE = -54 # Variable c_int '-0x00000000000000036'
GX5731_CLOCK1 = 1 # Variable c_int '1'
GX5731_CLOCK0 = 0 # Variable c_int '0'
GX5731_PORT_HIGH_WORD = 1 # Variable c_int '1'
GX5642_CHANNEL_TTL_PORT = 0 # Variable c_int '0'
GX5733_INTERNAL_CLOCK0_T0_STAR_TRIGGER = 3 # Variable c_int '3'
GX5732_COUNTER_PORT_LOAD_CONTROL_NONE = 0 # Variable c_int '0'
GX5731_PXI_TRIGGER_LINE_DISCONNECTED = 0 # Variable c_int '0'
GX5732_MIN_CLOCK_DIVIDER = 1 # Variable c_int '1'
GX5731_INTERNAL_CLOCK0_T0_STAR_TRIGGER = 3 # Variable c_int '3'
GXPIO_BUFFER_TEST_FAIL = -82 # Variable c_int '-0x00000000000000052'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER2 = 9 # Variable c_int '9'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER3 = 10 # Variable c_int '10'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER0 = 7 # Variable c_int '7'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER1 = 8 # Variable c_int '8'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER6 = 13 # Variable c_int '13'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER7 = 14 # Variable c_int '14'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER4 = 11 # Variable c_int '11'
GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER5 = 12 # Variable c_int '12'
GX5732_PORT_BYTE2 = 2 # Variable c_int '2'
GX5732_PORT_BYTE3 = 3 # Variable c_int '3'
GX5732_PORT_BYTE0 = 0 # Variable c_int '0'
GX5732_PORT_BYTE1 = 1 # Variable c_int '1'
GT_NOT_CALIBRATED = -12 # Variable c_int '-0x0000000000000000c'
GX5731_RS422_PORT_IO = 5709 # Variable c_int '5709'
GX5731_INTERNAL_CLOCK1_T0_PCI_CLOCK_33MHZ = 1 # Variable c_int '1'
GT_BOARD_INVALID_EEPROM = -10 # Variable c_int '-0x0000000000000000a'
GT_CANT_OPEN_HW = -1 # Variable c_int '-0x00000000000000001'
GXPIO_INVALID_INTERNAL_STROBE_SOURCE = -53 # Variable c_int '-0x00000000000000035'
GX5731_PORT_DIRECTION_IN = 0 # Variable c_int '0'
GX5733_MODULE_BUFFER_EMPTY = 0 # Variable c_int '0'
GXPIO_BUFFER_READ_FAIL = -84 # Variable c_int '-0x00000000000000054'
GXPIO_INVALID_BUFFER_SIZE = -56 # Variable c_int '-0x00000000000000038'
GX5733_PXI_TRIGGER_LINE_CONNECTED = 1 # Variable c_int '1'
GX5732_PORT_HIGH_WORD = 1 # Variable c_int '1'
GX5733_DIGITAL_OUTPUT_LATCH = 5702 # Variable c_int '5702'
GX5731_PXI_TRIGGER_LINE3 = 3 # Variable c_int '3'
GX5731_PXI_TRIGGER_LINE2 = 2 # Variable c_int '2'
GX5731_PXI_TRIGGER_LINE1 = 1 # Variable c_int '1'
GX5731_PXI_TRIGGER_LINE0 = 0 # Variable c_int '0'
GX5731_PXI_TRIGGER_LINE7 = 7 # Variable c_int '7'
GX5731_PXI_TRIGGER_LINE6 = 6 # Variable c_int '6'
GX5731_PXI_TRIGGER_LINE5 = 5 # Variable c_int '5'
GX5731_PXI_TRIGGER_LINE4 = 4 # Variable c_int '4'
GX5733_PORT_LOW_WORD = 0 # Variable c_int '0'
GT_UNABLE_ALLOC_MEMORY = -7 # Variable c_int '-0x00000000000000007'
GX5731_MODULE_MAX_STROBE_WIDTH = 5000 # Variable c_int '5000'
GX5731_MODULE_BUFFER_MODE_FULL = 0 # Variable c_int '0'
GX5733_MODULE_TERMINATION_OFF = 0 # Variable c_int '0'
GX5732_COUNTER_PORT_LOAD_CONTROL_IMMEDIATE = 1 # Variable c_int '1'
GX5733_MODULE_OPERATION_BUFFERED = 0 # Variable c_int '0'
GX5731_PORT_BYTE3 = 3 # Variable c_int '3'
GX5731_PORT_BYTE2 = 2 # Variable c_int '2'
GX5731_PORT_BYTE1 = 1 # Variable c_int '1'
GX5731_PORT_BYTE0 = 0 # Variable c_int '0'
GT_NO_ERROR = 0 # Variable c_int '0'
GX5731_MODULE_STROBE_NEGATIVE_EDGE = 1 # Variable c_int '1'
GXPIO_INVALID_CHANNEL_STATE = -63 # Variable c_int '-0x0000000000000003f'
GX5642_LAST_CHANNEL = 63 # Variable c_int '63'
GX5732_TERMINAL_COUNT_POS_SQUARE = 2 # Variable c_int '2'
GT_INVALID_STRLEN = -24 # Variable c_int '-0x00000000000000018'
GX5733_MODULE_DIRECTION_INPUT = 0 # Variable c_int '0'
GX5731_INTERNAL_CLOCK0_T0_PCI_CLOCK_33MHZ = 1 # Variable c_int '1'
GX5731_INTERNAL_CLOCK0_T0_CLOCK_IN0 = 0 # Variable c_int '0'
GX5731_DIGITAL_OUTPUT_LATCH = 5702 # Variable c_int '5702'
GX5641_CHANNEL_CONVERT_TTL_TO_DIFFERENTIAL = 1 # Variable c_int '1'
GT_BOARD_NOT_EXIST = -2 # Variable c_int '-0x00000000000000002'
GX5642_CHANNEL_MODE_CONVERSION = 0 # Variable c_int '0'
GX5641_CHANNEL_PORT_INPUT = 0 # Variable c_int '0'
GX5731_PXI_TRIGGER_LINE_CONNECTED = 1 # Variable c_int '1'
GXPIO_INVALID_CHANNEL = -59 # Variable c_int '-0x0000000000000003b'
GX5733_MODULE_DIRECTION_SOURCE_INTERNAL = 0 # Variable c_int '0'
GXPIO_PANEL_MODELESS = 0 # Variable c_int '0'
GX5731_MAX_CLOCK_DIVIDER = 268435456 # Variable c_int '268435456'
GX5733_DISABLE_INTERNAL_CLOCK = 0 # Variable c_int '0'
GX5733_MODULE_HANDSHAKE_OUTPUT_ENABLE = 1 # Variable c_int '1'
GXPIO_INVALID_IN_LOAD_CONTROL = -45 # Variable c_int '-0x0000000000000002d'
GX5641_FIRST_CHANNEL = 0 # Variable c_int '0'
GX5642_CHANNEL_CONVERT_TTL_TO_DIFFERENTIAL = 1 # Variable c_int '1'
GX5733_INTERNAL_CLOCK1_T0_PXI_CLOCK_10MHZ = 2 # Variable c_int '2'
GXPIO_INVALID_GROUP = -57 # Variable c_int '-0x00000000000000039'
GX5731_MODULE_DIRECTION_SOURCE_INTERNAL = 0 # Variable c_int '0'
GX5731_MODULE_MAX_VTHRESHOLD = 30.0 # Variable c_double '3.0e+1'
GXPIO_INVALID_TC_MODE = -47 # Variable c_int '-0x0000000000000002f'
GX5731_MODULE_OUTPUT_DISABLE = 0 # Variable c_int '0'
GXPIO_PANEL_MODAL = 1 # Variable c_int '1'
GX5733_MODULE_DIRECTION_OUTPUT = 1 # Variable c_int '1'
GX5641_CHANNEL_OUTPUT_DISABLE = 0 # Variable c_int '0'
GX5642_GROUP1 = 1 # Variable c_int '1'
GX5642_GROUP0 = 0 # Variable c_int '0'
GX5733_MODULE_STROBE_POSITIVE_EDGE = 0 # Variable c_int '0'
GX5731_COUNTER_TO_CLOCK1 = 1 # Variable c_int '1'
GX5731_COUNTER_TO_CLOCK0 = 0 # Variable c_int '0'
GX5732_COUNTER_PORT_DIRECTION_OUT = 1 # Variable c_int '1'
GX5733_MODULE_DIRECTION_DIFFERENTIAL_TO_TTL = 0 # Variable c_int '0'
GX5642_CHANNEL_PORT_OUTPUT = 1 # Variable c_int '1'
GX5733_MODULE_BUFFER_FULL = 1 # Variable c_int '1'
GT_NOT_IN_CALIBRATION_MODE = -11 # Variable c_int '-0x0000000000000000b'
GX5731_MODULE_TERMINATION_OFF = 0 # Variable c_int '0'
GX5732_PORT_LOW_WORD = 0 # Variable c_int '0'
GX5732_POSITIVE_EDGE = 0 # Variable c_int '0'
GX5733_INTERNAL_CLOCK1_NOT_CONNECTED = 0 # Variable c_int '0'
GX5733_MODULE_OUTPUT_ENABLE = 1 # Variable c_int '1'
GX5731_MODULE_BUFFER_FULL = 1 # Variable c_int '1'
GX5733_MODULE_STROBE_EXTERNAL = 1 # Variable c_int '1'
GX5642_CHANNEL_DIFFERENTIAL_PORT = 1 # Variable c_int '1'
GX5731_MODULE_STROBE_INTERNAL = 0 # Variable c_int '0'
GX5733_MODULE_MAX_STROBE_WIDTH = 5000 # Variable c_int '5000'
GXPIO_INVALID_CHANNEL_CONVERSION_MODE = -62 # Variable c_int '-0x0000000000000003e'
GX5641_LAST_CHANNEL = 63 # Variable c_int '63'
GX5733_INTERNAL_CLOCK1_T0_PCI_CLOCK_33MHZ = 1 # Variable c_int '1'
GX5641_CHANNEL_PORT_OUTPUT = 1 # Variable c_int '1'
GT_PARAMETER_OUT_OF_RANGE = -26 # Variable c_int '-0x0000000000000001a'
GX5731_MODULE_STATE_HALT = 0 # Variable c_int '0'
GX5733_MIN_BUFFER_SIZE = 1 # Variable c_int '1'
GX5731_INTERNAL_CLOCK1_T0_STAR_TRIGGER = 3 # Variable c_int '3'
GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER0 = 4 # Variable c_int '4'
GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER1 = 5 # Variable c_int '5'
GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER2 = 6 # Variable c_int '6'
GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER3 = 7 # Variable c_int '7'
GX5733_MODULE_MIN_STROBE_WIDTH = 50 # Variable c_int '50'
GX5733_MODULE_STROBE_NEGATIVE_EDGE = 1 # Variable c_int '1'
GT_INVALID_HANDLE = -23 # Variable c_int '-0x00000000000000017'
GX5731_MODULE_MIN_VTHRESHOLD = -30.0 # Variable c_double '-3.0e+1'
GX5732_TERMINAL_COUNT_NEG_SQUARE = 3 # Variable c_int '3'
GX5732_INTERNAL_CLOCK_T0_PXI_CLOCK_10MHZ = 1 # Variable c_int '1'
GX5733_MODULE_BUFFER_MODE_FULL = 0 # Variable c_int '0'
GX5733_DIGITAL_POWER_OUTPUT_LATCH = 5704 # Variable c_int '5704'
GXPIO_INVALID_COUNTER = -44 # Variable c_int '-0x0000000000000002c'
CHAR = c_char
BYTE = c_ubyte
SHORT = c_short
WORD = c_ushort
INT = c_int
UINT = c_uint
LONG = c_int
DWORD = c_uint
DOUBLE = c_double
BOOL = c_int
PBYTE = POINTER(BYTE)
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
GxPioGetErrorString = _libraries['libGxPio.so'].GxPioGetErrorString
GxPioGetErrorString.restype = None
GxPioGetErrorString.argtypes = [SHORT, PSTR, SHORT, PSHORT]
GxPioGetDriverSummary = _libraries['libGxPio.so'].GxPioGetDriverSummary
GxPioGetDriverSummary.restype = None
GxPioGetDriverSummary.argtypes = [PSTR, SHORT, PDWORD, PSHORT]
Gx5641Initialize = _libraries['libGxPio.so'].Gx5641Initialize
Gx5641Initialize.restype = None
Gx5641Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx5641InitializeVisa = _libraries['libGxPio.so'].Gx5641InitializeVisa
Gx5641InitializeVisa.restype = None
Gx5641InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx5641Reset = _libraries['libGxPio.so'].Gx5641Reset
Gx5641Reset.restype = None
Gx5641Reset.argtypes = [SHORT, PSHORT]
Gx5641Panel = _libraries['libGxPio.so'].Gx5641Panel
Gx5641Panel.restype = None
Gx5641Panel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
Gx5641GetBoardSummary = _libraries['libGxPio.so'].Gx5641GetBoardSummary
Gx5641GetBoardSummary.restype = None
Gx5641GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx5641GetChannelOutputState = _libraries['libGxPio.so'].Gx5641GetChannelOutputState
Gx5641GetChannelOutputState.restype = None
Gx5641GetChannelOutputState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5641SetChannelOutputState = _libraries['libGxPio.so'].Gx5641SetChannelOutputState
Gx5641SetChannelOutputState.restype = None
Gx5641SetChannelOutputState.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5641GetChannelMode = _libraries['libGxPio.so'].Gx5641GetChannelMode
Gx5641GetChannelMode.restype = None
Gx5641GetChannelMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5641SetChannelMode = _libraries['libGxPio.so'].Gx5641SetChannelMode
Gx5641SetChannelMode.restype = None
Gx5641SetChannelMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5641GetChannelTTLPort = _libraries['libGxPio.so'].Gx5641GetChannelTTLPort
Gx5641GetChannelTTLPort.restype = None
Gx5641GetChannelTTLPort.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx5641SetChannelTTLPort = _libraries['libGxPio.so'].Gx5641SetChannelTTLPort
Gx5641SetChannelTTLPort.restype = None
Gx5641SetChannelTTLPort.argtypes = [SHORT, SHORT, BOOL, PSHORT]
Gx5641GetChannelTTLPortDirection = _libraries['libGxPio.so'].Gx5641GetChannelTTLPortDirection
Gx5641GetChannelTTLPortDirection.restype = None
Gx5641GetChannelTTLPortDirection.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5641SetChannelTTLPortDirection = _libraries['libGxPio.so'].Gx5641SetChannelTTLPortDirection
Gx5641SetChannelTTLPortDirection.restype = None
Gx5641SetChannelTTLPortDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5641GetChannelDifferentialPort = _libraries['libGxPio.so'].Gx5641GetChannelDifferentialPort
Gx5641GetChannelDifferentialPort.restype = None
Gx5641GetChannelDifferentialPort.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx5641SetChannelDifferentialPort = _libraries['libGxPio.so'].Gx5641SetChannelDifferentialPort
Gx5641SetChannelDifferentialPort.restype = None
Gx5641SetChannelDifferentialPort.argtypes = [SHORT, SHORT, BOOL, PSHORT]
Gx5641GetChannelDifferentialPortDirection = _libraries['libGxPio.so'].Gx5641GetChannelDifferentialPortDirection
Gx5641GetChannelDifferentialPortDirection.restype = None
Gx5641GetChannelDifferentialPortDirection.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5641SetChannelDifferentialPortDirection = _libraries['libGxPio.so'].Gx5641SetChannelDifferentialPortDirection
Gx5641SetChannelDifferentialPortDirection.restype = None
Gx5641SetChannelDifferentialPortDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5641GetChannelConversionMode = _libraries['libGxPio.so'].Gx5641GetChannelConversionMode
Gx5641GetChannelConversionMode.restype = None
Gx5641GetChannelConversionMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5641SetChannelConversionMode = _libraries['libGxPio.so'].Gx5641SetChannelConversionMode
Gx5641SetChannelConversionMode.restype = None
Gx5641SetChannelConversionMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5641ResetGroup = _libraries['libGxPio.so'].Gx5641ResetGroup
Gx5641ResetGroup.restype = None
Gx5641ResetGroup.argtypes = [SHORT, SHORT, PSHORT]
Gx5641GetGroupOutputState = _libraries['libGxPio.so'].Gx5641GetGroupOutputState
Gx5641GetGroupOutputState.restype = None
Gx5641GetGroupOutputState.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5641SetGroupOutputState = _libraries['libGxPio.so'].Gx5641SetGroupOutputState
Gx5641SetGroupOutputState.restype = None
Gx5641SetGroupOutputState.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5641GetGroupMode = _libraries['libGxPio.so'].Gx5641GetGroupMode
Gx5641GetGroupMode.restype = None
Gx5641GetGroupMode.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5641SetGroupMode = _libraries['libGxPio.so'].Gx5641SetGroupMode
Gx5641SetGroupMode.restype = None
Gx5641SetGroupMode.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5641GetGroupTTLPort = _libraries['libGxPio.so'].Gx5641GetGroupTTLPort
Gx5641GetGroupTTLPort.restype = None
Gx5641GetGroupTTLPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5641SetGroupTTLPort = _libraries['libGxPio.so'].Gx5641SetGroupTTLPort
Gx5641SetGroupTTLPort.restype = None
Gx5641SetGroupTTLPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5641GetGroupTTLPortDirection = _libraries['libGxPio.so'].Gx5641GetGroupTTLPortDirection
Gx5641GetGroupTTLPortDirection.restype = None
Gx5641GetGroupTTLPortDirection.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5641SetGroupTTLPortDirection = _libraries['libGxPio.so'].Gx5641SetGroupTTLPortDirection
Gx5641SetGroupTTLPortDirection.restype = None
Gx5641SetGroupTTLPortDirection.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5641GetGroupDifferentialPort = _libraries['libGxPio.so'].Gx5641GetGroupDifferentialPort
Gx5641GetGroupDifferentialPort.restype = None
Gx5641GetGroupDifferentialPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5641SetGroupDifferentialPort = _libraries['libGxPio.so'].Gx5641SetGroupDifferentialPort
Gx5641SetGroupDifferentialPort.restype = None
Gx5641SetGroupDifferentialPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5641GetGroupDifferentialPortDirection = _libraries['libGxPio.so'].Gx5641GetGroupDifferentialPortDirection
Gx5641GetGroupDifferentialPortDirection.restype = None
Gx5641GetGroupDifferentialPortDirection.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5641SetGroupDifferentialPortDirection = _libraries['libGxPio.so'].Gx5641SetGroupDifferentialPortDirection
Gx5641SetGroupDifferentialPortDirection.restype = None
Gx5641SetGroupDifferentialPortDirection.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5641GetGroupConversionMode = _libraries['libGxPio.so'].Gx5641GetGroupConversionMode
Gx5641GetGroupConversionMode.restype = None
Gx5641GetGroupConversionMode.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5641SetGroupConversionMode = _libraries['libGxPio.so'].Gx5641SetGroupConversionMode
Gx5641SetGroupConversionMode.restype = None
Gx5641SetGroupConversionMode.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5641LoadGroupDirectionFromDIPSwitch = _libraries['libGxPio.so'].Gx5641LoadGroupDirectionFromDIPSwitch
Gx5641LoadGroupDirectionFromDIPSwitch.restype = None
Gx5641LoadGroupDirectionFromDIPSwitch.argtypes = [SHORT, SHORT, PSHORT]
Gx5641GetPxiTriggerBusToGroupOutputState = _libraries['libGxPio.so'].Gx5641GetPxiTriggerBusToGroupOutputState
Gx5641GetPxiTriggerBusToGroupOutputState.restype = None
Gx5641GetPxiTriggerBusToGroupOutputState.argtypes = [SHORT, SHORT, PSHORT, PBOOL, PSHORT]
Gx5641SetPxiTriggerBusToGroupOutputState = _libraries['libGxPio.so'].Gx5641SetPxiTriggerBusToGroupOutputState
Gx5641SetPxiTriggerBusToGroupOutputState.restype = None
Gx5641SetPxiTriggerBusToGroupOutputState.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5642Initialize = _libraries['libGxPio.so'].Gx5642Initialize
Gx5642Initialize.restype = None
Gx5642Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx5642InitializeVisa = _libraries['libGxPio.so'].Gx5642InitializeVisa
Gx5642InitializeVisa.restype = None
Gx5642InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx5642Reset = _libraries['libGxPio.so'].Gx5642Reset
Gx5642Reset.restype = None
Gx5642Reset.argtypes = [SHORT, PSHORT]
Gx5642Panel = _libraries['libGxPio.so'].Gx5642Panel
Gx5642Panel.restype = None
Gx5642Panel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
Gx5642GetBoardSummary = _libraries['libGxPio.so'].Gx5642GetBoardSummary
Gx5642GetBoardSummary.restype = None
Gx5642GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx5642GetChannelOutputState = _libraries['libGxPio.so'].Gx5642GetChannelOutputState
Gx5642GetChannelOutputState.restype = None
Gx5642GetChannelOutputState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5642SetChannelOutputState = _libraries['libGxPio.so'].Gx5642SetChannelOutputState
Gx5642SetChannelOutputState.restype = None
Gx5642SetChannelOutputState.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5642GetChannelMode = _libraries['libGxPio.so'].Gx5642GetChannelMode
Gx5642GetChannelMode.restype = None
Gx5642GetChannelMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5642SetChannelMode = _libraries['libGxPio.so'].Gx5642SetChannelMode
Gx5642SetChannelMode.restype = None
Gx5642SetChannelMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5642GetChannelTTLPort = _libraries['libGxPio.so'].Gx5642GetChannelTTLPort
Gx5642GetChannelTTLPort.restype = None
Gx5642GetChannelTTLPort.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx5642SetChannelTTLPort = _libraries['libGxPio.so'].Gx5642SetChannelTTLPort
Gx5642SetChannelTTLPort.restype = None
Gx5642SetChannelTTLPort.argtypes = [SHORT, SHORT, BOOL, PSHORT]
Gx5642GetChannelTTLPortDirection = _libraries['libGxPio.so'].Gx5642GetChannelTTLPortDirection
Gx5642GetChannelTTLPortDirection.restype = None
Gx5642GetChannelTTLPortDirection.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5642SetChannelTTLPortDirection = _libraries['libGxPio.so'].Gx5642SetChannelTTLPortDirection
Gx5642SetChannelTTLPortDirection.restype = None
Gx5642SetChannelTTLPortDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5642GetChannelDifferentialPort = _libraries['libGxPio.so'].Gx5642GetChannelDifferentialPort
Gx5642GetChannelDifferentialPort.restype = None
Gx5642GetChannelDifferentialPort.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx5642SetChannelDifferentialPort = _libraries['libGxPio.so'].Gx5642SetChannelDifferentialPort
Gx5642SetChannelDifferentialPort.restype = None
Gx5642SetChannelDifferentialPort.argtypes = [SHORT, SHORT, BOOL, PSHORT]
Gx5642GetChannelDifferentialPortDirection = _libraries['libGxPio.so'].Gx5642GetChannelDifferentialPortDirection
Gx5642GetChannelDifferentialPortDirection.restype = None
Gx5642GetChannelDifferentialPortDirection.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5642SetChannelDifferentialPortDirection = _libraries['libGxPio.so'].Gx5642SetChannelDifferentialPortDirection
Gx5642SetChannelDifferentialPortDirection.restype = None
Gx5642SetChannelDifferentialPortDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5642GetChannelConversionMode = _libraries['libGxPio.so'].Gx5642GetChannelConversionMode
Gx5642GetChannelConversionMode.restype = None
Gx5642GetChannelConversionMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5642SetChannelConversionMode = _libraries['libGxPio.so'].Gx5642SetChannelConversionMode
Gx5642SetChannelConversionMode.restype = None
Gx5642SetChannelConversionMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5642ResetGroup = _libraries['libGxPio.so'].Gx5642ResetGroup
Gx5642ResetGroup.restype = None
Gx5642ResetGroup.argtypes = [SHORT, SHORT, PSHORT]
Gx5642GetGroupOutputState = _libraries['libGxPio.so'].Gx5642GetGroupOutputState
Gx5642GetGroupOutputState.restype = None
Gx5642GetGroupOutputState.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5642SetGroupOutputState = _libraries['libGxPio.so'].Gx5642SetGroupOutputState
Gx5642SetGroupOutputState.restype = None
Gx5642SetGroupOutputState.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5642GetGroupMode = _libraries['libGxPio.so'].Gx5642GetGroupMode
Gx5642GetGroupMode.restype = None
Gx5642GetGroupMode.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5642SetGroupMode = _libraries['libGxPio.so'].Gx5642SetGroupMode
Gx5642SetGroupMode.restype = None
Gx5642SetGroupMode.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5642GetGroupTTLPort = _libraries['libGxPio.so'].Gx5642GetGroupTTLPort
Gx5642GetGroupTTLPort.restype = None
Gx5642GetGroupTTLPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5642SetGroupTTLPort = _libraries['libGxPio.so'].Gx5642SetGroupTTLPort
Gx5642SetGroupTTLPort.restype = None
Gx5642SetGroupTTLPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5642GetGroupTTLPortDirection = _libraries['libGxPio.so'].Gx5642GetGroupTTLPortDirection
Gx5642GetGroupTTLPortDirection.restype = None
Gx5642GetGroupTTLPortDirection.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5642SetGroupTTLPortDirection = _libraries['libGxPio.so'].Gx5642SetGroupTTLPortDirection
Gx5642SetGroupTTLPortDirection.restype = None
Gx5642SetGroupTTLPortDirection.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5642GetGroupDifferentialPort = _libraries['libGxPio.so'].Gx5642GetGroupDifferentialPort
Gx5642GetGroupDifferentialPort.restype = None
Gx5642GetGroupDifferentialPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5642SetGroupDifferentialPort = _libraries['libGxPio.so'].Gx5642SetGroupDifferentialPort
Gx5642SetGroupDifferentialPort.restype = None
Gx5642SetGroupDifferentialPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5642GetGroupDifferentialPortDirection = _libraries['libGxPio.so'].Gx5642GetGroupDifferentialPortDirection
Gx5642GetGroupDifferentialPortDirection.restype = None
Gx5642GetGroupDifferentialPortDirection.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5642SetGroupDifferentialPortDirection = _libraries['libGxPio.so'].Gx5642SetGroupDifferentialPortDirection
Gx5642SetGroupDifferentialPortDirection.restype = None
Gx5642SetGroupDifferentialPortDirection.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5642GetGroupConversionMode = _libraries['libGxPio.so'].Gx5642GetGroupConversionMode
Gx5642GetGroupConversionMode.restype = None
Gx5642GetGroupConversionMode.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5642SetGroupConversionMode = _libraries['libGxPio.so'].Gx5642SetGroupConversionMode
Gx5642SetGroupConversionMode.restype = None
Gx5642SetGroupConversionMode.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5642LoadGroupDirectionFromDIPSwitch = _libraries['libGxPio.so'].Gx5642LoadGroupDirectionFromDIPSwitch
Gx5642LoadGroupDirectionFromDIPSwitch.restype = None
Gx5642LoadGroupDirectionFromDIPSwitch.argtypes = [SHORT, SHORT, PSHORT]
Gx5642GetPxiTriggerBusToGroupOutputState = _libraries['libGxPio.so'].Gx5642GetPxiTriggerBusToGroupOutputState
Gx5642GetPxiTriggerBusToGroupOutputState.restype = None
Gx5642GetPxiTriggerBusToGroupOutputState.argtypes = [SHORT, SHORT, PSHORT, PBOOL, PSHORT]
Gx5642SetPxiTriggerBusToGroupOutputState = _libraries['libGxPio.so'].Gx5642SetPxiTriggerBusToGroupOutputState
Gx5642SetPxiTriggerBusToGroupOutputState.restype = None
Gx5642SetPxiTriggerBusToGroupOutputState.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5731Initialize = _libraries['libGxPio.so'].Gx5731Initialize
Gx5731Initialize.restype = None
Gx5731Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx5731InitializeVisa = _libraries['libGxPio.so'].Gx5731InitializeVisa
Gx5731InitializeVisa.restype = None
Gx5731InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx5731Reset = _libraries['libGxPio.so'].Gx5731Reset
Gx5731Reset.restype = None
Gx5731Reset.argtypes = [SHORT, PSHORT]
Gx5731Panel = _libraries['libGxPio.so'].Gx5731Panel
Gx5731Panel.restype = None
Gx5731Panel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
Gx5731GetBoardSummary = _libraries['libGxPio.so'].Gx5731GetBoardSummary
Gx5731GetBoardSummary.restype = None
Gx5731GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx5731ResetPort = _libraries['libGxPio.so'].Gx5731ResetPort
Gx5731ResetPort.restype = None
Gx5731ResetPort.argtypes = [SHORT, SHORT, PSHORT]
Gx5731GetPort = _libraries['libGxPio.so'].Gx5731GetPort
Gx5731GetPort.restype = None
Gx5731GetPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5731SetPort = _libraries['libGxPio.so'].Gx5731SetPort
Gx5731SetPort.restype = None
Gx5731SetPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5731GetPortWord = _libraries['libGxPio.so'].Gx5731GetPortWord
Gx5731GetPortWord.restype = None
Gx5731GetPortWord.argtypes = [SHORT, SHORT, SHORT, PWORD, PSHORT]
Gx5731SetPortWord = _libraries['libGxPio.so'].Gx5731SetPortWord
Gx5731SetPortWord.restype = None
Gx5731SetPortWord.argtypes = [SHORT, SHORT, SHORT, WORD, PSHORT]
Gx5731GetPortByte = _libraries['libGxPio.so'].Gx5731GetPortByte
Gx5731GetPortByte.restype = None
Gx5731GetPortByte.argtypes = [SHORT, SHORT, SHORT, PBYTE, PSHORT]
Gx5731SetPortByte = _libraries['libGxPio.so'].Gx5731SetPortByte
Gx5731SetPortByte.restype = None
Gx5731SetPortByte.argtypes = [SHORT, SHORT, SHORT, BYTE, PSHORT]
Gx5731GetPortBit = _libraries['libGxPio.so'].Gx5731GetPortBit
Gx5731GetPortBit.restype = None
Gx5731GetPortBit.argtypes = [SHORT, SHORT, SHORT, PBOOL, PSHORT]
Gx5731SetPortBit = _libraries['libGxPio.so'].Gx5731SetPortBit
Gx5731SetPortBit.restype = None
Gx5731SetPortBit.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5731GetPortDirection = _libraries['libGxPio.so'].Gx5731GetPortDirection
Gx5731GetPortDirection.restype = None
Gx5731GetPortDirection.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731SetPortDirection = _libraries['libGxPio.so'].Gx5731SetPortDirection
Gx5731SetPortDirection.restype = None
Gx5731SetPortDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731GetPortByteDirection = _libraries['libGxPio.so'].Gx5731GetPortByteDirection
Gx5731GetPortByteDirection.restype = None
Gx5731GetPortByteDirection.argtypes = [SHORT, SHORT, SHORT, PBOOL, PSHORT]
Gx5731SetPortByteDirection = _libraries['libGxPio.so'].Gx5731SetPortByteDirection
Gx5731SetPortByteDirection.restype = None
Gx5731SetPortByteDirection.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5731ModuleGetType = _libraries['libGxPio.so'].Gx5731ModuleGetType
Gx5731ModuleGetType.restype = None
Gx5731ModuleGetType.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetRevision = _libraries['libGxPio.so'].Gx5731ModuleGetRevision
Gx5731ModuleGetRevision.restype = None
Gx5731ModuleGetRevision.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetVThreshold = _libraries['libGxPio.so'].Gx5731ModuleGetVThreshold
Gx5731ModuleGetVThreshold.restype = None
Gx5731ModuleGetVThreshold.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx5731ModuleSetVThreshold = _libraries['libGxPio.so'].Gx5731ModuleSetVThreshold
Gx5731ModuleSetVThreshold.restype = None
Gx5731ModuleSetVThreshold.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
Gx5731ModuleBufferClear = _libraries['libGxPio.so'].Gx5731ModuleBufferClear
Gx5731ModuleBufferClear.restype = None
Gx5731ModuleBufferClear.argtypes = [SHORT, SHORT, PSHORT]
Gx5731ModuleBufferGetMode = _libraries['libGxPio.so'].Gx5731ModuleBufferGetMode
Gx5731ModuleBufferGetMode.restype = None
Gx5731ModuleBufferGetMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleBufferGetState = _libraries['libGxPio.so'].Gx5731ModuleBufferGetState
Gx5731ModuleBufferGetState.restype = None
Gx5731ModuleBufferGetState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleBufferSetMode = _libraries['libGxPio.so'].Gx5731ModuleBufferSetMode
Gx5731ModuleBufferSetMode.restype = None
Gx5731ModuleBufferSetMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleBufferReadData = _libraries['libGxPio.so'].Gx5731ModuleBufferReadData
Gx5731ModuleBufferReadData.restype = None
Gx5731ModuleBufferReadData.argtypes = [SHORT, SHORT, PDWORD, PDWORD, PSHORT]
Gx5731ModuleBufferWriteData = _libraries['libGxPio.so'].Gx5731ModuleBufferWriteData
Gx5731ModuleBufferWriteData.restype = None
Gx5731ModuleBufferWriteData.argtypes = [SHORT, SHORT, PDWORD, PDWORD, PSHORT]
Gx5731ModuleBufferTest = _libraries['libGxPio.so'].Gx5731ModuleBufferTest
Gx5731ModuleBufferTest.restype = None
Gx5731ModuleBufferTest.argtypes = [SHORT, SHORT, PSHORT]
Gx5731ModuleGetOperationMode = _libraries['libGxPio.so'].Gx5731ModuleGetOperationMode
Gx5731ModuleGetOperationMode.restype = None
Gx5731ModuleGetOperationMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleSetOperationMode = _libraries['libGxPio.so'].Gx5731ModuleSetOperationMode
Gx5731ModuleSetOperationMode.restype = None
Gx5731ModuleSetOperationMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleGetOutputMode = _libraries['libGxPio.so'].Gx5731ModuleGetOutputMode
Gx5731ModuleGetOutputMode.restype = None
Gx5731ModuleGetOutputMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleSetOutputMode = _libraries['libGxPio.so'].Gx5731ModuleSetOutputMode
Gx5731ModuleSetOutputMode.restype = None
Gx5731ModuleSetOutputMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleGetHandshakeOutputMode = _libraries['libGxPio.so'].Gx5731ModuleGetHandshakeOutputMode
Gx5731ModuleGetHandshakeOutputMode.restype = None
Gx5731ModuleGetHandshakeOutputMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleSetHandshakeOutputMode = _libraries['libGxPio.so'].Gx5731ModuleSetHandshakeOutputMode
Gx5731ModuleSetHandshakeOutputMode.restype = None
Gx5731ModuleSetHandshakeOutputMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleGetPort = _libraries['libGxPio.so'].Gx5731ModuleGetPort
Gx5731ModuleGetPort.restype = None
Gx5731ModuleGetPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5731ModuleSetPort = _libraries['libGxPio.so'].Gx5731ModuleSetPort
Gx5731ModuleSetPort.restype = None
Gx5731ModuleSetPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5731ModuleGetExtStrobeEnablePolarity = _libraries['libGxPio.so'].Gx5731ModuleGetExtStrobeEnablePolarity
Gx5731ModuleGetExtStrobeEnablePolarity.restype = None
Gx5731ModuleGetExtStrobeEnablePolarity.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetExtStrobeEnableState = _libraries['libGxPio.so'].Gx5731ModuleGetExtStrobeEnableState
Gx5731ModuleGetExtStrobeEnableState.restype = None
Gx5731ModuleGetExtStrobeEnableState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetExtStrobePolarity = _libraries['libGxPio.so'].Gx5731ModuleGetExtStrobePolarity
Gx5731ModuleGetExtStrobePolarity.restype = None
Gx5731ModuleGetExtStrobePolarity.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetExtStrobeState = _libraries['libGxPio.so'].Gx5731ModuleGetExtStrobeState
Gx5731ModuleGetExtStrobeState.restype = None
Gx5731ModuleGetExtStrobeState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetInternalStrobeSource = _libraries['libGxPio.so'].Gx5731ModuleGetInternalStrobeSource
Gx5731ModuleGetInternalStrobeSource.restype = None
Gx5731ModuleGetInternalStrobeSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetOutputStrobeWidth = _libraries['libGxPio.so'].Gx5731ModuleGetOutputStrobeWidth
Gx5731ModuleGetOutputStrobeWidth.restype = None
Gx5731ModuleGetOutputStrobeWidth.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetStrobeSource = _libraries['libGxPio.so'].Gx5731ModuleGetStrobeSource
Gx5731ModuleGetStrobeSource.restype = None
Gx5731ModuleGetStrobeSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleSetExtStrobeEnablePolarity = _libraries['libGxPio.so'].Gx5731ModuleSetExtStrobeEnablePolarity
Gx5731ModuleSetExtStrobeEnablePolarity.restype = None
Gx5731ModuleSetExtStrobeEnablePolarity.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleSetExtStrobePolarity = _libraries['libGxPio.so'].Gx5731ModuleSetExtStrobePolarity
Gx5731ModuleSetExtStrobePolarity.restype = None
Gx5731ModuleSetExtStrobePolarity.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleSetInternalStrobeSource = _libraries['libGxPio.so'].Gx5731ModuleSetInternalStrobeSource
Gx5731ModuleSetInternalStrobeSource.restype = None
Gx5731ModuleSetInternalStrobeSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleSetOutputStrobeWidth = _libraries['libGxPio.so'].Gx5731ModuleSetOutputStrobeWidth
Gx5731ModuleSetOutputStrobeWidth.restype = None
Gx5731ModuleSetOutputStrobeWidth.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleSetStrobeSource = _libraries['libGxPio.so'].Gx5731ModuleSetStrobeSource
Gx5731ModuleSetStrobeSource.restype = None
Gx5731ModuleSetStrobeSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleGetPxiTriggerBus = _libraries['libGxPio.so'].Gx5731ModuleGetPxiTriggerBus
Gx5731ModuleGetPxiTriggerBus.restype = None
Gx5731ModuleGetPxiTriggerBus.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleGetPxiTriggerLine = _libraries['libGxPio.so'].Gx5731ModuleGetPxiTriggerLine
Gx5731ModuleGetPxiTriggerLine.restype = None
Gx5731ModuleGetPxiTriggerLine.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleSetPxiTriggerBus = _libraries['libGxPio.so'].Gx5731ModuleSetPxiTriggerBus
Gx5731ModuleSetPxiTriggerBus.restype = None
Gx5731ModuleSetPxiTriggerBus.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleSetPxiTriggerLine = _libraries['libGxPio.so'].Gx5731ModuleSetPxiTriggerLine
Gx5731ModuleSetPxiTriggerLine.restype = None
Gx5731ModuleSetPxiTriggerLine.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleStep = _libraries['libGxPio.so'].Gx5731ModuleStep
Gx5731ModuleStep.restype = None
Gx5731ModuleStep.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5731ModuleGetState = _libraries['libGxPio.so'].Gx5731ModuleGetState
Gx5731ModuleGetState.restype = None
Gx5731ModuleGetState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleHalt = _libraries['libGxPio.so'].Gx5731ModuleHalt
Gx5731ModuleHalt.restype = None
Gx5731ModuleHalt.argtypes = [SHORT, SHORT, PSHORT]
Gx5731ModuleRun = _libraries['libGxPio.so'].Gx5731ModuleRun
Gx5731ModuleRun.restype = None
Gx5731ModuleRun.argtypes = [SHORT, SHORT, PSHORT]
Gx5731ModuleSetTermination = _libraries['libGxPio.so'].Gx5731ModuleSetTermination
Gx5731ModuleSetTermination.restype = None
Gx5731ModuleSetTermination.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleGetTermination = _libraries['libGxPio.so'].Gx5731ModuleGetTermination
Gx5731ModuleGetTermination.restype = None
Gx5731ModuleGetTermination.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleSetDirection = _libraries['libGxPio.so'].Gx5731ModuleSetDirection
Gx5731ModuleSetDirection.restype = None
Gx5731ModuleSetDirection.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleGetDirection = _libraries['libGxPio.so'].Gx5731ModuleGetDirection
Gx5731ModuleGetDirection.restype = None
Gx5731ModuleGetDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx5731ModuleSetDirectionSource = _libraries['libGxPio.so'].Gx5731ModuleSetDirectionSource
Gx5731ModuleSetDirectionSource.restype = None
Gx5731ModuleSetDirectionSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731ModuleGetDirectionSource = _libraries['libGxPio.so'].Gx5731ModuleGetDirectionSource
Gx5731ModuleGetDirectionSource.restype = None
Gx5731ModuleGetDirectionSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731GetInternalClock = _libraries['libGxPio.so'].Gx5731GetInternalClock
Gx5731GetInternalClock.restype = None
Gx5731GetInternalClock.argtypes = [SHORT, SHORT, PSHORT, PDWORD, PSHORT]
Gx5731GetInternalClockEnable = _libraries['libGxPio.so'].Gx5731GetInternalClockEnable
Gx5731GetInternalClockEnable.restype = None
Gx5731GetInternalClockEnable.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731SetInternalClock = _libraries['libGxPio.so'].Gx5731SetInternalClock
Gx5731SetInternalClock.restype = None
Gx5731SetInternalClock.argtypes = [SHORT, SHORT, SHORT, DWORD, PSHORT]
Gx5731SetInternalClockEnable = _libraries['libGxPio.so'].Gx5731SetInternalClockEnable
Gx5731SetInternalClockEnable.restype = None
Gx5731SetInternalClockEnable.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731GetStrobeToPxiTriggerBusState = _libraries['libGxPio.so'].Gx5731GetStrobeToPxiTriggerBusState
Gx5731GetStrobeToPxiTriggerBusState.restype = None
Gx5731GetStrobeToPxiTriggerBusState.argtypes = [SHORT, PSHORT, PSHORT]
Gx5731GetStrobeToPxiTriggerLineState = _libraries['libGxPio.so'].Gx5731GetStrobeToPxiTriggerLineState
Gx5731GetStrobeToPxiTriggerLineState.restype = None
Gx5731GetStrobeToPxiTriggerLineState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731SetStrobeToPxiTriggerBusState = _libraries['libGxPio.so'].Gx5731SetStrobeToPxiTriggerBusState
Gx5731SetStrobeToPxiTriggerBusState.restype = None
Gx5731SetStrobeToPxiTriggerBusState.argtypes = [SHORT, SHORT, PSHORT]
Gx5731SetStrobeToPxiTriggerLineState = _libraries['libGxPio.so'].Gx5731SetStrobeToPxiTriggerLineState
Gx5731SetStrobeToPxiTriggerLineState.restype = None
Gx5731SetStrobeToPxiTriggerLineState.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5731GetExtTriggerToPxiTriggerBus = _libraries['libGxPio.so'].Gx5731GetExtTriggerToPxiTriggerBus
Gx5731GetExtTriggerToPxiTriggerBus.restype = None
Gx5731GetExtTriggerToPxiTriggerBus.argtypes = [SHORT, PSHORT, PSHORT]
Gx5731GetExtTriggerToPxiTriggerLine = _libraries['libGxPio.so'].Gx5731GetExtTriggerToPxiTriggerLine
Gx5731GetExtTriggerToPxiTriggerLine.restype = None
Gx5731GetExtTriggerToPxiTriggerLine.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5731SetExtTriggerToPxiTriggerBus = _libraries['libGxPio.so'].Gx5731SetExtTriggerToPxiTriggerBus
Gx5731SetExtTriggerToPxiTriggerBus.restype = None
Gx5731SetExtTriggerToPxiTriggerBus.argtypes = [SHORT, SHORT, PSHORT]
Gx5731SetExtTriggerToPxiTriggerLine = _libraries['libGxPio.so'].Gx5731SetExtTriggerToPxiTriggerLine
Gx5731SetExtTriggerToPxiTriggerLine.restype = None
Gx5731SetExtTriggerToPxiTriggerLine.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5732Initialize = _libraries['libGxPio.so'].Gx5732Initialize
Gx5732Initialize.restype = None
Gx5732Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx5732InitializeVisa = _libraries['libGxPio.so'].Gx5732InitializeVisa
Gx5732InitializeVisa.restype = None
Gx5732InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx5732Reset = _libraries['libGxPio.so'].Gx5732Reset
Gx5732Reset.restype = None
Gx5732Reset.argtypes = [SHORT, PSHORT]
Gx5732Panel = _libraries['libGxPio.so'].Gx5732Panel
Gx5732Panel.restype = None
Gx5732Panel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
Gx5732GetBoardSummary = _libraries['libGxPio.so'].Gx5732GetBoardSummary
Gx5732GetBoardSummary.restype = None
Gx5732GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx5732ResetPort = _libraries['libGxPio.so'].Gx5732ResetPort
Gx5732ResetPort.restype = None
Gx5732ResetPort.argtypes = [SHORT, SHORT, PSHORT]
Gx5732GetPort = _libraries['libGxPio.so'].Gx5732GetPort
Gx5732GetPort.restype = None
Gx5732GetPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5732SetPort = _libraries['libGxPio.so'].Gx5732SetPort
Gx5732SetPort.restype = None
Gx5732SetPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5732GetPortWord = _libraries['libGxPio.so'].Gx5732GetPortWord
Gx5732GetPortWord.restype = None
Gx5732GetPortWord.argtypes = [SHORT, SHORT, SHORT, PWORD, PSHORT]
Gx5732SetPortWord = _libraries['libGxPio.so'].Gx5732SetPortWord
Gx5732SetPortWord.restype = None
Gx5732SetPortWord.argtypes = [SHORT, SHORT, SHORT, WORD, PSHORT]
Gx5732GetPortByte = _libraries['libGxPio.so'].Gx5732GetPortByte
Gx5732GetPortByte.restype = None
Gx5732GetPortByte.argtypes = [SHORT, SHORT, SHORT, PBYTE, PSHORT]
Gx5732SetPortByte = _libraries['libGxPio.so'].Gx5732SetPortByte
Gx5732SetPortByte.restype = None
Gx5732SetPortByte.argtypes = [SHORT, SHORT, SHORT, BYTE, PSHORT]
Gx5732GetPortBit = _libraries['libGxPio.so'].Gx5732GetPortBit
Gx5732GetPortBit.restype = None
Gx5732GetPortBit.argtypes = [SHORT, SHORT, SHORT, PBYTE, PSHORT]
Gx5732SetPortBit = _libraries['libGxPio.so'].Gx5732SetPortBit
Gx5732SetPortBit.restype = None
Gx5732SetPortBit.argtypes = [SHORT, SHORT, SHORT, BYTE, PSHORT]
Gx5732GetPortDirection = _libraries['libGxPio.so'].Gx5732GetPortDirection
Gx5732GetPortDirection.restype = None
Gx5732GetPortDirection.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5732SetPortDirection = _libraries['libGxPio.so'].Gx5732SetPortDirection
Gx5732SetPortDirection.restype = None
Gx5732SetPortDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5732GetPortByteDirection = _libraries['libGxPio.so'].Gx5732GetPortByteDirection
Gx5732GetPortByteDirection.restype = None
Gx5732GetPortByteDirection.argtypes = [SHORT, SHORT, SHORT, PBOOL, PSHORT]
Gx5732SetPortByteDirection = _libraries['libGxPio.so'].Gx5732SetPortByteDirection
Gx5732SetPortByteDirection.restype = None
Gx5732SetPortByteDirection.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5732ResetCounter = _libraries['libGxPio.so'].Gx5732ResetCounter
Gx5732ResetCounter.restype = None
Gx5732ResetCounter.argtypes = [SHORT, SHORT, PSHORT]
Gx5732GetCounterEnable = _libraries['libGxPio.so'].Gx5732GetCounterEnable
Gx5732GetCounterEnable.restype = None
Gx5732GetCounterEnable.argtypes = [SHORT, SHORT, PBOOL, PSHORT]
Gx5732SetCounterEnable = _libraries['libGxPio.so'].Gx5732SetCounterEnable
Gx5732SetCounterEnable.restype = None
Gx5732SetCounterEnable.argtypes = [SHORT, SHORT, BOOL, PSHORT]
Gx5732GetCounterValue = _libraries['libGxPio.so'].Gx5732GetCounterValue
Gx5732GetCounterValue.restype = None
Gx5732GetCounterValue.argtypes = [SHORT, SHORT, PBYTE, PBOOL, PSHORT]
Gx5732SetCounterValue = _libraries['libGxPio.so'].Gx5732SetCounterValue
Gx5732SetCounterValue.restype = None
Gx5732SetCounterValue.argtypes = [SHORT, SHORT, BYTE, PSHORT]
Gx5732GetCounterMode = _libraries['libGxPio.so'].Gx5732GetCounterMode
Gx5732GetCounterMode.restype = None
Gx5732GetCounterMode.argtypes = [SHORT, SHORT, PBOOL, PBOOL, PSHORT, PSHORT]
Gx5732SetCounterMode = _libraries['libGxPio.so'].Gx5732SetCounterMode
Gx5732SetCounterMode.restype = None
Gx5732SetCounterMode.argtypes = [SHORT, SHORT, BOOL, BOOL, SHORT, PSHORT]
Gx5732GetCounterClock = _libraries['libGxPio.so'].Gx5732GetCounterClock
Gx5732GetCounterClock.restype = None
Gx5732GetCounterClock.argtypes = [SHORT, SHORT, PSHORT, PBOOL, PSHORT]
Gx5732SetCounterClock = _libraries['libGxPio.so'].Gx5732SetCounterClock
Gx5732SetCounterClock.restype = None
Gx5732SetCounterClock.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5732GetCounterGate = _libraries['libGxPio.so'].Gx5732GetCounterGate
Gx5732GetCounterGate.restype = None
Gx5732GetCounterGate.argtypes = [SHORT, SHORT, PSHORT, PBOOL, PSHORT]
Gx5732SetCounterGate = _libraries['libGxPio.so'].Gx5732SetCounterGate
Gx5732SetCounterGate.restype = None
Gx5732SetCounterGate.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5732GetTerminalCountPortConnection = _libraries['libGxPio.so'].Gx5732GetTerminalCountPortConnection
Gx5732GetTerminalCountPortConnection.restype = None
Gx5732GetTerminalCountPortConnection.argtypes = [SHORT, PSHORT, PSHORT]
Gx5732SetTerminalCountPortConnection = _libraries['libGxPio.so'].Gx5732SetTerminalCountPortConnection
Gx5732SetTerminalCountPortConnection.restype = None
Gx5732SetTerminalCountPortConnection.argtypes = [SHORT, SHORT, PSHORT]
Gx5732GetCounterPort = _libraries['libGxPio.so'].Gx5732GetCounterPort
Gx5732GetCounterPort.restype = None
Gx5732GetCounterPort.argtypes = [SHORT, PBOOL, PSHORT, PSHORT, PSHORT]
Gx5732SetCounterPort = _libraries['libGxPio.so'].Gx5732SetCounterPort
Gx5732SetCounterPort.restype = None
Gx5732SetCounterPort.argtypes = [SHORT, BOOL, SHORT, SHORT, PSHORT]
Gx5732LoadCounterCounterPort = _libraries['libGxPio.so'].Gx5732LoadCounterCounterPort
Gx5732LoadCounterCounterPort.restype = None
Gx5732LoadCounterCounterPort.argtypes = [SHORT, PSHORT]
Gx5732GetInternalClock = _libraries['libGxPio.so'].Gx5732GetInternalClock
Gx5732GetInternalClock.restype = None
Gx5732GetInternalClock.argtypes = [SHORT, SHORT, PSHORT, PDWORD, PSHORT]
Gx5732SetInternalClock = _libraries['libGxPio.so'].Gx5732SetInternalClock
Gx5732SetInternalClock.restype = None
Gx5732SetInternalClock.argtypes = [SHORT, SHORT, SHORT, DWORD, PSHORT]
Gx5733Initialize = _libraries['libGxPio.so'].Gx5733Initialize
Gx5733Initialize.restype = None
Gx5733Initialize.argtypes = [SHORT, PSHORT, PSHORT]
Gx5733InitializeVisa = _libraries['libGxPio.so'].Gx5733InitializeVisa
Gx5733InitializeVisa.restype = None
Gx5733InitializeVisa.argtypes = [PCSTR, PSHORT, PSHORT]
Gx5733Reset = _libraries['libGxPio.so'].Gx5733Reset
Gx5733Reset.restype = None
Gx5733Reset.argtypes = [SHORT, PSHORT]
Gx5733Panel = _libraries['libGxPio.so'].Gx5733Panel
Gx5733Panel.restype = None
Gx5733Panel.argtypes = [PSHORT, HWND, SHORT, POINTER(HWND), PSHORT]
Gx5733GetBoardSummary = _libraries['libGxPio.so'].Gx5733GetBoardSummary
Gx5733GetBoardSummary.restype = None
Gx5733GetBoardSummary.argtypes = [SHORT, PSTR, SHORT, PSHORT]
Gx5733ResetPort = _libraries['libGxPio.so'].Gx5733ResetPort
Gx5733ResetPort.restype = None
Gx5733ResetPort.argtypes = [SHORT, SHORT, PSHORT]
Gx5733GetPort = _libraries['libGxPio.so'].Gx5733GetPort
Gx5733GetPort.restype = None
Gx5733GetPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5733SetPort = _libraries['libGxPio.so'].Gx5733SetPort
Gx5733SetPort.restype = None
Gx5733SetPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5733GetPortWord = _libraries['libGxPio.so'].Gx5733GetPortWord
Gx5733GetPortWord.restype = None
Gx5733GetPortWord.argtypes = [SHORT, SHORT, SHORT, PWORD, PSHORT]
Gx5733SetPortWord = _libraries['libGxPio.so'].Gx5733SetPortWord
Gx5733SetPortWord.restype = None
Gx5733SetPortWord.argtypes = [SHORT, SHORT, SHORT, WORD, PSHORT]
Gx5733GetPortByte = _libraries['libGxPio.so'].Gx5733GetPortByte
Gx5733GetPortByte.restype = None
Gx5733GetPortByte.argtypes = [SHORT, SHORT, SHORT, PBYTE, PSHORT]
Gx5733SetPortByte = _libraries['libGxPio.so'].Gx5733SetPortByte
Gx5733SetPortByte.restype = None
Gx5733SetPortByte.argtypes = [SHORT, SHORT, SHORT, BYTE, PSHORT]
Gx5733GetPortBit = _libraries['libGxPio.so'].Gx5733GetPortBit
Gx5733GetPortBit.restype = None
Gx5733GetPortBit.argtypes = [SHORT, SHORT, SHORT, PBOOL, PSHORT]
Gx5733SetPortBit = _libraries['libGxPio.so'].Gx5733SetPortBit
Gx5733SetPortBit.restype = None
Gx5733SetPortBit.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5733GetPortDirection = _libraries['libGxPio.so'].Gx5733GetPortDirection
Gx5733GetPortDirection.restype = None
Gx5733GetPortDirection.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733SetPortDirection = _libraries['libGxPio.so'].Gx5733SetPortDirection
Gx5733SetPortDirection.restype = None
Gx5733SetPortDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733GetPortByteDirection = _libraries['libGxPio.so'].Gx5733GetPortByteDirection
Gx5733GetPortByteDirection.restype = None
Gx5733GetPortByteDirection.argtypes = [SHORT, SHORT, SHORT, PBOOL, PSHORT]
Gx5733SetPortByteDirection = _libraries['libGxPio.so'].Gx5733SetPortByteDirection
Gx5733SetPortByteDirection.restype = None
Gx5733SetPortByteDirection.argtypes = [SHORT, SHORT, SHORT, BOOL, PSHORT]
Gx5733ModuleGetType = _libraries['libGxPio.so'].Gx5733ModuleGetType
Gx5733ModuleGetType.restype = None
Gx5733ModuleGetType.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetRevision = _libraries['libGxPio.so'].Gx5733ModuleGetRevision
Gx5733ModuleGetRevision.restype = None
Gx5733ModuleGetRevision.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetVThreshold = _libraries['libGxPio.so'].Gx5733ModuleGetVThreshold
Gx5733ModuleGetVThreshold.restype = None
Gx5733ModuleGetVThreshold.argtypes = [SHORT, SHORT, PDOUBLE, PSHORT]
Gx5733ModuleSetVThreshold = _libraries['libGxPio.so'].Gx5733ModuleSetVThreshold
Gx5733ModuleSetVThreshold.restype = None
Gx5733ModuleSetVThreshold.argtypes = [SHORT, SHORT, DOUBLE, PSHORT]
Gx5733ModuleBufferClear = _libraries['libGxPio.so'].Gx5733ModuleBufferClear
Gx5733ModuleBufferClear.restype = None
Gx5733ModuleBufferClear.argtypes = [SHORT, SHORT, PSHORT]
Gx5733ModuleBufferGetMode = _libraries['libGxPio.so'].Gx5733ModuleBufferGetMode
Gx5733ModuleBufferGetMode.restype = None
Gx5733ModuleBufferGetMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleBufferGetState = _libraries['libGxPio.so'].Gx5733ModuleBufferGetState
Gx5733ModuleBufferGetState.restype = None
Gx5733ModuleBufferGetState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleBufferSetMode = _libraries['libGxPio.so'].Gx5733ModuleBufferSetMode
Gx5733ModuleBufferSetMode.restype = None
Gx5733ModuleBufferSetMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleBufferReadData = _libraries['libGxPio.so'].Gx5733ModuleBufferReadData
Gx5733ModuleBufferReadData.restype = None
Gx5733ModuleBufferReadData.argtypes = [SHORT, SHORT, PDWORD, PDWORD, PSHORT]
Gx5733ModuleBufferWriteData = _libraries['libGxPio.so'].Gx5733ModuleBufferWriteData
Gx5733ModuleBufferWriteData.restype = None
Gx5733ModuleBufferWriteData.argtypes = [SHORT, SHORT, PDWORD, PDWORD, PSHORT]
Gx5733ModuleBufferTest = _libraries['libGxPio.so'].Gx5733ModuleBufferTest
Gx5733ModuleBufferTest.restype = None
Gx5733ModuleBufferTest.argtypes = [SHORT, SHORT, PSHORT]
Gx5733ModuleGetOperationMode = _libraries['libGxPio.so'].Gx5733ModuleGetOperationMode
Gx5733ModuleGetOperationMode.restype = None
Gx5733ModuleGetOperationMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleSetOperationMode = _libraries['libGxPio.so'].Gx5733ModuleSetOperationMode
Gx5733ModuleSetOperationMode.restype = None
Gx5733ModuleSetOperationMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleGetOutputMode = _libraries['libGxPio.so'].Gx5733ModuleGetOutputMode
Gx5733ModuleGetOutputMode.restype = None
Gx5733ModuleGetOutputMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleSetOutputMode = _libraries['libGxPio.so'].Gx5733ModuleSetOutputMode
Gx5733ModuleSetOutputMode.restype = None
Gx5733ModuleSetOutputMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleGetHandshakeOutputMode = _libraries['libGxPio.so'].Gx5733ModuleGetHandshakeOutputMode
Gx5733ModuleGetHandshakeOutputMode.restype = None
Gx5733ModuleGetHandshakeOutputMode.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleSetHandshakeOutputMode = _libraries['libGxPio.so'].Gx5733ModuleSetHandshakeOutputMode
Gx5733ModuleSetHandshakeOutputMode.restype = None
Gx5733ModuleSetHandshakeOutputMode.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleGetPort = _libraries['libGxPio.so'].Gx5733ModuleGetPort
Gx5733ModuleGetPort.restype = None
Gx5733ModuleGetPort.argtypes = [SHORT, SHORT, PDWORD, PSHORT]
Gx5733ModuleSetPort = _libraries['libGxPio.so'].Gx5733ModuleSetPort
Gx5733ModuleSetPort.restype = None
Gx5733ModuleSetPort.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5733ModuleGetExtStrobeEnablePolarity = _libraries['libGxPio.so'].Gx5733ModuleGetExtStrobeEnablePolarity
Gx5733ModuleGetExtStrobeEnablePolarity.restype = None
Gx5733ModuleGetExtStrobeEnablePolarity.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetExtStrobeEnableState = _libraries['libGxPio.so'].Gx5733ModuleGetExtStrobeEnableState
Gx5733ModuleGetExtStrobeEnableState.restype = None
Gx5733ModuleGetExtStrobeEnableState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetExtStrobePolarity = _libraries['libGxPio.so'].Gx5733ModuleGetExtStrobePolarity
Gx5733ModuleGetExtStrobePolarity.restype = None
Gx5733ModuleGetExtStrobePolarity.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetExtStrobeState = _libraries['libGxPio.so'].Gx5733ModuleGetExtStrobeState
Gx5733ModuleGetExtStrobeState.restype = None
Gx5733ModuleGetExtStrobeState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetInternalStrobeSource = _libraries['libGxPio.so'].Gx5733ModuleGetInternalStrobeSource
Gx5733ModuleGetInternalStrobeSource.restype = None
Gx5733ModuleGetInternalStrobeSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetOutputStrobeWidth = _libraries['libGxPio.so'].Gx5733ModuleGetOutputStrobeWidth
Gx5733ModuleGetOutputStrobeWidth.restype = None
Gx5733ModuleGetOutputStrobeWidth.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetStrobeSource = _libraries['libGxPio.so'].Gx5733ModuleGetStrobeSource
Gx5733ModuleGetStrobeSource.restype = None
Gx5733ModuleGetStrobeSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleSetExtStrobeEnablePolarity = _libraries['libGxPio.so'].Gx5733ModuleSetExtStrobeEnablePolarity
Gx5733ModuleSetExtStrobeEnablePolarity.restype = None
Gx5733ModuleSetExtStrobeEnablePolarity.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleSetExtStrobePolarity = _libraries['libGxPio.so'].Gx5733ModuleSetExtStrobePolarity
Gx5733ModuleSetExtStrobePolarity.restype = None
Gx5733ModuleSetExtStrobePolarity.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleSetInternalStrobeSource = _libraries['libGxPio.so'].Gx5733ModuleSetInternalStrobeSource
Gx5733ModuleSetInternalStrobeSource.restype = None
Gx5733ModuleSetInternalStrobeSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleSetOutputStrobeWidth = _libraries['libGxPio.so'].Gx5733ModuleSetOutputStrobeWidth
Gx5733ModuleSetOutputStrobeWidth.restype = None
Gx5733ModuleSetOutputStrobeWidth.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleSetStrobeSource = _libraries['libGxPio.so'].Gx5733ModuleSetStrobeSource
Gx5733ModuleSetStrobeSource.restype = None
Gx5733ModuleSetStrobeSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleGetPxiTriggerBus = _libraries['libGxPio.so'].Gx5733ModuleGetPxiTriggerBus
Gx5733ModuleGetPxiTriggerBus.restype = None
Gx5733ModuleGetPxiTriggerBus.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleGetPxiTriggerLine = _libraries['libGxPio.so'].Gx5733ModuleGetPxiTriggerLine
Gx5733ModuleGetPxiTriggerLine.restype = None
Gx5733ModuleGetPxiTriggerLine.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleSetPxiTriggerBus = _libraries['libGxPio.so'].Gx5733ModuleSetPxiTriggerBus
Gx5733ModuleSetPxiTriggerBus.restype = None
Gx5733ModuleSetPxiTriggerBus.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleSetPxiTriggerLine = _libraries['libGxPio.so'].Gx5733ModuleSetPxiTriggerLine
Gx5733ModuleSetPxiTriggerLine.restype = None
Gx5733ModuleSetPxiTriggerLine.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleStep = _libraries['libGxPio.so'].Gx5733ModuleStep
Gx5733ModuleStep.restype = None
Gx5733ModuleStep.argtypes = [SHORT, SHORT, DWORD, PSHORT]
Gx5733ModuleGetState = _libraries['libGxPio.so'].Gx5733ModuleGetState
Gx5733ModuleGetState.restype = None
Gx5733ModuleGetState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleHalt = _libraries['libGxPio.so'].Gx5733ModuleHalt
Gx5733ModuleHalt.restype = None
Gx5733ModuleHalt.argtypes = [SHORT, SHORT, PSHORT]
Gx5733ModuleRun = _libraries['libGxPio.so'].Gx5733ModuleRun
Gx5733ModuleRun.restype = None
Gx5733ModuleRun.argtypes = [SHORT, SHORT, PSHORT]
Gx5733ModuleSetTermination = _libraries['libGxPio.so'].Gx5733ModuleSetTermination
Gx5733ModuleSetTermination.restype = None
Gx5733ModuleSetTermination.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleGetTermination = _libraries['libGxPio.so'].Gx5733ModuleGetTermination
Gx5733ModuleGetTermination.restype = None
Gx5733ModuleGetTermination.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleSetDirection = _libraries['libGxPio.so'].Gx5733ModuleSetDirection
Gx5733ModuleSetDirection.restype = None
Gx5733ModuleSetDirection.argtypes = [SHORT, SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleGetDirection = _libraries['libGxPio.so'].Gx5733ModuleGetDirection
Gx5733ModuleGetDirection.restype = None
Gx5733ModuleGetDirection.argtypes = [SHORT, SHORT, SHORT, PSHORT, PSHORT]
Gx5733ModuleSetDirectionSource = _libraries['libGxPio.so'].Gx5733ModuleSetDirectionSource
Gx5733ModuleSetDirectionSource.restype = None
Gx5733ModuleSetDirectionSource.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733ModuleGetDirectionSource = _libraries['libGxPio.so'].Gx5733ModuleGetDirectionSource
Gx5733ModuleGetDirectionSource.restype = None
Gx5733ModuleGetDirectionSource.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733GetInternalClock = _libraries['libGxPio.so'].Gx5733GetInternalClock
Gx5733GetInternalClock.restype = None
Gx5733GetInternalClock.argtypes = [SHORT, SHORT, PSHORT, PDWORD, PSHORT]
Gx5733GetInternalClockEnable = _libraries['libGxPio.so'].Gx5733GetInternalClockEnable
Gx5733GetInternalClockEnable.restype = None
Gx5733GetInternalClockEnable.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733SetInternalClock = _libraries['libGxPio.so'].Gx5733SetInternalClock
Gx5733SetInternalClock.restype = None
Gx5733SetInternalClock.argtypes = [SHORT, SHORT, SHORT, DWORD, PSHORT]
Gx5733SetInternalClockEnable = _libraries['libGxPio.so'].Gx5733SetInternalClockEnable
Gx5733SetInternalClockEnable.restype = None
Gx5733SetInternalClockEnable.argtypes = [SHORT, SHORT, SHORT, PSHORT]
Gx5733GetStrobeToPxiTriggerBusState = _libraries['libGxPio.so'].Gx5733GetStrobeToPxiTriggerBusState
Gx5733GetStrobeToPxiTriggerBusState.restype = None
Gx5733GetStrobeToPxiTriggerBusState.argtypes = [SHORT, PSHORT, PSHORT]
Gx5733GetStrobeToPxiTriggerLineState = _libraries['libGxPio.so'].Gx5733GetStrobeToPxiTriggerLineState
Gx5733GetStrobeToPxiTriggerLineState.restype = None
Gx5733GetStrobeToPxiTriggerLineState.argtypes = [SHORT, SHORT, PSHORT, PSHORT]
Gx5733SetStrobeToPxiTriggerBusState = _libraries['libGxPio.so'].Gx5733SetStrobeToPxiTriggerBusState
Gx5733SetStrobeToPxiTriggerBusState.restype = None
Gx5733SetStrobeToPxiTriggerBusState.argtypes = [SHORT, SHORT, PSHORT]
Gx5733SetStrobeToPxiTriggerLineState = _libraries['libGxPio.so'].Gx5733SetStrobeToPxiTriggerLineState
Gx5733SetStrobeToPxiTriggerLineState.restype = None
Gx5733SetStrobeToPxiTriggerLineState.argtypes = [SHORT, SHORT, SHORT, PSHORT]
__all__ = ['GX5641_PXI_TRIGGER_LINE7', 'GX5641_PXI_TRIGGER_LINE6',
           'GX5641_PXI_TRIGGER_LINE5', 'GX5641_PXI_TRIGGER_LINE4',
           'GX5641_PXI_TRIGGER_LINE3', 'GX5733_DIGITAL_PORT_IO',
           'GX5641_PXI_TRIGGER_LINE1', 'GX5641_PXI_TRIGGER_LINE0',
           'Gx5642SetGroupMode', 'GX5733_MAX_CLOCK_DIVIDER',
           'GX5731_MODULE_INTERNAL_STROBE_NOT_CONNECTED',
           'Gx5733Panel', 'GX5641_PXI_TRIGGER_LINE2',
           'Gx5732SetPortWord',
           'Gx5732GetTerminalCountPortConnection',
           'GX5733_RS422_TTL_BIDIRECTIONAL_CONVERTER',
           'GX5731_PORT_IN_ONLY',
           'GX5641_CHANNEL_CONVERT_DIFFERENTIAL_TO_TTL',
           'GX5731_MODULE_GROUP0', 'GX5731_MODULE_GROUP1',
           'GXPIO_INVALID_STROBE_POLARITY',
           'GX5733_INTERNAL_CLOCK0_T0_PXI_CLOCK_10MHZ',
           'Gx5731GetInternalClockEnable',
           'Gx5733ModuleSetHandshakeOutputMode', 'Gx5731SetPortByte',
           'Gx5732GetCounterGate',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER0',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER1',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER2',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER3',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER4',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER5',
           'GX5733_INTERNAL_CLOCK0_T0_PCI_CLOCK_33MHZ',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER7',
           'Gx5732GetPortBit', 'Gx5733GetStrobeToPxiTriggerBusState',
           'Gx5732SetPortByte', 'Gx5731SetInternalClockEnable',
           'GXPIO_INVALID_CHANNEL_PORT_DIRECTION',
           'Gx5731ModuleSetOutputStrobeWidth', 'Gx5731ModuleGetState',
           'Gx5731SetPortBit', 'GX5732_INTERNAL_CLOCK_T0_USER_LINE4',
           'GX5732_INTERNAL_CLOCK_T0_USER_LINE5',
           'GX5732_INTERNAL_CLOCK_T0_USER_LINE2',
           'GX5732_INTERNAL_CLOCK_T0_USER_LINE3',
           'GX5732_INTERNAL_CLOCK_T0_USER_LINE0',
           'GX5732_INTERNAL_CLOCK_T0_USER_LINE1',
           'GX5733_PORT_HIGH_WORD', 'Gx5731ModuleSetVThreshold',
           'Gx5731SetPortWord', 'Gx5641Panel',
           'Gx5641SetGroupTTLPortDirection',
           'Gx5731ModuleSetDirectionSource',
           'Gx5733ModuleGetExtStrobeEnableState',
           'Gx5641GetChannelTTLPortDirection',
           'GX5731_MODULE_TERMINATION_ON', 'Gx5733ResetPort',
           'Gx5731ModuleSetPxiTriggerBus',
           'Gx5733ModuleGetExtStrobeState',
           'Gx5642SetGroupDifferentialPortDirection',
           'Gx5733InitializeVisa', 'Gx5641GetGroupMode',
           'Gx5733GetBoardSummary', 'GX5731_EXT_TRIGGER_LINE3',
           'GX5732_TERMINAL_COUNT_NEG_PULSE',
           'GX5642_PXI_TRIGGER_LINE1', 'GX5642_PXI_TRIGGER_LINE2',
           'Gx5732SetPort',
           'GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN4',
           'GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN5',
           'GXPIO_INVALID_BYTE', 'GX5642_PXI_TRIGGER_LINE3',
           'GX5733_MAX_BUFFER_SIZE',
           'GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN2',
           'GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK_IN3', 'INT',
           'GX5642_PXI_TRIGGER_LINE4', 'Gx5731ModuleSetStrobeSource',
           'Gx5732SetPortDirection', 'Gx5732GetCounterEnable',
           'Gx5733ModuleSetStrobeSource', 'GX5731_EXT_TRIGGER_LINE6',
           'Gx5642SetGroupConversionMode', 'Gx5642Reset',
           'GX5731_EXT_TRIGGER_LINE5',
           'Gx5731GetExtTriggerToPxiTriggerLine',
           'GX5642_CHANNEL_OUTPUT_DISABLE',
           'GX5731_EXT_TRIGGER_LINE4',
           'Gx5641GetChannelConversionMode', 'Gx5642SetGroupTTLPort',
           'GX5733_PXI_TRIGGER_LINE6', 'GX5732_NEGATIVE_EDGE',
           'Gx5642SetChannelOutputState',
           'GX5731_MODULE_OPERATION_PORT_IO',
           'Gx5733ModuleGetOutputMode', 'Gx5731ModuleGetVThreshold',
           'Gx5642GetGroupDifferentialPort', 'GX5733_RS422_PORT_IO',
           'Gx5731ModuleBufferSetMode', 'GXPIO_INVALID_DIRECTION',
           'Gx5733ModuleBufferGetMode',
           'GX5731_MODULE_BUFFER_MODE_HALF_FULL',
           'Gx5733ModuleSetDirectionSource', 'Gx5641GetGroupTTLPort',
           'Gx5733ModuleSetTermination', 'Gx5732SetInternalClock',
           'Gx5732GetCounterMode', 'Gx5731ModuleGetType',
           'GT_SLOT_NOT_CONFIG', 'GT_WRONG_BOARD',
           'Gx5731GetStrobeToPxiTriggerLineState', 'Gx5731GetPort',
           'GX5731_MIN_CLOCK_DIVIDER', 'GX5733_MODULE_GROUP0',
           'GX5733_MODULE_GROUP1', 'Gx5641SetChannelMode',
           'GXPIO_MODULE_BUFFER_OVERFLOW', 'GX5733_CLOCK1',
           'GX5733_CLOCK0', 'GX5642_PXI_TRIGGER_LINE0',
           'GX5731_EXT_TRIGGER_LINE2', 'GX5731_EXT_TRIGGER_LINE1',
           'GX5731_EXT_TRIGGER_LINE0', 'GX5731_EXT_TRIGGER_LINE7',
           'GX5642_PXI_TRIGGER_LINE5', 'GX5642_PXI_TRIGGER_LINE6',
           'GX5642_PXI_TRIGGER_LINE7', 'Gx5642SetChannelTTLPort',
           'GXPIO_INVALID_BIT', 'Gx5642SetChannelMode',
           'GX5731_MAX_BUFFER_SIZE', 'Gx5732GetCounterValue',
           'Gx5642GetGroupTTLPortDirection',
           'Gx5733ModuleSetOutputMode',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE3',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE2',
           'GX5732_MAX_CLOCK_DIVIDER',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE0',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE1',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE4',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_USERLINE5',
           'Gx5732GetPort', 'Gx5732Initialize',
           'GXPIO_INVALID_COUNTER_OR_ALL_TERMINAL_COUNT_AND_CLOCKS',
           'Gx5733ModuleGetDirectionSource',
           'GXPIO_INVALID_CLOCK_SOURCE', 'GX5731_MODULE_STATE_RUN',
           'GX5731_PORT_LOW_WORD', 'Gx5733GetPortDirection',
           'GX5731_PORT_DIRECTION_OUT', 'Gx5732Panel',
           'GX5733_PORT_IN_ONLY', 'PSHORT',
           'Gx5733ModuleSetPxiTriggerLine',
           'Gx5641GetChannelOutputState', 'GxPioGetErrorString',
           'GX5733_MODULE_STATE_HALT', 'GXPIO_INVALID_CHANNEL_MODE',
           'GX5732_TERMINAL_COUNT_OUPUT_COUNTER2',
           'GX5732_TERMINAL_COUNT_OUPUT_COUNTER3',
           'GX5732_TERMINAL_COUNT_OUPUT_COUNTER0',
           'GX5732_TERMINAL_COUNT_OUPUT_COUNTER1',
           'GX5732_COUNTER_GATE_CARRY_COUNTER1',
           'GX5731_DISABLE_INTERNAL_CLOCK',
           'Gx5641SetChannelConversionMode',
           'GX5733_MODULE_BUFFER_MODE_HALF_FULL',
           'Gx5733ModuleSetDirection', 'Gx5641GetGroupOutputState',
           'Gx5731GetPortBit', 'Gx5733ModuleGetPort',
           'Gx5641GetChannelDifferentialPortDirection',
           'Gx5733GetStrobeToPxiTriggerLineState',
           'GX5731_MODULE_STROBE_POSITIVE_EDGE', 'GX5731_PORT2',
           'GX5731_PORT1', 'GX5731_PORT0',
           'GX5731_MODULE_DIRECTION_OUTPUT', 'GX5731_PORT6',
           'GX5731_PORT5', 'GX5731_PORT4',
           'GX5641_CHANNEL_DIFFERENTIAL_PORT', 'GT_INVALID_MODE',
           'GXPIO_INVALID_WORD', 'LONG',
           'GX5733_MODULE_MAX_VTHRESHOLD', 'Gx5731ModuleBufferClear',
           'Gx5731ModuleGetPxiTriggerLine', 'GT_UNABLE_CREATE_PANEL',
           'Gx5733ModuleBufferReadData', 'Gx5731GetBoardSummary',
           'Gx5731SetStrobeToPxiTriggerLineState',
           'Gx5732SetCounterMode', 'PSTR', 'GXPIO_BUFFER_WRITE_FAIL',
           'Gx5733Initialize', 'GX5733_MODULE_STROBE_INTERNAL',
           'GX5733_MODULE_HANDSHAKE_OUTPUT_DISABLE',
           'Gx5731GetInternalClock', 'Gx5641GetChannelMode',
           'GX5731_MODULE_DIRECTION_SOURCE_EXTERNAL',
           'GX5731_MIN_BUFFER_SIZE', 'GX5732_COUNTER_TO_USER_LINE4',
           'GX5732_COUNTER_TO_USER_LINE5',
           'GX5732_COUNTER_TO_USER_LINE2',
           'GX5731_MODULE_INTERNAL_STROBE_T0_XTRIGGER6',
           'GX5732_COUNTER_TO_USER_LINE0',
           'GX5732_COUNTER_TO_USER_LINE1',
           'Gx5732LoadCounterCounterPort',
           'GX5731_MODULE_DIRECTION_DIFFERENTIAL_TO_TTL',
           'GX5731_MODULE_BUFFER_EMPTY',
           'GX5731_MODULE_HANDSHAKE_OUTPUT_DISABLE',
           'GX5731_NO_MODULE_INSTALLED', 'GX5733_PORT_DIRECTION_OUT',
           'Gx5731ModuleGetHandshakeOutputMode',
           'GX5731_MODULE_MIN_STROBE_WIDTH',
           'GX5733_DIGITAL_INPUT_LATCH',
           'GX5733_MODULE_MIN_VTHRESHOLD',
           'Gx5733ModuleBufferGetState', 'GX5733_MODULE_STATE_RUN',
           'Gx5731ModuleSetExtStrobePolarity',
           'GX5731_ENABLE_INTERNAL_CLOCK',
           'Gx5641SetChannelDifferentialPort', 'Gx5732InitializeVisa',
           'Gx5731ResetPort', 'Gx5733SetStrobeToPxiTriggerBusState',
           'GX5642_FIRST_CHANNEL',
           'Gx5641SetGroupDifferentialPortDirection',
           'GX5731_RS422_TTL_BIDIRECTIONAL_CONVERTER',
           'GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER5',
           'GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER4',
           'GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER7',
           'GX5731_INTERNAL_CLOCK1_T0_EXT_TRIGGER6',
           'GX5731_MODULE_OUTPUT_ENABLE',
           'Gx5733GetPortByteDirection',
           'GX5732_TERMINAL_COUNT_POS_PULSE', 'GXPIO_INVALID_DIVIDER',
           'Gx5642GetGroupConversionMode', 'PDOUBLE',
           'GT_UNABLE_ALLOC_DEVICE_RESOURCE',
           'GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK1',
           'GX5731_MODULE_INTERNAL_STROBE_T0_CLOCK0',
           'Gx5641LoadGroupDirectionFromDIPSwitch',
           'Gx5733GetPortWord', 'GXPIO_INVALID_GATE_SOURCE',
           'Gx5732GetPortByteDirection',
           'Gx5733ModuleGetHandshakeOutputMode',
           'GX5731_MODULE_HANDSHAKE_OUTPUT_ENABLE',
           'Gx5642GetChannelTTLPort', 'GX5642_CHANNEL_PORT_INPUT',
           'Gx5641ResetGroup', 'Gx5731ModuleSetOutputMode',
           'Gx5641GetChannelDifferentialPort',
           'Gx5733ModuleGetTermination', 'Gx5642GetChannelMode',
           'CHAR', 'GX5731_INTERNAL_CLOCK1_T0_PXI_CLOCK_10MHZ',
           'Gx5731ModuleSetPxiTriggerLine',
           'GX5733_PORT_DIRECTION_IN',
           'Gx5642SetChannelTTLPortDirection', 'Gx5731GetPortByte',
           'GX5733_INTERNAL_CLOCK0_NOT_CONNECTED',
           'GXPIO_INVALID_PORT',
           'GXPIO_INVALID_CLOCK_INTERNAL_SOURCE', 'Gx5641Reset',
           'Gx5642GetBoardSummary',
           'Gx5733ModuleGetExtStrobeEnablePolarity',
           'GX5733_LVDS_TTL_BIDIRECTIONAL_CONVERTER',
           'GX5731_DIGITAL_POWER_OUTPUT_LATCH',
           'GT_ERR_FUNCTION_NOT_SUPPORTED', 'GT_INVALID_ERROR',
           'GX5731_INTERNAL_CLOCK1_T0_CLOCK_IN1',
           'GX5733_MODULE_DIRECTION_SOURCE_EXTERNAL',
           'Gx5731ModuleGetExtStrobeEnableState',
           'GX5731_INTERNAL_CLOCK0_T0_PXI_CLOCK_10MHZ',
           'Gx5733ModuleSetPxiTriggerBus', 'Gx5731Reset',
           'GX5641_CHANNEL_MODE_CONVERSION', 'GX5732_COUNTER2',
           'GX5732_COUNTER3', 'GX5732_COUNTER0', 'GX5732_COUNTER1',
           'GX5642_CHANNEL_CONVERT_DIFFERENTIAL_TO_TTL',
           'Gx5733GetPortByte', 'Gx5642SetGroupOutputState',
           'Gx5641SetGroupMode', 'GXPIO_COUNTER_PORT_NOT_INPUT',
           'Gx5641GetBoardSummary', 'Gx5731ModuleGetOperationMode',
           'GX5733_MODULE_INTERNAL_STROBE_T0_CLOCK1',
           'GX5733_MODULE_INTERNAL_STROBE_T0_CLOCK0',
           'Gx5731GetPortWord', 'Gx5733ModuleBufferWriteData',
           'GT_INVALID_SLOT', 'GT_UNABLE_TO_GETTIMER',
           'Gx5732SetCounterClock', 'Gx5732Reset', 'DWORD',
           'GX5731_DIGITAL_INPUT_LATCH',
           'GX5731_MODULE_DIRECTION_INPUT',
           'Gx5731ModuleGetExtStrobeEnablePolarity',
           'GX5732_COUNTER_GATE_ENABLE_ALWAYS', 'GX5732_PORT0',
           'GX5732_PORT1', 'GXPIO_INVALID_CHANNEL', 'GX5732_PORT3',
           'GX5732_PORT4', 'GX5732_PORT5', 'GX5732_PORT6',
           'GXPIO_INVALID_PXI_TRIGGER_LINE',
           'Gx5733ModuleGetRevision',
           'Gx5733SetStrobeToPxiTriggerLineState',
           'Gx5731SetPortDirection', 'GX5731_MODULE_BUFFER_FULL',
           'Gx5731GetPortDirection', 'PBYTE', 'GX5733_PORT_BYTE1',
           'GX5733_PORT_BYTE0', 'GX5733_PORT_BYTE3',
           'GX5733_PORT_BYTE2', 'PWORD', 'GX5641_GROUP0',
           'GX5641_GROUP1', 'GX5642_CHANNEL_MODE_STATIC_IO', 'PVOID',
           'Gx5641GetChannelTTLPort', 'GX5731_MODULE_STROBE_EXTERNAL',
           'Gx5732SetCounterValue', 'GT_UNABLE_REGISTER_DEVICE',
           'Gx5733SetPortDirection', 'WORD',
           'GX5731_LVDS_TTL_BIDIRECTIONAL_CONVERTER',
           'Gx5732GetCounterPort', 'Gx5732ResetCounter',
           'GX5733_PORT1', 'GX5733_PORT0', 'GX5733_PORT3',
           'GX5733_PORT2', 'GX5733_PXI_TRIGGER_LINE5',
           'GX5733_PXI_TRIGGER_LINE4', 'GX5733_PXI_TRIGGER_LINE7',
           'GX5733_MODULE_INTERNAL_STROBE_NOT_CONNECTED',
           'GX5733_PXI_TRIGGER_LINE1', 'GX5733_PXI_TRIGGER_LINE0',
           'GX5733_PXI_TRIGGER_LINE3', 'GX5733_PXI_TRIGGER_LINE2',
           'Gx5733ModuleGetOutputStrobeWidth',
           'Gx5731ModuleBufferGetMode',
           'Gx5731SetExtTriggerToPxiTriggerBus',
           'Gx5641InitializeVisa', 'PDWORD',
           'GX5733_NO_MODULE_INSTALLED',
           'Gx5641GetGroupDifferentialPort',
           'GX5732_TERMINAL_COUNT_OUPUT_ALLCOUNTERS_AND_CLOCKS',
           'GX5733_PXI_TRIGGER_LINE_DISCONNECTED',
           'Gx5731ModuleSetTermination',
           'Gx5733ModuleSetExtStrobeEnablePolarity', 'GX5731_PORT3',
           'Gx5731Panel', 'Gx5733ModuleSetOperationMode',
           'Gx5642Initialize', 'GX5642_CHANNEL_OUTPUT_ENABLE',
           'Gx5731ModuleGetExtStrobeState',
           'Gx5731ModuleSetExtStrobeEnablePolarity',
           'GXPIO_INVALID_CLOCK',
           'GX5731_MODULE_DIRECTION_TTL_TO_DIFFERENTIAL',
           'Gx5731ModuleGetPxiTriggerBus', 'SHORT',
           'Gx5733GetInternalClock', 'GX5731_DIGITAL_PORT_IO',
           'GX5641_CHANNEL_TTL_PORT',
           'GX5733_MODULE_OPERATION_PORT_IO', 'Gx5641Initialize',
           'GX5732_COUNTER_PORT_DIRECTION_IN',
           'GX5733_ENABLE_INTERNAL_CLOCK',
           'GX5733_INTERNAL_CLOCK1_T0_STAR_TRIGGER',
           'Gx5733ModuleSetInternalStrobeSource',
           'Gx5641GetPxiTriggerBusToGroupOutputState',
           'Gx5733SetPortBit', 'GXPIO_UNABLE_TO_EMPTY_BUFFER',
           'Gx5733ModuleGetVThreshold',
           'GX5733_MODULE_DIRECTION_TTL_TO_DIFFERENTIAL',
           'GX5733_MODULE_TERMINATION_ON',
           'GX5731_MODULE_OPERATION_BUFFERED', 'GT_INVALID_PARAMETER',
           'Gx5733ModuleGetType', 'Gx5731SetInternalClock',
           'Gx5733ModuleGetExtStrobePolarity', 'Gx5732GetPortWord',
           'GX5641_CHANNEL_MODE_STATIC_IO', 'Gx5733SetPortWord',
           'Gx5641GetGroupDifferentialPortDirection',
           'Gx5641SetGroupConversionMode', 'Gx5641SetGroupTTLPort',
           'GX5732_COUNTER_GATE_USER_LINE2',
           'GX5732_COUNTER_GATE_USER_LINE3',
           'GX5732_COUNTER_GATE_USER_LINE0',
           'GX5732_COUNTER_GATE_USER_LINE1',
           'Gx5733ModuleGetOperationMode',
           'GX5732_COUNTER_GATE_USER_LINE4',
           'GX5732_COUNTER_GATE_USER_LINE5',
           'GX5733_MIN_CLOCK_DIVIDER', 'GX5641_CHANNEL_OUTPUT_ENABLE',
           'GXPIO_INVALID_STROBE_SOURCE',
           'Gx5732SetTerminalCountPortConnection', 'GX5731_CLOCK1',
           'GX5731_CLOCK0', 'GX5731_PORT_HIGH_WORD',
           'GX5642_CHANNEL_TTL_PORT',
           'GX5733_INTERNAL_CLOCK0_T0_STAR_TRIGGER',
           'Gx5733SetInternalClock', 'Gx5733ModuleBufferSetMode',
           'Gx5732SetCounterEnable',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_NONE',
           'Gx5642LoadGroupDirectionFromDIPSwitch',
           'GX5731_PXI_TRIGGER_LINE_DISCONNECTED',
           'Gx5642GetChannelConversionMode', 'Gx5731InitializeVisa',
           'Gx5733ModuleGetPxiTriggerLine',
           'GX5732_MIN_CLOCK_DIVIDER',
           'GX5731_INTERNAL_CLOCK0_T0_STAR_TRIGGER',
           'GXPIO_BUFFER_TEST_FAIL', 'Gx5731ModuleBufferReadData',
           'Gx5642SetChannelDifferentialPortDirection',
           'Gx5642GetGroupDifferentialPortDirection',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER2',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER3',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER0',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER1',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER6',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER7',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER4',
           'GX5733_MODULE_INTERNAL_STROBE_T0_XTRIGGER5',
           'Gx5642GetPxiTriggerBusToGroupOutputState',
           'Gx5733ModuleGetState', 'BYTE', 'GX5732_PORT_BYTE2',
           'GX5732_PORT_BYTE3', 'GX5732_PORT_BYTE0',
           'GX5732_PORT_BYTE1', 'Gx5731ModuleGetPort',
           'Gx5733ModuleSetExtStrobePolarity',
           'Gx5642SetGroupDifferentialPort', 'GT_NOT_CALIBRATED',
           'Gx5731ModuleBufferWriteData',
           'Gx5642GetChannelDifferentialPort',
           'Gx5731SetStrobeToPxiTriggerBusState',
           'Gx5642SetPxiTriggerBusToGroupOutputState',
           'GX5731_RS422_PORT_IO',
           'GX5731_INTERNAL_CLOCK1_T0_PCI_CLOCK_33MHZ',
           'GT_BOARD_INVALID_EEPROM', 'Gx5642Panel',
           'Gx5731ModuleSetOperationMode',
           'Gx5731ModuleSetHandshakeOutputMode',
           'Gx5642GetGroupTTLPort',
           'Gx5733ModuleSetOutputStrobeWidth',
           'Gx5642SetGroupTTLPortDirection',
           'Gx5641SetGroupOutputState', 'GT_CANT_OPEN_HW',
           'Gx5731ModuleGetDirectionSource',
           'Gx5642GetChannelOutputState',
           'GXPIO_INVALID_INTERNAL_STROBE_SOURCE',
           'Gx5641SetGroupDifferentialPort',
           'Gx5731ModuleGetOutputMode', 'GX5731_PORT_DIRECTION_IN',
           'Gx5731ModuleGetTermination', 'Gx5731ModuleSetPort',
           'Gx5731ModuleGetDirection', 'GX5733_MODULE_BUFFER_EMPTY',
           'GXPIO_BUFFER_READ_FAIL', 'GXPIO_INVALID_BUFFER_SIZE',
           'Gx5733ModuleBufferTest',
           'GX5733_PXI_TRIGGER_LINE_CONNECTED',
           'GX5732_PORT_HIGH_WORD', 'GxPioGetDriverSummary',
           'Gx5731ModuleBufferGetState', 'UINT',
           'GX5733_DIGITAL_OUTPUT_LATCH', 'GX5731_PXI_TRIGGER_LINE3',
           'GX5731_PXI_TRIGGER_LINE2', 'GX5731_PXI_TRIGGER_LINE1',
           'GX5731_PXI_TRIGGER_LINE0', 'GX5731_PXI_TRIGGER_LINE7',
           'GX5731_PXI_TRIGGER_LINE6', 'GX5731_PXI_TRIGGER_LINE5',
           'GX5731_PXI_TRIGGER_LINE4', 'GX5733_PORT_LOW_WORD',
           'GT_UNABLE_ALLOC_MEMORY', 'GX5731_MODULE_MAX_STROBE_WIDTH',
           'Gx5733SetPortByte', 'GX5731_MODULE_BUFFER_MODE_FULL',
           'GX5733_MODULE_TERMINATION_OFF',
           'Gx5731ModuleGetStrobeSource',
           'GX5732_COUNTER_PORT_LOAD_CONTROL_IMMEDIATE',
           'GX5733_MODULE_OPERATION_BUFFERED', 'Gx5731ModuleRun',
           'Gx5733ModuleGetInternalStrobeSource', 'GX5731_PORT_BYTE3',
           'GX5731_PORT_BYTE2', 'GX5731_PORT_BYTE1',
           'GX5731_PORT_BYTE0', 'GT_NO_ERROR',
           'GX5731_MODULE_STROBE_NEGATIVE_EDGE',
           'GXPIO_INVALID_CHANNEL_STATE', 'Gx5641SetChannelTTLPort',
           'GX5642_LAST_CHANNEL', 'GX5732_TERMINAL_COUNT_POS_SQUARE',
           'GT_INVALID_STRLEN', 'GX5733_MODULE_DIRECTION_INPUT',
           'GX5731_INTERNAL_CLOCK0_T0_PCI_CLOCK_33MHZ',
           'Gx5733ModuleStep', 'GX5731_INTERNAL_CLOCK0_T0_CLOCK_IN0',
           'GX5731_DIGITAL_OUTPUT_LATCH',
           'GX5733_MODULE_OUTPUT_DISABLE',
           'GX5641_CHANNEL_CONVERT_TTL_TO_DIFFERENTIAL',
           'GT_BOARD_NOT_EXIST', 'GX5642_CHANNEL_MODE_CONVERSION',
           'Gx5733ModuleBufferClear', 'Gx5642GetGroupMode',
           'GX5641_CHANNEL_PORT_INPUT',
           'GX5731_PXI_TRIGGER_LINE_CONNECTED',
           'Gx5641SetPxiTriggerBusToGroupOutputState', 'GX5732_PORT2',
           'GX5732_COUNTER_TO_USER_LINE3',
           'Gx5641SetChannelTTLPortDirection',
           'Gx5731ModuleSetDirection', 'DOUBLE',
           'GX5733_MODULE_DIRECTION_SOURCE_INTERNAL',
           'Gx5642ResetGroup', 'GXPIO_PANEL_MODELESS',
           'Gx5642SetChannelConversionMode',
           'Gx5731ModuleGetInternalStrobeSource',
           'GX5731_MAX_CLOCK_DIVIDER', 'PLONG',
           'GX5733_DISABLE_INTERNAL_CLOCK', 'Gx5732SetPortBit',
           'Gx5641GetGroupConversionMode',
           'GX5733_MODULE_HANDSHAKE_OUTPUT_ENABLE',
           'GXPIO_INVALID_IN_LOAD_CONTROL', 'Gx5731ModuleGetRevision',
           'Gx5641GetGroupTTLPortDirection', 'GX5641_FIRST_CHANNEL',
           'Gx5733SetPortByteDirection', 'Gx5733ModuleGetDirection',
           'Gx5732GetPortByte', 'Gx5731SetExtTriggerToPxiTriggerLine',
           'GX5642_CHANNEL_CONVERT_TTL_TO_DIFFERENTIAL',
           'GX5733_INTERNAL_CLOCK1_T0_PXI_CLOCK_10MHZ',
           'GXPIO_INVALID_GROUP', 'Gx5733GetInternalClockEnable',
           'PBOOL', 'GX5731_MODULE_DIRECTION_SOURCE_INTERNAL',
           'GX5731_MODULE_MAX_VTHRESHOLD', 'GXPIO_INVALID_TC_MODE',
           'Gx5731ModuleBufferTest', 'Gx5733ModuleSetPort',
           'GX5731_MODULE_OUTPUT_DISABLE',
           'Gx5731ModuleGetExtStrobePolarity', 'GXPIO_PANEL_MODAL',
           'Gx5731GetExtTriggerToPxiTriggerBus',
           'GX5733_MODULE_DIRECTION_OUTPUT',
           'Gx5731ModuleSetInternalStrobeSource',
           'GX5641_CHANNEL_OUTPUT_DISABLE', 'GX5642_GROUP1',
           'GX5642_GROUP0', 'GX5733_MODULE_STROBE_POSITIVE_EDGE',
           'Gx5641SetChannelDifferentialPortDirection',
           'GX5731_COUNTER_TO_CLOCK1', 'GX5731_COUNTER_TO_CLOCK0',
           'GX5732_COUNTER_PORT_DIRECTION_OUT',
           'Gx5732GetCounterClock', 'Gx5733ModuleRun',
           'GX5733_MODULE_DIRECTION_DIFFERENTIAL_TO_TTL', 'PCSTR',
           'GX5642_CHANNEL_PORT_OUTPUT',
           'Gx5642SetChannelDifferentialPort',
           'GX5733_MODULE_BUFFER_FULL', 'GT_NOT_IN_CALIBRATION_MODE',
           'Gx5732SetCounterPort', 'GX5731_MODULE_TERMINATION_OFF',
           'Gx5642GetGroupOutputState', 'Gx5732GetPortDirection',
           'GX5732_PORT_LOW_WORD', 'GX5732_POSITIVE_EDGE',
           'GX5733_INTERNAL_CLOCK1_NOT_CONNECTED',
           'Gx5731GetPortByteDirection',
           'GX5733_MODULE_OUTPUT_ENABLE',
           'GX5732_INTERNAL_CLOCK_T0_PCI_CLOCK_33MHZ',
           'Gx5641SetChannelOutputState', 'Gx5731Initialize',
           'GX5733_MODULE_STROBE_EXTERNAL',
           'GX5642_CHANNEL_DIFFERENTIAL_PORT',
           'GX5731_MODULE_STROBE_INTERNAL', 'Gx5731ModuleStep',
           'Gx5733GetPort', 'Gx5733ModuleHalt', 'Gx5731ModuleHalt',
           'GX5733_MODULE_MAX_STROBE_WIDTH',
           'GXPIO_INVALID_CHANNEL_CONVERSION_MODE',
           'Gx5731ModuleGetOutputStrobeWidth', 'BOOL',
           'Gx5642GetChannelDifferentialPortDirection',
           'GX5641_LAST_CHANNEL',
           'GX5733_INTERNAL_CLOCK1_T0_PCI_CLOCK_33MHZ',
           'Gx5731SetPort', 'Gx5733Reset', 'Gx5732GetBoardSummary',
           'Gx5733ModuleSetVThreshold', 'GX5641_CHANNEL_PORT_OUTPUT',
           'GT_PARAMETER_OUT_OF_RANGE', 'GX5731_MODULE_STATE_HALT',
           'Gx5733ModuleGetStrobeSource', 'GX5733_MIN_BUFFER_SIZE',
           'GX5731_INTERNAL_CLOCK1_T0_STAR_TRIGGER',
           'GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER0',
           'GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER1',
           'GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER2',
           'GX5731_INTERNAL_CLOCK0_T0_EXT_TRIGGER3',
           'GX5733_MODULE_MIN_STROBE_WIDTH', 'Gx5642InitializeVisa',
           'HWND', 'Gx5732GetInternalClock', 'Gx5732ResetPort',
           'Gx5731GetStrobeToPxiTriggerBusState', 'Gx5733GetPortBit',
           'Gx5731SetPortByteDirection',
           'Gx5733ModuleGetPxiTriggerBus',
           'GX5733_DIGITAL_POWER_OUTPUT_LATCH', 'Gx5733SetPort',
           'Gx5733SetInternalClockEnable', 'GXPIO_INVALID_COUNTER',
           'GX5731_MODULE_MIN_VTHRESHOLD',
           'Gx5642GetChannelTTLPortDirection',
           'GX5732_TERMINAL_COUNT_NEG_SQUARE',
           'Gx5732SetPortByteDirection', 'Gx5732SetCounterGate',
           'GX5732_INTERNAL_CLOCK_T0_PXI_CLOCK_10MHZ',
           'GX5733_MODULE_BUFFER_MODE_FULL',
           'GX5733_MODULE_STROBE_NEGATIVE_EDGE', 'GT_INVALID_HANDLE']
