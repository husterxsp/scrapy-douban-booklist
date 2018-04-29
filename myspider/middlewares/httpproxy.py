# -*-coding:utf-8-*-
import random


class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        print(proxy)
        request.meta['proxy'] = proxy

    # http://cn-proxy.com/archives/218
    proxy_list = [
        'http://62.93.60.14:8090',
        'http://87.118.192.29:8080',
        'http://94.158.70.222:3377',
        'http://185.185.44.2:8080',
        'http://194.67.201.106:3128',
        'http://193.93.216.95:8080',
        'http://194.208.63.191:8080',
        'http://83.18.150.53:3128',
        'http://212.92.204.54:80',
        'http://87.98.174.157:3128',
    ]