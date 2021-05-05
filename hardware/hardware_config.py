from RPi import GPIO


# list of GPIO
PIN_3 = 2
PIN_5 = 3
PIN_7 = 4
PIN_11 = 17
PIN_12 = 18
PIN_13 = 27
PIN_15 = 22
PIN_16 = 23
PIN_18 = 24
PIN_19 = 10
PIN_21 = 9
PIN_22 = 25
PIN_23 = 11
PIN_24 = 8
PIN_26 = 7
PIN_27 = 0
PIN_28 = 1
PIN_29 = 5
PIN_31 = 6
PIN_32 = 12
PIN_33 = 13
PIN_35 = 19
PIN_36 = 16
PIN_37 = 26
PIN_38 = 20
PIN_40 = 21

# wiring input:
GPIO_OPC = PIN_36
GPIO_LIQUID_LEVEL = PIN_29
GPIO_MISO = PIN_21

# wiring outut:
GPIO_SATURATOR_HEATER = PIN_15
GPIO_CONDENSOR_COOLOR = PIN_22
GPIO_OPTICS_HEATER = PIN_16
GPIO_AIR_PUMP = PIN_13
GPIO_LIQUID_PUMP = PIN_18
GPIO_SATURATOR_TEMPERATURE = PIN_31
GPIO_CONDENSOR_TEMPERATURE = PIN_11
GPIO_OPTICS_TEMPERATURE = PIN_37
GPIO_MOSI = PIN_19
GPIO_CLK = PIN_23

# initialize GPIO
GPIO.cleanup()  # Reset ports
GPIO.setwarnings(False)  # do not show any warnings
GPIO.setmode(GPIO.BCM)  # programming the GPIO by BCM pin numbers.
GPIO.setup(GPIO_OPC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # input, counter
GPIO.setup(GPIO_LIQUID_LEVEL, GPIO.IN)  # input
GPIO.setup(GPIO_SATURATOR_HEATER, GPIO.OUT)  # output, saturator heater
GPIO.setup(GPIO_CONDENSOR_COOLOR, GPIO.OUT)  # output, cooler
GPIO.setup(GPIO_OPTICS_HEATER, GPIO.OUT)  # output, saturator heater
GPIO.setup(GPIO_AIR_PUMP, GPIO.OUT)  # output
GPIO.setup(GPIO_LIQUID_PUMP, GPIO.OUT)  # output
# saturator temperature ADC Chip Select pin
GPIO.setup(GPIO_SATURATOR_TEMPERATURE, GPIO.OUT)
# condenser temperature ADC Chip Select pin
GPIO.setup(GPIO_CONDENSOR_TEMPERATURE, GPIO.OUT)
# OPC temperature ADC Chip Select pin
GPIO.setup(GPIO_OPTICS_TEMPERATURE, GPIO.OUT)
GPIO.setup(GPIO_MISO, GPIO.IN)  # define MISO-pin for SPI communication
GPIO.setup(GPIO_MOSI, GPIO.OUT)  # define MOSI-pin for SPI communication
GPIO.setup(GPIO_CLK, GPIO.OUT)  # define CLK-pin for SPI communication

# set chip select pin to high according to datasheet
GPIO.output(GPIO_SATURATOR_TEMPERATURE, GPIO.HIGH)
# set chip select pin to high according to datasheet
GPIO.output(GPIO_CONDENSOR_TEMPERATURE, GPIO.HIGH)
# set chip select pin to high according to datasheet
GPIO.output(GPIO_OPTICS_TEMPERATURE, GPIO.HIGH)
GPIO.output(GPIO_MOSI, GPIO.LOW)  # set set mosi low
GPIO.output(GPIO_CLK, GPIO.LOW)  # set serial clock low

# PID parameters
SATURATOP_PID = {
    'P': 1,
    'I': 1,
    'D': 1,
}
CONDENSOR_PID = {
    'P': 1,
    'I': 1,
    'D': 1,
}
OPTICS_PID = {
    'P': 1,
    'I': 1,
    'D': 1,
}
AIR_PUMP_PID = {
    'P': 1,
    'I': 1,
    'D': 1,
}
