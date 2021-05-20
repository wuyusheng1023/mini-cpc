import redis
import json
from flask import Flask, request

import config
import services


r = redis.Redis(**config.get_redis_host_and_port())

app = Flask(__name__)


@app.route('/api/settings')
def get_settings():
  try:
    settings = services.read_settings()
    return settings
  except:
    return {'message': 'get settings error'}


@app.route('/api/command', methods=['POST'])
def commmand():
  try:
    data = request.get_json()
    r.publish('commands', data)
    return {'message': f'command: {data}'}
  except:
    return {'message': 'a command error'}


@app.route('/api/set', methods=['POST'])
def update_settings():
  try:
    data = request.get_json()
    services.update_settings_file(data)
    r.publish('settings', json.dumps({'update': 'on'}))
    return {'message': f'settings: {data}'} 
  except:
    print('error')
    return {'message': 'set settings error'}
