from configparser import ConfigParser
from datetime import datetime

import config
from hardware.temperature import TemperatureSensor
from hardware.flow import FlowSensor
from hardware.acuators import Acuator
from hardware.io import DigitalInput, DigitaolOutput


settings = ConfigParser().read('settings.ini')['SETTINGS']


class Instrument():

  def __init__(self):
    self.on = True
    self.saturator_temperature_sensor = TemperatureSensor(config.GPIO_SATURATOR_TEMPERATURE)
    self.condensor_temperature_sensor = TemperatureSensor(config.GPIO_CONDENSOR_TEMPERATURE)
    self.optics_temperature_sensor = TemperatureSensor(config.GPIO_OPTICS_TEMPERATURE)
    self.flow_sensor = FlowSensor()
    self.liquid_level = DigitalInput(config.GPIO_LIQUID_LEVEL)
    self.saturator_heater = Acuator(
      name='saturator_temperature',
      gpio=config.GPIO_SATURATOR_HEATER,
      pid_params=config.SATURATOP_PID,
    )
    self.condensor_coolor = Acuator(
      name='condensor_temperature',
      gpio=config.GPIO_CONDENSOR_COOLOR,
      pid_params=config.CONDENSOR_PID,
    )
    self.optics_heater = Acuator(
      name='optics_temperature',
      gpio=config.GPIO_OPTICS_HEATER,
      pid_params=config.OPTICS_PID,
    )
    self.air_pump = Acuator(
      name='sample_flow',
      gpio=config.GPIO_AIR_PUMP,
      pid_params=config.AIR_PUMP_PID,
    )
    self.liquid_pump = DigitaolOutput(config.GPIO_LIQUID_PUMP)

  @property
  def status(self):
    return {
      'datetime_utc': datetime.utcnow(),
      'status': 'on' if self.on else 'off',
      'saturator_temperature': self.saturator_temperature_sensor.data,
      'condensor_temperature': self.condensor_temperature_sensor.data,
      'optics_temperature': self.optics_temperature_sensor.data,
      'flow': self.flow_sensor.data,
      'liquid_level': self.liquid_level.data,
    }
  
  def update(self):
    status = self.status
    if self.on:
      self.saturator_heater.update(status['saturator_temperature'])
      self.condensor_coolor.update(
        2 * self.condensor_coolor.setpoint - status['condensor_temperature']
      )
      self.saturator_heater.update(status['saturator_temperature'])
      self.air_pump.update(status['flow'])
      if status['liquid_level']:
        self.liquid_pump.off()
      else:
        self.liquid_pump.on()
    return status

    def reload(self):
      self.saturator_heater.reload()
      self.condensor_coolor.reload()
      self.optics_heater.reload()
      self.flow_sensor.reload()
  
  def on(self):
    self.on = True
    self.saturator_heater.off()
    self.condensor_coolor.off()
    self.optics_heater.off()
    self.air_pump.off()
    self.liquid_pump.off()
  
  def off(self):
    self.on = False
    self.saturator_heater.off()
    self.condensor_coolor.off()
    self.optics_heater.off()
    self.air_pump.off()
    self.liquid_pump.off()
