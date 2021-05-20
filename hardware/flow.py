from smbus2 import SMBus

from configparser import ConfigParser


config = ConfigParser()
config.read('settings.ini')


class FlowSensor:

  def __init__(self):
    self.bus = SMBus(1)
    self.coef = 1

  @property
  def data(self):
    data = self.bus.read_i2c_block_data(0x07, 0, 2)
    flow = self.coef * ((data[0] << 8) + data[1]) / 1000 # LPM
    return flow
  
  def reload(self):
    self.coef = config['SETTINGS']['flow_coef']
