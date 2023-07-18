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
        ssl=True)
    r.set('foo', 'bar')
    v = r.get('foo')
    print (v)