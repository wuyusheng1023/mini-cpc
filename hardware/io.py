from RPi import GPIO


class DigitalInput:

  def __init__(self, gpio):
    self.gpio = gpio
  
  @property
  def data(self):
    GPIO.input(self.gpio)


class DigitalOutput:
  def __init__(self, gpio):
    self.gpio = gpio

  def start(self):
    GPIO.output(self.gpio, GPIO.HIGH)
  
  def stop(self):
    GPIO.output(self.gpio, GPIO.LOW)
