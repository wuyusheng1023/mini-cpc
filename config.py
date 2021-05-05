# Redis
def get_redis_host_and_port():
  host = 'localhost'
  port = 6379
  return dict(host=host, port=port)

# WebSockets
def get_websockets_host_and_port():
  host = 'localhost'
  port = 8765
  return dict(host=host, port=port)

# MongoDB
def get_mongodb_host_port_db_col():
  host= 'localhost'
  port = 27017
  db = 'minicpc'
  col = 'data'
  return dict(host=host, port=port, db=db, col=col)
