import redis
import json

import config

# from instrument import Instrument
import services


r = redis.Redis(**config.get_redis_host_and_port())


def main():
  pubsub = r.pubsub(ignore_subscribe_messages=True)
  pubsub.subscribe(['counter', 'commands', 'settings'])

  # instrument = Instrument()

  for m in pubsub.listen():

    if m['channel'] == b'counter':
      counts = json.loads(m['data'])['counts']
      # data = instrument.update()
      data = {}
      data['counts'] = counts
      print(data)

      services.publish(data)
      # r.publish('local_web', json.dumps(data))
      # r.publish('local_database', json.dumps(data))
      # r.publish('aws_iot', json.dumps(data))

    # elif m['channel'] == b'commands':
    #   if json.loads(m['data'])['switch']:
    #     instrument.on()
    #   else:
    #     instrument.off()
        
    # elif m['channel'] == b'settings':
    #   instrument.reload()


if __name__ == '__main__':
  main()
