from RPi import GPIO
from simple_pid import PID

from configparser import ConfigParser


config = ConfigParser()


class Acuator:

  def __init__(self, name, gpio, pid_params):
    self.on = True
    self.name = name
    self.gpio = gpio
    config.read('settings.ini')
    settings = config['SETTINGS']
    self.setpoint = float(settings[self.name.lower()])
    self.pid_params = pid_params
    self.pid = PID(
      self.pid_params['P'],
      self.pid_params['I'],
      self.pid_params['D'],
      self.setpoint,
    )
    self.pwm = GPIO.PWM(self.gpio, self.pid_params['FREQUENCY'])

  def __repr__(self):
    return f'Acuator: {self.name}, GPIO: {self.gpio}, setpoint: {self.setpoint}'
  
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
    print(f'{self}, duty cycle: {duty_cycle}')
    self.pwm.ChangeDutyCycle(duty_cycle)

  def reload(self):
    config.read('settings.ini')
    settings = config['SETTINGS']
    self.setpoint = float(settings[self.name.lower()])
    self.pid = PID(
      self.pid_params['P'],
      self.pid_params['I'],
      self.pid_params['D'],
      self.setpoint,
    )
  
  def start(self):
    self.on = True
  
  def stop(self):
    self.on = False
    