
from cache.backends.redis import RedisCache

_params = dict()
_redis = RedisCache(_params)

def cache_get(key, default=None):
    return _redis.get(key, default)

def cache_add(key,value):
    _redis.add(key,value)

def cache_del(key):
    _redis.delete(key)