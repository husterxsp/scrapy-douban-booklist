# -*-coding:utf-8-*-

import requests
import telnetlib

# 测试代理IP是否可用
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
    'http://119.28.50.37:82',
    'http://221.130.253.135:8090',
    'http://219.135.99.185:8088',
    'http://120.92.119.120:10000',
    'http://58.240.53.196:8080',
    'http://58.240.53.194:8080',
    'http://139.196.144.222:9999'
]

for ip in proxy_list:   
    try:
        requests.get('http://www.baidu.com/', proxies={"http": ip})
    except:
        print 'connect failed ' + ip
    else:
        print 'success ' + ip


# for ip in proxy_list:  
#     try:
#         telnetlib.Telnet('127.0.0.1', port='80', timeout=20)
#     except:
#         print 'connect failed'
#     else:
#         print 'success'