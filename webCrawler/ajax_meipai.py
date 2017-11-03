#!coding=utf-8

'''
XHR:

http://www.meipai.com/lives/get_channels_program?page=2&count=12
'''
import requests
import demjson
import json
from pprint import pprint
from urllib import request
import re
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time

global null
null=''

global  false
false = False

global true
true = True

url='http://www.meipai.com/live/'
rep=request.Request(url)
rep.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
resp=request.urlopen(rep)
buf=resp.read().decode('utf-8')
soup=BeautifulSoup(buf,'html.parser')
#data=soup.find_all('span',class_=re.compile(r'category-boxb-ul-ft2'))
#pages=int(data[0].get_text())

ac = open('allContents.txt', 'w')
pu = open('playUrls.txt', 'w')
fu = open('flvUrls.txt', 'w')
mu = open('m3u8Urls.txt', 'w')
ru = open('rtmpUrls.txt', 'w')

playUrls = []
flvUrls = []
m3u8Urls = []
rtmpUrls = []

s=requests.session()
i=1

while True:
    params = {'page': i, 'count': 12}
    haders = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
    }

    req = s.get('http://www.meipai.com/lives/get_channels_program', params=params, headers=haders)

    content = req.content
    jsonContent = content.decode('utf-8')
    jsonContent = json.loads(jsonContent)

    jc = json.dumps(jsonContent, indent=4)

    if len(eval(jc)) == 0:
        break

    ac.write('%s%s' % (jc, os.linesep))

    for item in eval(jc):
        tempPu = item["live"]["user"]["url"]
        tempFu = item["live"]["video_stream"]["http_flv_url"]
        tempMu = item["live"]["video_stream"]["hls_url"]
        tempRu = item["live"]["video_stream"]["rtmp_live_url"]
        playUrls.append(tempPu)
        pu.write('%s%s' % (tempPu, os.linesep))
        fu.write('%s%s' % (tempFu, os.linesep))
        mu.write('%s%s' % (tempMu, os.linesep))
        ru.write('%s%s' % (tempRu, os.linesep))

    print('Now it is the %s page', i)
    i += 1

ac.close()
pu.close()
fu.close()
mu.close()
ru.close()

'''
# capture the primary video source
#driver = webdriver.PhantomJS(executable_path=r'D:\eclipse\eclipse\workspace\Cs\phantomjs')
driver = webdriver.Chrome(r'D:\eclipse\eclipse\workspace\Cs\chromedriver.exe')
for url in playUrls:
    driver.get(url)
    time.sleep(2)

driver.close()
driver.quit()
'''

# get all flv url
fu = open("flvUrls.txt")
allContents = fu.readlines()
fu.close()
flvLists = []
for content in allContents:
    content = content.strip()
    content = re.sub("(?m)http://(.*?)/.*", r"\1", content)
    flvLists.append(content)

dFlvLists = [item for item in set(flvLists) if item]
print('all different flv url', dFlvLists)
print()

# get all m3u8 url
mu = open("m3u8Urls.txt")
allContents = mu.readlines()
mu.close()
m3u8Lists = []
for content in allContents:
    content = content.strip()
    content = re.sub("(?m)http://(.*?)/.*", r"\1", content)
    m3u8Lists.append(content)

dM3u8Lists = [item for item in set(m3u8Lists) if item]
print('all different m3u8 url', dM3u8Lists)
print()

# get all rtmp url
ru = open("rtmpUrls.txt")
allContents = ru.readlines()
ru.close()
rtmpLists = []
for content in allContents:
    content = content.strip()
    content = re.sub("(?m)rtmp://(.*?)/.*", r"\1", content)
    rtmpLists.append(content)

dRtmpLists = [item for item in set(rtmpLists) if item]
print('all different rtmp url', dRtmpLists)
print()

'''
"D:\Program Files\Anaconda3\python.exe" D:/csTest/ajax_meipai.py
60664
Now it is the %s page 1
62406
Now it is the %s page 2
59279
Now it is the %s page 3
59389
Now it is the %s page 4
61147
Now it is the %s page 5
60377
Now it is the %s page 6
60885
Now it is the %s page 7
59938
Now it is the %s page 8
59384
Now it is the %s page 9
63107
Now it is the %s page 10
59980
Now it is the %s page 11
58572
Now it is the %s page 12
57383
Now it is the %s page 13
59764
Now it is the %s page 14
57843
Now it is the %s page 15
56407
Now it is the %s page 16
57404
Now it is the %s page 17
58338
Now it is the %s page 18
57747
Now it is the %s page 19
56637
Now it is the %s page 20
56104
Now it is the %s page 21
52175
Now it is the %s page 22
61592
Now it is the %s page 23
58415
Now it is the %s page 24
56258
Now it is the %s page 25
61084
Now it is the %s page 26
57835
Now it is the %s page 27
59336
Now it is the %s page 28
59295
Now it is the %s page 29
55442
Now it is the %s page 30
58317
Now it is the %s page 31
57191
Now it is the %s page 32
57145
Now it is the %s page 33
58854
Now it is the %s page 34
57992
Now it is the %s page 35
53253
Now it is the %s page 36
57737
Now it is the %s page 37
58932
Now it is the %s page 38
53755
Now it is the %s page 39
56452
Now it is the %s page 40
57791
Now it is the %s page 41
57977
Now it is the %s page 42
60836
Now it is the %s page 43
56508
Now it is the %s page 44
55113
Now it is the %s page 45
48244
Now it is the %s page 46
56738
Now it is the %s page 47
57461
Now it is the %s page 48
58658
Now it is the %s page 49
57497
Now it is the %s page 50
56743
Now it is the %s page 51
58042
Now it is the %s page 52
59492
Now it is the %s page 53
56401
Now it is the %s page 54
58044
Now it is the %s page 55
53526
Now it is the %s page 56
57087
Now it is the %s page 57
58249
Now it is the %s page 58
58467
Now it is the %s page 59
59895
Now it is the %s page 60
55995
Now it is the %s page 61
57437
Now it is the %s page 62
52065
Now it is the %s page 63
57979
Now it is the %s page 64
52496
Now it is the %s page 65
56993
Now it is the %s page 66
56991
Now it is the %s page 67
58667
Now it is the %s page 68
53541
Now it is the %s page 69
54793
Now it is the %s page 70
57378
Now it is the %s page 71
58142
Now it is the %s page 72
14954
Now it is the %s page 73
2
all different flv url ['live-hdl-pili.1iptv.com', 'live-hdl-ali.1iptv.com', 'live-hdl-mt.1iptv.com']

all different m3u8 url ['live-hls-mt.1iptv.com', 'live-hls-pili.1iptv.com']

all different rtmp url ['live-rtmp-mt.1iptv.com', 'live-rtmp-pili.1iptv.com', 'live-rtmp-ali.1iptv.com']


Process finished with exit code 0
'''
