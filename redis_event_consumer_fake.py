import redis
import json
from datetime import datetime


def get_redis_host_and_port():
  host = 'localhost'
  port = 6379
  return dict(host=host, port=port)

r = redis.Redis(**get_redis_host_and_port())

def fake_instruemnt_data():
  return {
    'datetime_utc': datetime.utcnow(),
    'saturator_temperature': 50,
    'condensor_temperature': 20,
    'optics_temperature': 50,
    'flow': 0.1,
    'liquid_level': 1,
  }


def main():
  pubsub = r.pubsub(ignore_subscribe_messages=True)
  pubsub.subscribe(['counter', 'settings'])

  for m in pubsub.listen():
    if m['channel'] == b'counter':
      print(m)
      counts = json.loads(m['data'])['counts']
      data = fake_instruemnt_data()
      data['counts'] = counts
    elif m['channel'] == b'settings':
      print(m)


if __name__ == '__main__':
  main()
