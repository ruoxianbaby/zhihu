#!/usr/bin/python
# -*- coding: UTF-8 -*-

import redis
from common import config

class Redis:
    redis = ""
    config = {}
    def __init__(self):
        if not self.redis:
            self.config = config.config['redis']
            self.connect_redis()
    
    def connect_redis(self):
        config = self.config
        pool = redis.ConnectionPool(host = config['host'], port = config['port'], password = config['passwd'], db = config['dbname'])
        self.redis = redis.Redis(connection_pool = pool)
        return self.redis

    # def __del__(self):
        