import json
import asyncio
import websockets
# from pymongo import MongoClient
from configparser import ConfigParser

import config


# publish to local websockets
host = config.get_websockets_host_and_port()['host']
port = config.get_websockets_host_and_port()['port']
uri = f'ws://{host}:{port}'


async def _publish(data):
  async with websockets.connect(uri) as websocket:
    data = json.dumps(data)
    await websocket.send(data)
    await websocket.recv()

def publish_to_websockets(data):
  asyncio.get_event_loop().run_until_complete(_publish(data))


# save to local database
# host = config.get_mongodb_host_port_db_col()['host']
# port = config.get_mongodb_host_port_db_col()['port']
# db = config.get_mongodb_host_port_db_col()['db']
# col = config.get_mongodb_host_port_db_col()['col']
# collection = MongoClient(host, port)[db][col]

# def save_to_database(data):
#   collection.insert_one(data)

# Read settings
def read_settings():
  settings = ConfigParser()
  settings.read('settings.ini')
  data = dict(settings['SETTINGS'])
  data = {k: float(v) for k, v in data.items()}
  return data

def update_settings_file(data):
  settings = ConfigParser()
  settings.read('settings.ini')
  for key, value in data.items():
    print(key, value)
    settings.set('SETTINGS', key, str(value))
  with open('settings.ini', 'w') as file:
    settings.write(file)
