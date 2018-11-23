#!/usr/bin/python
# -*- coding: UTF-8 -*-

from common import Base
import re
import sys
import urllib.request
import requests
import json
import time
from bs4 import BeautifulSoup
import redis

class main(Base.Base):
    people_profile = "https://www.zhihu.com/people/"
    def __init__(self):
        Base.Base.__init__(self)
        
    def run(self):
        self.get_user_info()
    
    def get_user_info(self):
        url = self.people_profile + self.get_people()
        context = self._request(url)
        self.analysis(context)

    def _request(self, url):
        result = urllib.request.urlopen(url)
        return result
    
    # 分析格式化得到的html
    def analysis(self, context):
        print(context)
        soup = BeautifulSoup(context, "html.parser", from_encoding="utf-8")
        self.get_followers(soup)
        info = self.format_info(soup)
        return info
    
    def format_info(self, soup):
        info = {}
        info['name'] = soup.find(attrs={"class": "ProfileHeader-name"}).get_text()
        return info
    
    def get_followers(self, soup):
        data = soup.find(id = "js-initialData").get_text()
        print(data)

    def add_done_people(self, people):
        return self.redis.sadd('done_people', people)
    
    # 从redis集合里随机抛出一个用户
    def get_people(self):
        people = self.redis.spop("people")
        if people:
            return str(people, encoding='utf-8')
        else:
            sys.exit()

    def add_people(self, people):
        return self.redis.sadd("people", people)
    
    def check_people_exists(self, people):
        return self.redis.sismember("done_people", people)

    def __del__(self):
        print("programe exit")

main = main()
main.run()
