#! coding=utf-8 

import json
import urllib2 
import random
import time 

# Read and write at Redis server
def readWriteRedis(queryUrl='http://192.168.32.223:8081/core?cchost_tag=issCluster'):
    
    isType = random.randint(0, 7)
    
    # set string
    if isType == 0:
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myStr","set","myStr","123"]}}]

    # get string
    elif isType == 1:        
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myStr","get","myStr"]}}]
        
    # set single hash
    elif isType == 2:
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myHash","hset","myHash","field","456"]}}]
    
    # get single hash
    elif isType == 3:
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myHash","hgetall","myHash"]}}]
        
    # set multi hash
    elif isType == 4:
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myMhash","hmset","myMhash","username","runoob", "password","runoob", "points","200"]}}]
        
    # get multi hash
    elif isType == 5:
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myMhash","hgetall","myMhash"]}}]
    
    # set list
    elif isType == 6:
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myList","lpush","myList","redis"]}}]

    # get list
    else:
        data = [{"method":"TestRedisCluster","args":{"mode":"exec","set":["myList","lrange","myList","0", "-1"]}}]
        
    req = urllib2.Request(queryUrl)
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps(data))
    allResults = response.readlines()
    print 'allResults:', allResults
     
def redisAync(num=None):
    
    from multiprocessing.dummy import Pool as ThreadPool 

    queryUrls = ['http://192.168.32.223:8081/core?cchost_tag=issCluster'] * num 
    pool = ThreadPool() 
    _results = pool.map(readWriteRedis, queryUrls)
    #print results
    
def redis(num=None):
    
    for _ in range(num):
        readWriteRedis()
        
if __name__ == "__main__":
    start = time.clock()
    redisAync(num=100)
    end = time.clock()
    
    print 'Time needed: ', end-start
