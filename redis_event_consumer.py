import redis

import config


def get_redis_host_and_port():
  host = 'localhost'
  port = 6379
  return dict(host=host, port=port)

r = redis.Redis(**config.get_redis_host_and_port())


def main():
  pubsub = r.pubsub(ignore_subscribe_messages=True)
  pubsub.subscribe('counter')

  for m in pubsub.listen():
    print(m)


if __name__ == '__main__':
  main()
