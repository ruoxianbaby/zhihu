#!/usr/bin/python
# -*- coding: UTF-8 -*-

import redis
import sys
from common import Redis

class RedisManagerPeople(Redis.Redis):
    def add_done_people(self, people):
        return self.redis.sadd('done_people', people)
    
    # 从redis集合里随机抛出一个用户
    def get_people(self):
        people = self.redis.spop("people")
        if people:
            return str(people, encoding='utf-8')
        else:
            print("redis has no people")
            sys.exit()

    def add_people(self, people):
        return self.redis.sadd("people", people)
    
    def check_people_exists(self, people):
        return self.redis.sismember("done_people", people)
    