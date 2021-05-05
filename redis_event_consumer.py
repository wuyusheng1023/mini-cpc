import redis
import json

import config

from instrument import Instrument


r = redis.Redis(**config.get_redis_host_and_port())


def main():
  pubsub = r.pubsub(ignore_subscribe_messages=True)
  pubsub.subscribe(['counter', 'settings'])

  instrument = Instrument()

  for m in pubsub.listen():
    if m['channel'] == b'counter':
      counts = json.loads(m['data'])['counts']
      data = instrument.update()
      data['counts'] = counts
    elif m['channel'] == b'settings':
      instrument.reload()


if __name__ == '__main__':
  main()
