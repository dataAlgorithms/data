#! coding=utf-8 

import urllib2 
import json 
from random import Random
import redis 

# init
hostList = ['192.168.32.220', '192.168.32.221', '192.168.32.222', '192.168.32.223']
queryUrl='http://192.168.32.223:8081/core?cchost_tag=issCluster'

# random string
def randomStr(randomlength=4):
    str_ = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for _ in range(randomlength):
        str_+=chars[random.randint(0, length)]
    return str_

# class to access redis
class Redis:
    def __init__(self, host=None, password='root', port=6379):
        self.rds = self._connectRds(host=host, password=password, port=port)        

    def _connectRds(self,host,password,port):
        pool=redis.ConnectionPool(host=host,password=password,port=port)
        rds = redis.StrictRedis(connection_pool=pool)
        return rds
  
    def scanWithPipe(self, match):
        
        r = self.rds
        pipe = r.pipeline()
        pipe_size = 10000000
         
        l = 0
        key_list = []
        for key in r.scan_iter(match=match, count=10000000):
            key_list.append(key)
            istype = r.type(key)
            
            if istype == 'string':
                _vals = r.get(key)
                pipe.get(key)
            elif istype == 'hash':
                _vals = r.hgetall(key)
                pipe.hgetall(key)
            elif istype == 'set':
                pipe.smembers(key)
                _vals = r.zrange(key, 0, -1)
                
            if l < pipe_size:
                l += 1
            else:
                for (k, v) in zip(key_list, pipe.execute()):
                    print k, v
                l = 0
                key_list = []
         
        for (k, v) in zip(key_list, pipe.execute()):
            print k, v
                      
    def flushall(self):
        self.rds.flushall()
        
    def scan(self, match):
        r = self.rds
        for key in r.scan_iter(match=match):
            print key
        
# function to flush all redis
def flushall():
    for host in hostList:
        rds = Redis(host=host)
        print '\rhost:',host
        rds.flushall()
        
# function to view all redis
def view(key="*"):
    for host in hostList:
        rds = Redis(host=host)
        print '\rhost:',host
        rds.scanWithPipe(key)

# do domain informatin report
class domainReport:
    
    # init
    def __init__(self, devNum=1, domainNum=1, eachDataNum=1, streamNum=1, sendNum=1):
        
        devIps = [randomStr() for _ in range(devNum)]
        devNames = [randomStr() for _ in range(devNum)]
        domains = [randomStr() for _ in range(domainNum)]
            
        for dev in range(len(devIps)):
                   
            devIp = devIps[dev]
            devName = devNames[dev]
            
            for dom in range(len(domains)):
                
                domain = domains[dom]

                msgs = []
                for each in range(eachDataNum):
                        
                    msg = {"external":{"hls":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each},
                                      "hts":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each},
                                      "total":{"lossrate":each,"speed":each,"pv":each,"flux":each,"concurrence":each},
                                      "rtmp":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each},
                                      "hflv":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each}},
                          "hls":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each},
                          "abstime":each,
                          "srcInfos":[{"hls":{"speed":each,"flux":each,"concurrence":each,"lossrate":each},
                                       "devIp":devIp,"total":{"speed":each,"flux":each,"concurrence":each,"lossrate":each},
                                       "rtmp":{"speed":each,"flux":each,"concurrence":each,"lossrate":each},
                                       "hts":{"speed":each,"flux":each,"concurrence":each,"lossrate":each},
                                       "hflv":{"speed":each,"flux":each,"concurrence":each,"lossrate":each}}],
                                       "hts":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each},
                          "ip":devIp,
                          "total":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each},
                          "devName":devName,
                          "rtmp":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each},
                          "name":domain,
                          "hflv":{"flux":each,"speed":each,"pv":each,"lossrate":each,"concurrence":each}}
                        
                    msgs.append(msg)
                        
                data = [{"msgs":msgs,
                          "version":2,
                          "method":"DomainMsgReport"}]
        
        req = urllib2.Request(queryUrl)
        req.add_header('Content-Type', 'application/json')

        for _send in range(sendNum):
            response = urllib2.urlopen(req, json.dumps(data))
            allResults = response.readlines()
            print 'allResults:', allResults
    
# do stream informatin report
class streamReport:
    
    # init
    def __init__(self, devNum=1, domainNum=1, eachDataNum=1, streamNum=1, sendNum=1):
        
        devIps = [randomStr() for _ in range(devNum)]
        devNames = [randomStr() for _ in range(devNum)]
        domains = [randomStr() for _ in range(domainNum)]
        streams = [randomStr() for _ in range(streamNum)]
            
            
        for dev in range(len(devIps)):
                   
            devIp = devIps[dev]
            devName = devNames[dev]
            
            for dom in range(len(domains)):
                
                domain = domains[dom]
                
                for stre in range(len(streams)):
                    
                    name = streams[stre]

                    msgs = []
                    for each in range(eachDataNum):
                        
                        msg = {"startTime":each,
                              "devIp":devIp,
                              "resolutionV":each,
                              "videoCode":each,
                              "lossrate":each,
                              "framerate":each,
                              "pv":each,
                              "devName":devName,
                              "external":{"lossrate":each,"speed":each,"pv":each,"flux":each,"concurrence":each},
                              "srcInfos":[{"devIp":devIp,"lossrate":each,"realFramerate":each,"flux":each,"internal":1,"speed":each}],
                              "abstime":each,"protocol":1,"speed":each,"guid":each,"urlHash":each,"concurrence":each,
                          "audioCode":each,"flux":each,"domain":domain,
                          "bitrate":each,"name":name,"resolutionH":each}
                        
                        msgs.append(msg)
                        
                    data = [{"msgs":msgs,
                          "version":2,
                          "method":"StreamMsgReport"}]
        
        req = urllib2.Request(queryUrl)
        req.add_header('Content-Type', 'application/json')

        for _send in range(sendNum):

            response = urllib2.urlopen(req, json.dumps(data))
            allResults = response.readlines()
            print 'allResults:', allResults
        
# do device informatin report
class deviceReport:
    
    # init
    def __init__(self, devNum=1, domainNum=1, eachDataNum=1, streamNum=1, sendNum=1):
        
        devIps = [randomStr() for _ in range(devNum)]
        devNames = [randomStr() for _ in range(devNum)]

        for index in range(len(devIps)):
            
            devIp = devIps[index]
            devName = devNames[index]
        
            # build msgs 
            msgs = []
        
            for each in range(eachDataNum):
                msg = {"devSrc":[{"devIp":devIp,
                           "lossrate":each,
                           "pv":each,
                           "flux":each,
                           "speed":each}],
                           "devIp":devIp,
                           "flux":each,
                           "abstime":each,
                           "pv":each,
                           "speed":each,
                           "devName":devName}
            
                msgs.append(msg)
            
            # build data 
            data = [{"msgs":msgs,
                 "method":"DeviceMsgReport",
                 "version":2}]
    
        req = urllib2.Request(queryUrl)
        req.add_header('Content-Type', 'application/json')
    
        # do 
        for _send in range(sendNum):
            response = urllib2.urlopen(req, json.dumps(data))
            allResults = response.readlines()
            print 'allResults:', allResults

def showmenu():
    
    CMDs = {'v': view, 'f': flushall, 'd': deviceReport, 's': streamReport, 'o': domainReport}
    
    pr = """
    (V)iew
    (F)lushall
    (D)eviceReport
    (S)treamReport
   D(O)mainReport
    (Q)quit

    Enter choice: """

    while True:

        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'

            print '\nYou picked: [%s]' % choice
            if choice not in 'vfdsoq':
                print 'Invalid option, try again'
            else:
                break

        if choice == 'q':
            break
        elif choice in 'dso':
            CMDs[choice](devNum=10, domainNum=10, eachDataNum=100, streamNum=100, sendNum=1000)
        else:
            CMDs[choice]()
            
# prompt menu
if __name__ == "__main__":
    devNum=10
    domainNum=10
    eachDataNum=100
    streamNum=100
    sendNum=1000
    
    num = 1
    
    while True:
        domainReport(devNum, domainNum, eachDataNum, streamNum, sendNum)
        deviceReport(devNum, domainNum, eachDataNum, streamNum, sendNum)
        streamReport(devNum, domainNum, eachDataNum, streamNum, sendNum)
        
        num += 1
        if num == 1000:
            break
