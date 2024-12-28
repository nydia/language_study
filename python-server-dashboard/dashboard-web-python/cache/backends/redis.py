#-*- coding:utf-8 -*-

import pickle
import re
import random
from cache.backends.base import DEFAULT_TIMEOUT,BaseCache
from utils.functional import cached_property
from utils.module_loading import import_string
from config.config_api import DashboardConfig

# Redis序列化类
class RedisSerializer:
    def __init__(self, protocol=None):
        self.protocol = pickle.HIGHEST_PROTOCOL if protocol is None else protocol

    def dumps(self, obj):
        # Only skip pickling for integers, a int subclasses as bool should be
        # pickled.
        if type(obj) is int:
            return obj
        return pickle.dumps(obj, self.protocol)

    def loads(self, data):
        try:
            return int(data)
        except ValueError:
            return pickle.loads(data)

# 缓存客户端 - 单机版本
class RedisCacheClient:
    def __init__(
        self
    ):
        import redis

        self._lib = redis
        self._client = self._lib.Redis
        self._serializer = RedisSerializer()
        self._config = DashboardConfig().get_config()

    def _get_connection_pool(self):
        _pool = self._lib.ConnectionPool(
            host=self._config['cache']['redis']['host'],
            port=self._config['cache']['redis']['port'],
            password=self._config['cache']['redis']['password'],
            db=self._config['cache']['redis']['db'],
            max_connections=self._config['cache']['redis']['max_connections'],
            decode_responses=True  # 如果使用这个参数，那么必须在连接池中声明
        )
        return _pool

    def get_client(self):
        # key is used so that the method signature remains the same and custom
        # cache client can be implemented which might require the key to select
        # the server, e.g. sharding.
        pool = self._get_connection_pool()
        return self._client(connection_pool=pool)    

    def add(self, key, value, timeout):
        client = self.get_client()
        #value = self._serializer.dumps(value)

        if timeout == 0:
            if ret := bool(client.set(key, value, nx=True)):
                client.delete(key)
            return ret
        else:
            return bool(client.set(key, value, ex=timeout, nx=True))

    def get(self, key, default):
        client = self.get_client()
        value = client.get(key)
        #return default if value is None else self._serializer.loads(value)
        return default if value is None else value

    def delete(self, key):
        client = self.get_client()
        return bool(client.delete(key))

    def delete_many(self, keys):
        client = self.get_client()
        client.delete(*keys)

    def clear(self):
        client = self.get_client()
        return bool(client.flushdb())

# 缓存客户端 - 哨兵集群版本
class RedisCacheSentinelClusterClient:
    def __init__(
        self
    ):
        from redis.sentinel import Sentinel

        _config = DashboardConfig().get_config()
        _config_cache = _config['cache']
        _nodes = DashboardConfig().get_redis_nodes()
        self._lib = Sentinel(_nodes, socket_timeout=_config_cache['timeout'])  # 尝试连接最长时间单位毫秒, 1000毫秒为1秒
        # 通过哨兵获取主数据库连接实例      参数1: 主数据库的名字(集群部署时在配置文件里指明)
        self._lib.master = self._lib.master_for(
            _config_cache['redis']['master-node-name'], 
            socket_timeout=_config_cache['timeout'],
            password=_config_cache['redis']['password'],
            db=_config_cache['redis']['db']
        )
        # 通过哨兵获取从数据库连接实例    参数1: 从数据的名字(集群部署时在配置文件里指明)
        self._lib.slave = self._lib.slave_for(
            _config_cache['redis']['master-node-name'], 
            socket_timeout=_config_cache['timeout'],
            password=_config_cache['redis']['password'],
            db=_config_cache['redis']['db']
        )
        self._client = None
        self._serializer = RedisSerializer()
        self._config = _config

    def get_master_client(self):
        return self._lib.master

    def get_slave_client(self):
        return self._lib.slave  

    def add(self, key, value, timeout):
        client = self.get_master_client()
        #value = self._serializer.dumps(value)
        client.set(key, value)

    def get(self, key, default):
        client = self.get_slave_client()
        value = client.get(key)
        if value != None:
            # 在python3里面，从redis取出来的值前面有个b,比如：b'100',所以需要解码
            value = value.decode()
        #return default if value is None else self._serializer.loads(value)
        return default if value is None else value

    def delete(self, key):
        pass

    def delete_many(self, keys):
        pass

    def clear(self):
        pass

# 继承基础缓存类BaseCache
class RedisCache(BaseCache):
    def __init__(self,params):
         super().__init__(params)
         # Redis 单机版
         # self._class = RedisCacheClient()
         # Redis 哨兵集群
         self._class = RedisCacheSentinelClusterClient()

    def get_backend_timeout(self, timeout=DEFAULT_TIMEOUT):
        if timeout == DEFAULT_TIMEOUT:
            timeout = self.default_timeout
        # The key will be made persistent if None used as a timeout.
        # Non-positive values will cause the key to be deleted.
        return None if timeout is None else max(0, int(timeout))
        
    def get(self, key, default=None, version=None):
        return self._class.get(key,default)
        
    def add(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        return self._class.add(key, value, self.get_backend_timeout(timeout))

    def delete(self, key, version=None):
        return self._class.delete(key)

    def delete_many(self, keys, version=None):
        if not keys:
            return
        #safe_keys = [self.make_and_validate_key(key, version=version) for key in keys]
        #self._cache.delete_many(safe_keys)
        self._class.delete_many(keys)
