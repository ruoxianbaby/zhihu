#!/usr/bin/python
# -*- coding: UTF-8 -*-

from common import Base
import re
import sys
import urllib.request
import requests
import json
from bs4 import BeautifulSoup
import Proxy
import RedisManagerPeople

class main(Base.Base, Proxy.Proxy, RedisManagerPeople.RedisManagerPeople):
    people_profile = "https://www.zhihu.com/people/"
    
    def __init__(self):
        Base.Base.__init__(self)
        RedisManagerPeople.RedisManagerPeople.__init__(self)


    def run(self):
        self.get_zhihu_user_info()
    
    def get_zhihu_user_info(self):
        self.people = self.get_people()
        url = self.people_profile + self.people
        context = None
        while not context:
            context = self._request(url)
        result = self.analysis(context)
        print(result)

    def _request(self, url):
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Connection': 'keep-alive'}
        proxy = self.get_proxy() 
        try:
            result = requests.get(url, headers = head, proxies={"http": "http://{}".format(proxy)}, timeout = 8).text
            return result
        except:
            self.delete_proxy(proxy)
            return None
        
    
    # 分析格式化得到的html
    def analysis(self, context):
        soup = BeautifulSoup(context, "html.parser")
        self.soup = soup
        self.base_info = json.loads(soup.find(id = "js-initialData").get_text())
        self.get_followers(soup)
        info = self.format_info()
        return info
    
    def format_info(self):
        info = {}
        user_info = self.base_info['initialState']['entities']['users'][self.people]
        info = {
            "name": user_info['name'],
            "following_num": user_info['followingCount'],
            "follows_num": user_info['followerCount'],
            "url_token": self.people,
            "gender": user_info['gender'],
            "header_img": user_info['avatarUrl'],
            "create_time": self.datetime(),
            "industry": user_info['business']['name'],
            "headline": user_info['headline'],
            "Intro": user_info['description'],
            "bg_img": user_info['avatarUrlTemplate'],
            "answer_num": user_info['answerCount'],
            "question_num": user_info['questionCount'],
            "be_star": user_info['voteupCount'],
            "education": user_info['educations'][0]['school']['name'],
            "company": user_info["employments"][0]['company']['name'],
            "job": user_info["employments"][0]['job']['name'],
            "location": user_info['locations'][0]['name']
        }
        return info
    
    def get_followers(self, soup):
        pass
        # print(json.loads(data))
    
    def __del__(self):
        print("programe exit")

main = main()
main.run()
