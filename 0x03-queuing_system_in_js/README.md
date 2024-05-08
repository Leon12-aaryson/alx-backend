## queing system in JavaSvript

### Resources
- [Redis quick start](https://redis.io/docs/latest/integrate/)
- [Redis client interface](https://redis.io/docs/latest/develop/connect/cli/)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue](https://github.com/Automattic/kue)

#### Downloading redis
wget http://download.redis.io/releases/redis-6.0.10.tar.gz

```tar xzf redis-6.0.10.tar.gz```
```cd redis-6.0.10```
```make```



### Start Redis in the background with src/redis-server
```src/redis-server &```

Make sure that the server is working with a ping src/redis-cli ping
PONG
Using the Redis client again, set the value School for the key Holberton
```127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School" ```

Kill the server with the process id of the redis-server (hint: use ps and grep)
``` kill [PID_OF_Redis_Server]```
