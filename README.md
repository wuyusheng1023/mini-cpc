# mini-cpc

## Redis
- Docker start redis: `docker run --name redis -p 6379:6379 -d redis:6.2.3-alpine`
- Mac start redis: `redis-server /usr/local/etc/redis.conf`
- Test redis service: `redis-cli ping`

## MongoDB
- `sudo apt update`
- `sudo apt upgrade`
- `sudo apt install mongodb`
- `sudo systemctl enable mongodb`
- `sudo systemctl start mongodb`
- `mongod --version`
- shell `mongo`
  - `show dbs`
  - `use <db>`
  - `db.dropDatabase()`
  - `db.data.find().sort({ $natural: -1}).limit(1)`

## React
- `sudo apt-get install nodejs npm`
- `sudo npm install -g npx`
- `sudo yarn add antd --network-timeout 100000`
