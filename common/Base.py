#!/usr/bin/python
# -*- coding: UTF-8 -*-

from common import Mysql
from common import Redis
import time

class Base:
    def __init__(self):
        self.db = Mysql.Mysql()
        # redis = Redis.Redis()
        # self.redis = redis.connect_redis()

    def datetime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    def error_log(self, type, message):
        sql = """ 
            INSERT INTO error_log (error_type, error_message, create_time) VAULES ('%s', '%s', '%s')
            """ % {type, message, self.datetime()}
        self.db.query(sql)

