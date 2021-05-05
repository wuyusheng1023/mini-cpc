from smbus2 import SMBus

from configparser import ConfigParser


class FlowSensor:

  def __init__(self):
    self.bus = SMBus(1)
    self.coef = float(ConfigParser().read('settings.ini')['SETTINGS']['flow_coef'])

  @property
  def data(self):
    data = self.bus.read_i2c_block_data(0x07, 0, 2)
    flow = self.coef * ((data[0] << 8) + data[1]) / 1000 # LPM
    return flow
  
  def reload(self):
    self.coef = ConfigParser().read('settings.ini')['SETTINGS']['flow_coef']
