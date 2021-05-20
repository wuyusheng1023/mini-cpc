from RPi import GPIO

from datetime import datetime
from time import sleep
import json
import redis

import config
from hardware import hardware_config


counter = 0
r = redis.Redis(**config.get_redis_host_and_port())

def counter_plus_one(_):
  global counter
  counter += 1

GPIO.add_event_detect(
  hardware_config.GPIO_OPC, 
  GPIO.RISING, 
  callback=counter_plus_one
)


def main():

  t0 = datetime.now().timestamp()
  while True:
    global counter
    counts = counter
    t1 = datetime.now().timestamp()
    if int(t1) > int(t0):
      duration = t1 - t0
      counter = 0
      t0 = datetime.now().timestamp()
      data = {'counts': int(counts / duration)}
      r.publish('counter', json.dumps(data))
      t0 = t1
    sleep(0.01)


if __name__ == '__main__':
  main()
