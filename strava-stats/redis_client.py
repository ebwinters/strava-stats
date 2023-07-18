import redis
import os

def get_redis():
    r = None
    e = os.environ["environment"]
    if (e == "test"):
        r = redis.Redis(host=os.environ["redisHost"], port=os.environ["redisPort"], decode_responses=True)
    else:
        r = redis.StrictRedis(
        host=os.environ["redisHost"],
        port=os.environ["redisPort"],
        db=0,
        password=os.environ["redisPassword"],
        ssl=True,
        decode_responses=True)
    return r

def set_hash(r, key, val):
    r.hmset(key, val)
    r.expire(key, 60)

def get_hash(r, key):
    val = r.hgetall(key)
    if (val == {}):
        return None
    return val