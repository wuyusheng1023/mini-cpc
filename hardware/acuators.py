from RPi import GPIO
from simple_pid import PID

from configparser import ConfigParser


config = ConfigParser()
config.read('settings.ini')


class Acuator:

  def __init__(self, name, gpio, pid_params):
    self.on = True
    self.name = name
    settings = config['SETTINGS']
    self.setpoint = float(settings[self.name.lower()])
    self.pid = PID(
      pid_params['P'],
      pid_params['I'],
      pid_params['D'],
      self.setpoint,
    )
    self.pwm = GPIO.PWM(gpio, pid_params['FREQUENCY'])
  
  def update(self, value, upper_limit=75, scale=1):
    if self.on:
      duty_cycle = self.pid(value)
      if duty_cycle > upper_limit:
        duty_cycle = upper_limit
      elif duty_cycle < 0:
        duty_cycle = 0
      duty_cycle *= 1
    else:
      duty_cycle = 0
    self.pwm.ChangeDutyCycle(duty_cycle)

  def reload(self):
    settings = config['SETTINGS']
    self.setpoint = float(settings[self.name.lower()])
  
  def on(self):
    self.on = True
  
  def off(self):
    self.on = False
    