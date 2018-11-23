#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json

class Proxy:
    proxy = []
    def get_proxy(self):
        if len(self.proxy) <= 0:
            self.proxy = json.loads(requests.get("http://127.0.0.1:5010/get_all").text)
        return self.proxy.pop()
    
    def delete_proxy(self, proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    