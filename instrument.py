from configparser import ConfigParser
from datetime import datetime

from hardware import hardware_config as config
from hardware.temperature import TemperatureSensor
from hardware.flow import FlowSensor
from hardware.acuators import Acuator
from hardware.io import DigitalInput, DigitalOutput


class Instrument:

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
    self.liquid_pump = DigitalOutput(config.GPIO_LIQUID_PUMP)

  @property
  def status(self):
    return {
      'datetime_utc': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
      'status': 'on' if self.on else 'off',
      'saturator_temperature': self.saturator_temperature_sensor.data,
      'condensor_temperature': self.condensor_temperature_sensor.data,
      'optics_temperature': self.optics_temperature_sensor.data,
      'sample_flow': self.flow_sensor.data,
      'liquid_level': self.liquid_level.data,
    }
  
  def update(self):
    status = self.status
    self.saturator_heater.update(status['saturator_temperature'])
    self.condensor_coolor.update(
      2 * self.condensor_coolor.setpoint - status['condensor_temperature']
    )
    self.optics_heater.update(status['optics_temperature'])
    self.air_pump.update(status['sample_flow'])
    if status['liquid_level']:
      self.liquid_pump.stop()
    else:
      self.liquid_pump.start()
    return status

  def reload(self):
    self.saturator_heater.reload()
    self.condensor_coolor.reload()
    self.optics_heater.reload()
  
  def start(self):
    self.on = True
    self.saturator_heater.start()
    self.condensor_coolor.start()
    self.optics_heater.start()
    self.air_pump.start()
  
  def stop(self):
    self.on = False
    self.saturator_heater.stop()
    self.condensor_coolor.stop()
    self.optics_heater.stop()
    self.air_pump.stop()
    self.liquid_pump.stop()


if __name__ == '__main__':
  instr = Instrument()
  instr.start()
  instr.stop()
