#!/usr/bin/python
# -*- coding: UTF-8 -*-

from common import Mysql
from common import Redis

class Base:
    def __init__(self):
        self.db = Mysql.Mysql()
        redis = Redis.Redis()
        self.redis = redis.connect_redis()

