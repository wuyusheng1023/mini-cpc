import json
import asyncio
import websockets

import config


host = config.get_websockets_host_and_port()['host']
port = config.get_websockets_host_and_port()['port']
uri = f'ws://{host}:{port}'

async def _publish(data):
  async with websockets.connect(uri) as websocket:
    data = json.dumps(data)
    await websocket.send(data)
    await websocket.recv()

def publish(data):
  asyncio.get_event_loop().run_until_complete(_publish(data))
