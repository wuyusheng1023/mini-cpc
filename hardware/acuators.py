from RPi import GPIO
from simple_pid import PID

from configparser import ConfigParser


class Acuator():

  def __init__(self, name, gpio, pid_params):
    self.name = name
    settings = ConfigParser().read('settings.ini')['SETTINGS']
    self.setpoint = float(settings[self.name.lower()])
    self.pid = PID(
      pid_params['P'],
      pid_params['I'],
      pid_params['D'],
      self.setpoint,
    )
    self.pwm = GPIO.PWM(gpio, pid_params['FREQUENCY'])
  
  def update(self, value, upper_limit=75, scale=1):
    duty_cycle = self.pid(value)
    if duty_cycle > upper_limit:
      duty_cycle = upper_limit
    elif duty_cycle < 0:
      duty_cycle = 0
    duty_cycle *= 1
    self.pwm(duty_cycle)

  def reload(self):
    settings = ConfigParser().read('settings.ini')['SETTINGS']
    self.setpoint = float(settings[self.name.lower()])
