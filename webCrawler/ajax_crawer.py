#coding=utf-8

'''
页面特点:
  通过ajax技术加载, 才能看到更多内容
  
直观:
  点击加载更多
'''

#!coding=utf-8

import requests
import demjson
import json
from pprint import pprint
from urllib import request
import re
from bs4 import BeautifulSoup

url='http://www.228.com.cn/category/yanchanghui/'
rep=request.Request(url)
rep.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
resp=request.urlopen(rep)
buf=resp.read().decode('utf-8')
soup=BeautifulSoup(buf,'html.parser')
data=soup.find_all('span',class_=re.compile(r'category-boxb-ul-ft2'))
pages=int(data[0].get_text())

if pages /20!=0:
    pages=(pages/20)+1
else:
    pages=pages/20

s=requests.session()
i=1
while i<=pages:
    params = {'j': '1', 'p': i}
    haders = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}
    req = s.get('http://www.228.com.cn/category/yanchanghui', params=params, headers=haders)
    ss = demjson.decode(req.text)
    for information in ss['products']:
        print("演唱会名称："+information['shorta'])
        print("演唱会时间："+information['begindate']+'~'+information['enddate'])
        print("演唱会票价："+information['minprice']+'~'+information['maxprice'])
        print("演唱会地点："+information['cityname'])
        print("演唱会人员："+information['performer'])
        print('--------------------------------------------')
    i=i+1
