import redis
import json

import config

from instrument import Instrument
import services


# fake data
# fake_data = {
#   'status': 'on',
#   'saturator_temperature': 50,
#   'condensor_temperature': 20,  
#   'optics_temperature': 50,
#   'flow': 0.1,
#   'liquid_level': 1,
# }

r = redis.Redis(**config.get_redis_host_and_port())


def main():
  pubsub = r.pubsub(ignore_subscribe_messages=True)
  pubsub.subscribe(['counter', 'commands', 'settings'])

  instrument = Instrument()

  for m in pubsub.listen():

    if m['channel'] == b'counter':
      counts = json.loads(m['data'])['counts']
      data = instrument.update()
      # data = fake_data
      data['counts'] = counts
      data['concentration'] = int(counts / (data['flow'] * 1000 / 60)) # particles/cm3
      print(data)

      try:
        services.publish_to_websockets(data)
        # services.save_to_database(data)
        # r.publish('aws_iot', json.dumps(data))
      except:
        print('No data published or saved.')

    # elif m['channel'] == b'commands':
    #   switch = json.loads(m['data']['switch'])
    #   if switch == 'on':
    #     instrument.on()
    #   else:
    #     instrument.off()
    
    # elif m['channel'] == b'settings':
    #   if json.loads(m['data']['update']) == 'on':
    #     instrument.reload()


if __name__ == '__main__':
  main()
