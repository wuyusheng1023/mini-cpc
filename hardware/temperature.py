from RPi import GPIO

from time import sleep

from . import hardware_config as config


def send_byte(byte):
  for _ in range(8):
    GPIO.output(config.GPIO_CLK, GPIO.HIGH)
    if (byte & 0x80):
      GPIO.output(config.GPIO_MOSI, GPIO.HIGH)
    else:
      GPIO.output(config.GPIO_MOSI, GPIO.LOW)
    byte <<= 1
    GPIO.output(config.GPIO_CLK, GPIO.LOW)

def write_register(gpio):
    GPIO.output(gpio, GPIO.LOW)
    send_byte(0x80 | 0) # 0x8x to specify 'write register value', first byte is address byte
    send_byte(0xC3) # the rest are data bytes
    GPIO.output(gpio, GPIO.HIGH)

def recv_byte():
  byte = 0x00
  for _ in range(8):
    GPIO.output(config.GPIO_CLK, GPIO.HIGH)
    byte <<= 1
    if GPIO.input(config.GPIO_MISO):
      byte |= 0x1
    GPIO.output(config.GPIO_CLK, GPIO.LOW)
  return byte


class TemperatureSensor:

  def __init__(self, gpio):
    self.gpio = gpio
    write_register(gpio)
    sleep(0.1)

  def read_registers(self):
    out = []
    GPIO.output(self.gpio, GPIO.LOW)
    send_byte(0)
    for _ in range(8):
      data = recv_byte()
      out.append(data)
    GPIO.output(self.gpio, GPIO.HIGH)
    return out

  @property
  def data(self):
    out = self.read_registers() #read all registers
    rtd_msb, rtd_lsb = out[1], out[2]
    rtd_adc_code = ((rtd_msb << 8) | rtd_lsb) >> 1 #acquire ADC_code
    temp = (rtd_adc_code / 32.0) - 256.0 #calculate temperature in celsius
    return temp
