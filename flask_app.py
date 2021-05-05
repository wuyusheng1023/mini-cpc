import redis
import json
from flask import Flask, request

import config
import services


r = redis.Redis(**config.get_redis_host_and_port())

app = Flask(__name__)


@app.route('/api/settings')
def get_settings():
  settings = services.read_settings()
  return settings


@app.route('/api/command', methods=['POST'])
def commmand():
  data = request.get_json()
  r.publish('commands', data)


@app.route('/api/set', methods=['POST'])
def update_settings():
  data = request.get_json()
  services.update_settings_file(data)
  r.publish('settings', json.dumps({'update': 'on'}))
