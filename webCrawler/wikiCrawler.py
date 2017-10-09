#!/usr/bin/env python 
# -*- coding:utf-8 -*-  

'''
downloadfile: 
https://stackoverflow.com/questions/27911395/download-file-via-hyperlink-in-phantomjs-using-selenium

python淇濆瓨缃戦〉:
https://jingyihiter.github.io/2016/07/04/python%E5%AD%A6%E4%B9%A0%E4%BF%9D%E5%AD%98%E7%BD%91%E9%A1%B5%E5%88%B0%E6%9C%AC%E5%9C%B0-html%E5%8F%8Apdf/

import urllib2
import cookielib
import pdfkit

cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
url = "https://www.taobao.com/"
req = urllib2.Request(url)

淇濆瓨html鍒版湰鍦�
operate = opener.open(req)
msg = operate.read()
document = 'D://1.html'  
file_ = open(document,'w')   
file_.write(msg)
file_.close()

path_wk = r'C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wk)

淇濆瓨pdf鍒版湰鍦�
pdfkit.from_url(url, r'D:\are you coding\pdf\taobao.pdf', configuration=config)
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
import urllib2
import cookielib
import pdfkit
import time
import re 

import sys   
reload(sys) 
sys.setdefaultencoding('utf-8')   

from selenium import webdriver

'''
download attachment
https://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python

http://wiki.dev.chinacache.com//download/attachments/18403560/%5B6X1G227%5B1_21J_%29%5BBH05FD.jpg?version=1&modificationDate=1442469617000&api=v2
http://wiki.dev.chinacache.com//download/attachments/17673050/worddav8fe2ef79af8b34458a553e904b334ed0.png?version=1&modificationDate=1437968159000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28616296/image2016-2-25%2021%3A4%3A23.png?version=1&modificationDate=1456405016000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28616296/image2016-2-25%2021%3A11%3A42.png?version=1&modificationDate=1456405455000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28616296/image2016-2-25%2021%3A16%3A5.png?version=1&modificationDate=1456405718000&api=v2
http://wiki.dev.chinacache.com//download/attachments/13043647/SMS.png?version=1&modificationDate=1430735131000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28616296/image2016-2-25%2021%3A7%3A30.png?version=1&modificationDate=1456405204000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28616296/image2016-2-25%2021%3A0%3A50.png?version=1&modificationDate=1456404804000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28616296/image2016-2-25%2021%3A12%3A14.png?version=1&modificationDate=1456405488000&api=v2
http://wiki.dev.chinacache.com//download/attachments/31632386/image2016-9-14%2014%3A49%3A9.png?version=1&modificationDate=1473835190000&api=v2
http://wiki.dev.chinacache.com//download/attachments/31632386/image2016-9-14%2014%3A56%3A51.png?version=1&modificationDate=1473835652000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A17%3A40.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A19%3A7.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A21%3A46.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A16%3A29.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A19%3A48.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43926241/image2017-9-4%2011%3A54%3A17.png?version=1&modificationDate=1504496952000&api=v2
http://wiki.dev.chinacache.com//download/attachments/44859887/image2017-9-8%2017%3A30%3A56.png?version=1&modificationDate=1504863185000&api=v2
http://wiki.dev.chinacache.com//download/attachments/44859887/image2017-9-11%2014%3A23%3A0.png?version=1&modificationDate=1505110760000&api=v2
http://wiki.dev.chinacache.com//download/attachments/44859887/image2017-9-11%2014%3A23%3A51.png?version=1&modificationDate=1505110810000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925679/image2017-8-30%2014%3A32%3A11.png?version=1&modificationDate=1504074871000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925679/image2017-8-30%2014%3A26%3A37.png?version=1&modificationDate=1504074871000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925679/image2017-8-30%2014%3A30%3A41.png?version=1&modificationDate=1504074871000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925641/image2017-8-30%2014%3A2%3A36.png?version=1&modificationDate=1504072744000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43926170/image2017-9-1%2014%3A31%3A51.png?version=1&modificationDate=1504247474000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43926170/image2017-9-1%2014%3A33%3A19.png?version=1&modificationDate=1504247474000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43926170/image2017-9-1%2014%3A34%3A1.png?version=1&modificationDate=1504247474000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43926170/image2017-9-1%2014%3A34%3A41.png?version=1&modificationDate=1504247474000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A13%3A43.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A13%3A6.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A15%3A34.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A18%3A12.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A20%3A31.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43926241/image2017-9-4%2011%3A44%3A58.png?version=1&modificationDate=1504496393000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925641/image2017-8-30%2014%3A4%3A51.png?version=1&modificationDate=1504072880000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A16%3A45.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925667/image2017-8-30%2014%3A18%3A32.png?version=1&modificationDate=1504073925000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925650/image2017-8-30%2013%3A44%3A11.png?version=1&modificationDate=1504072094000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925679/image2017-8-30%2014%3A28%3A56.png?version=1&modificationDate=1504074871000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925650/image2017-8-30%2013%3A47%3A45.png?version=1&modificationDate=1504072094000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925650/image2017-8-30%2013%3A50%3A47.png?version=1&modificationDate=1504072094000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925650/image2017-8-30%2013%3A49%3A9.png?version=1&modificationDate=1504072094000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925650/image2017-8-30%2013%3A49%3A39.png?version=1&modificationDate=1504072094000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43925650/image2017-8-30%2013%3A50%3A9.png?version=1&modificationDate=1504072094000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43004271/image2017-5-8%2018%3A25%3A27.png?version=1&modificationDate=1494239408000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43911845/image2017-7-10%2019%3A59%3A12.png?version=1&modificationDate=1499687662000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43911845/image2017-7-17%2014%3A25%3A20.png?version=1&modificationDate=1500272381000&api=v2
http://wiki.dev.chinacache.com//download/attachments/13699438/FC_billing.JPG?version=1&modificationDate=1430908097000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32606225/7CC6.tmp.png?version=1&modificationDate=1480312447000&api=v2
http://wiki.dev.chinacache.com//download/attachments/35291413/image2017-1-3%2017%3A55%3A7.png?version=1&modificationDate=1483439160000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-19%2014%3A16%3A50.png?version=1&modificationDate=1482126394000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-19%2014%3A16%3A22.png?version=1&modificationDate=1482126366000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-19%2019%3A4%3A15.png?version=1&modificationDate=1482143636000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-20%2015%3A0%3A5.png?version=1&modificationDate=1482215373000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-20%2020%3A4%3A9.png?version=1&modificationDate=1482233614000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-21%2016%3A12%3A18.png?version=1&modificationDate=1482306092000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2017-1-3%2014%3A58%3A11.png?version=1&modificationDate=1483426648000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-13%2014%3A22%3A40.png?version=1&modificationDate=1481608435000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-11-16%2010%3A59%3A26.png?version=1&modificationDate=1479263658000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-11-16%2011%3A19%3A13.png?version=1&modificationDate=1479264844000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/%7B812B060E-E17E-4B41-9CAB-6BF5AE58A3AF%7D.bmp?version=1&modificationDate=1479264695000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/host.bmp?version=1&modificationDate=1479280368000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-13%2012%3A23%3A40.png?version=1&modificationDate=1481601300000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/%7B00EA2BCF-6128-4A28-81F0-45C901479BD3%7D.bmp?version=1&modificationDate=1479284818000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32606755/image2016-11-25%2010%3A0%3A16.png?version=1&modificationDate=1480037749000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28613183/%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2.jpg?version=1&modificationDate=1453365067000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-13%2013%3A54%3A4.png?version=1&modificationDate=1481606720000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-13%2013%3A59%3A4.png?version=1&modificationDate=1481607020000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2016-12-13%2014%3A1%3A57.png?version=1&modificationDate=1481607193000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/%7BCDF7B67D-FD22-4E52-B217-E630B3C7136D%7D.bmp?version=1&modificationDate=1479285566000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2017-2-16%2014%3A43%3A52.png?version=1&modificationDate=1487227359000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2017-2-20%2014%3A25%3A24.png?version=1&modificationDate=1487571476000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/%7BBA386DF2-879D-4CBB-B78E-9CD5D3AD78F9%7D.png?version=1&modificationDate=1487842701000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/%7BAEE0C793-7C43-4D33-BD56-0ECE4FB8B185%7D.png?version=1&modificationDate=1489644211000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2017-4-18%2010%3A46%3A6.png?version=1&modificationDate=1492483427000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32604838/image2017-7-11%2014%3A26%3A56.png?version=1&modificationDate=1499754222000&api=v2
http://wiki.dev.chinacache.com//download/attachments/32606755/image2016-11-25%2015%3A19%3A53.png?version=1&modificationDate=1480056709000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43007735/12.png?version=1&modificationDate=1495855934000&api=v2
http://wiki.dev.chinacache.com//download/attachments/43001864/%E6%8D%95%E8%8E%B7.JPG?version=2&modificationDate=1495878036000&api=v2
http://wiki.dev.chinacache.com//download/attachments/28631572/image2016-3-1%2013%3A56%3A30.png?version=1&modificationDate=1456811682000&api=v2
'''

def download(driver, target_path):
    """Download the currently displayed page to target_path."""
    def execute(script, args):
        driver.execute('executePhantomScript',
                       {'script': script, 'args': args})

    # hack while the python interface lags
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
    # set page format
    # inside the execution script, webpage is "this"
    page_format = 'this.paperSize = {format: "A4", orientation: "portrait" };'
    execute(page_format, [])

    # render current page
    render = '''this.render("{}")'''.format(target_path)
    execute(render, [])


cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

usr = "ping.zhou"
pwd = "qazQAZ123!!!"

#chromedriver = 'D:\eclipse\eclipse\workspace\Cs\chromedriver.exe'
#os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.Chrome(chromedriver)

driver = webdriver.PhantomJS(executable_path=r'D:\eclipse\eclipse\workspace\Cs\phantomjs')

    
#driver = webdriver.Firefox()
# or you can use Chrome(executable_path="/usr/bin/chromedriver")

driver.get("http://wiki.dev.chinacache.com/pages/viewpage.action?pageId=%s" % 360453)

elem = driver.find_element_by_id("os_username")
elem.send_keys(usr)
elem = driver.find_element_by_id("os_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)


for i in ['9846054', '9840593', '9838285', '9838283', '9838281', '9838276', '9838274', '9838272', '9837024', '9837018', '9836963', '44859887', '44859596', '43926675', '43926671', '43926241', '43926170', '43925708', '43925706', '43925679', '43925667', '43925665', '43925650', '43925641', '43925468', '43918023', '43917129', '43916557', '43915425', '43915417', '43912008', '43912003', '43911936', '43911845', '43911504', '43911502', '43911385', '43910946', '43015899', '43015861', '43015859', '43015789', '43015513', '43015143', '43015067', '43015066', '43011959', '43011846', '43011844', '43011838', '43011804', '43011800', '43011791', '43011789', '43011787', '43009310', '43008645', '43007735', '43004497', '43004271', '43001864', '43000787', '42999285', '42999165', '42998362', '42997993', '42996463', '42995824', '42995800', '42995798', '42995570', '42995560', '42993473', '42993468', '42993265', '42993145', '42993116', '42993114', '42993110', '42993108', '42993106', '42993104', '42993102', '42993100', '42993097', '42993000', '42992773', '42992695', '42992686', '42992683', '42992678', '42992676', '42992674', '42992632', '42992624', '41747001', '39029089', '39028239', '37093477', '360453', '3604', '35292759', '35292303', '35291413', '33357852', '32611407', '32609896', '32609679', '32609371', '32608564', '32608205', '32607528', '32607054', '32606755', '32606225', '32606102', '32605654', '32605053', '32604838', '32604512', '31645090', '31644762', '31642817', '31641798', '31641700', '31638563', '31638468', '31637896', '31636725', '31633952', '31633926', '31633922', '31633352', '31632948', '31632827', '31632676', '31632027', '31630667', '31630396', '31630202', '31630028', '31629', '31626417', '31625810', '31625071', '31624308', '31624009', '31623917', '31623872', '31623869', '31622786', '31622448', '31622149', '31621643', '31621196', '30968603', '30968513', '30968351', '30967857', '30967114', '30966933', '30966876', '30966556', '30966354', '30966088', '30179542', '29898346', '29896854', '29896454', '29896424', '29894119', '29894106', '29893343', '29893283', '29892404', '29891839', '29890336', '29888564', '29888466', '29888417', '29888231', '29886014', '29885321', '29884900', '29556186', '29555218', '29555216', '29554437', '29553658', '29553272', '29550000', '29549334', '29548179', '29547113', '29546619', '29546245', '29544904', '29544029', '29544025', '29542214', '29541493', '29540047', '29540006', '29538708', '29538432', '29537940', '29537935', '29537219', '29536039', '29536036', '29535972', '29535833', '29535739', '29535404', '29535266', '29534001', '29532386', '29531681', '29531371', '29531366', '29530416', '29530083', '28638909', '28635839', '28634625', '28634620', '28634596', '28632181', '28632127', '28631572', '28631360', '28627813', '28625251', '28623673', '28617763', '28617489', '28617096', '28616296', '28615426', '28615013', '28613729', '28610347', '28608851', '28608836', '28608033', '28607784', '28607714', '28607225', '28606961', '27954960', '27954889', '27954801', '27954747', '27361708', '24903821', '24903812', '24903804', '24347067', '23728959', '23727532', '23727522', '23727499', '23727137', '23726469', '23726357', '23726341', '23726140', '23725969', '23725367', '23725331', '23725008', '23724409', '23724358', '22479679', '22479589', '21860469', '21860436', '21860257', '21859240', '21857494', '21857311', '21857215', '21857209', '21856711', '21856427', '21856410', '21856374', '20460167', '20458122', '20457828', '20457826', '20457515', '20457508', '20457478', '20455568', '20454786', '20453931', '20453484', '20453478', '20453252', '20452871', '20450609', '20450093', '20449748', '20449527', '20449525', '20448906', '20448779', '20448689', '20448672', '20448646', '20448165', '20448163', '20447903', '19825307', '19268970', '19268919', '19268900', '19268599', '19267704', '18406939', '18404948', '18404306', '18404271', '18403560', '18403047', '18402999', '18402366', '18401335', '18401331', '18400598', '18400445', '18397176', '18396475', '18395613', '18393395', '18392671', '18392666', '18391830', '18390566', '17674609', '17673050', '17671478', '17670314', '17670098', '17668800', '17668696', '17668448', '17666067', '17664718', '17664546', '17664061', '17662870', '15796709', '15796494', '15796442', '15796377', '15796367', '15796346', '15080931', '15080611', '15077378', '15076289', '15076281', '15073852', '14452044', '14450789', '13711229', '13710932', '13709851', '13708193', '13708189', '13708166', '13707984', '13703754', '13703153', '13700130', '13699691', '13699438', '13697501', '13697058', '13045608', '13045553', '13045463', '13044076', '13044047', '13043896', '13043842', '13043810', '13043756', '13043752', '13043717', '13043647', '13043643', '13043141', '13043120', '13043115', '13042078', '13042045', '13041680', '13041677', '13041675', '12454786', '12454555', '12453003', '11799846', '11578171', '11578153', '11578149', '11570284', '11567778', '11567776', '11567767', '10774579', '10771564', '10771562', '10771558', '10769216', '10766960', '10766955', '10766952', '10766620', '10766296', '10765963', '10764844', '10764841', '10764830', '10764358', '10764307', '10764265', '10761587', '10761583', '10761581', '10761578', '10761569', '10761567', '10760763', '10760761', '10760758', '10760756', '10758535', '10755950', '10755375', '10755212', '10754377', '10754276', '10754265', '10752093', '10748827']:    

    time.sleep(0.001)
    print 'i=:', i
    driver.get("http://wiki.dev.chinacache.com/pages/viewpage.action?pageId=%s" % i)

    if u"页面未找到" in driver.title:
        print "11111111111111111"
        continue
    
    pageSource =  driver.page_source
    
    driver_title = driver.title 
    driver_title = re.sub('/', '_', driver_title)
    driver_title = re.sub('\*', '', driver_title)
    driver_title = re.sub('\|', '', driver_title)
    driver_title = re.sub("( .*)", "", driver_title)
    
    fobj = open('%s_%s.html' % (driver_title, i), 'w')
    fobj.write(pageSource)
    fobj.close()
    
    driver.get_screenshot_as_file('%s_%s.png' % (driver_title, i))
    
    download(driver, '%s_%s.pdf' % (driver_title, i))
    
driver.close()
