import asyncio
import websockets

import config


USERS = set()

async def register(websocket):
  USERS.add(websocket)

async def unregister(websocket):
  USERS.remove(websocket)

async def counter(websocket, path):
  await register(websocket)
  try:
    async for message in websocket:
      await asyncio.wait([user.send(message) for user in USERS])
  finally:
    await unregister(websocket)

host = config.get_websockets_host_and_port()['host']
port = config.get_websockets_host_and_port()['port']
start_server = websockets.serve(counter, host, port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
