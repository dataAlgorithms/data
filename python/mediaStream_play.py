'''
    Play the video
'''
from helper import login
import subprocess
import re 
import sys 
import librtmp 
import requests 
from multiprocessing.dummy import Pool as ThreadPool 
#import kombu # implement AMQP (advance message queue protocol)

class Play:
    # Init 
    def __init__(self, login_ip=None, login_username=None, login_password=None):
 
        self._login_session = login(login_ip, login_username, login_password)
        print 'session:', self._login_session

    # Play the rtmp video
    def rtmpPlay(self, ghost_ip=None, ghost_username=None, ghost_password=None, ghost_port=None, ghost_name=None, ghost_location=None, stream_name="stream", play_type=None):
        play_url = 'rtmp://%s:%s/%s?vhost=%s/%s' % (ghost_ip, ghost_port, ghost_location,  ghost_name, stream_name)

        # Create a connection
        conn = librtmp.RTMP(play_url, live=True)
        
        # Attempt to connect
        conn.connect()
        # Get a file-like object to access to the stream
        stream = conn.create_stream()
        # Read 1024 bytes of data
        data = stream.read(1024)

        if data == '':
            play_flag = 'No'
        else:
            play_flag = 'Yes'
        
        return play_flag
    
    # Play the http video
    def httpPlay(self, ghost_ip=None, ghost_username=None, ghost_password=None, ghost_port=None, ghost_name=None, ghost_location=None, stream_name="stream", play_type=None):
        play_url = 'http://%s:%s/%s/%s.flv?cchost_tag=%s' % (ghost_ip, ghost_port, ghost_location, stream_name, ghost_name)
        response = requests.head(play_url)
        if response.status_code == '200':
            play_flag = 'Yes'
        else:
            play_flag = 'No'
            
        return play_flag    
        
    # Play the video using ffplay (windows)
    def ffplayPlay(self, ghost_ip=None, ghost_username=None, ghost_password=None, ghost_port=None, ghost_name=None, ghost_location=None, stream_name="stream", play_type=None, keyString=None):
        if play_type == 'rtmp':
            print '111111111111111'
            
        if sys.platform != "win32":
            print "The function can only run at windows system."
            return 
        
        print 'It is the time to play video!'
        play_flag = 'Yes'
        if keyString is None:
            if play_type == 'rtmp':
                play_url = 'rtmp://%s:%s/%s?vhost=%s/%s' % (ghost_ip, ghost_port, ghost_location,  ghost_name, stream_name)
            else:
                play_url = 'http://%s:%s/%s/%s.flv?cchost_tag=%s' % (ghost_ip, ghost_port, ghost_location, stream_name, ghost_name)
        else:
            if play_type == 'rtmp':
                play_url = 'rtmp://%s:%s/%s?vhost=%s/%s%s' % (ghost_ip, ghost_port, ghost_location,  ghost_name, stream_name, keyString)
            else:
                play_url = 'http://%s:%s/%s/%s.flv?cchost_tag=%s%s' % (ghost_ip, ghost_port, ghost_location, stream_name, ghost_name, keyString)
                                
        print 'play_url:', play_url
        process = subprocess.Popen('cmd.exe /k ffplay -i "%s"' % play_url, shell=True, 
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
        buffers = ""
        while True:
            buff = process.stdout.readline()
            print 'buff:', buff
            buffers += '%s' % buff
        
            if re.search('Not Found|HTTP error 403 Forbidden|Internal Server Error|Unknown error occurred|failed to read RTMP packet header', buff):
                play_flag = 'No'
                break
            
            if re.search('Stream #0:0', buff):
                break
    
        return play_flag, buffers, process.pid
    
    # Play the video using rtmpdump and curl
    def linuxPlay(self, ghost_ip=None, ghost_username=None, ghost_password=None, ghost_port=None, ghost_name=None, ghost_location=None, stream_name="stream", play_type=None):
        if sys.platform == "win32":
            print "The function can only run at linux system."
            return 
        
        print 'It is the time to play video!'
        play_flag = 'Yes'
        if self._play_type == 'rtmp':
            play_url = 'rtmp://%s:%s/%s?vhost=%s/%s' % (ghost_ip, ghost_port, ghost_location,  ghost_name, stream_name)
            print 'session:', self._login_session
        
            process = subprocess.Popen('rtmpdump -o /dev/null -r  "%s"' % play_url, shell=True, 
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            
            buffers = ""
            while True:
                buff = process.stdout.readline()
                print 'buff:', buff
                buffers += '%s' % buff
        
                if re.search('failed to read RTMP packet header', buff):
                    play_flag = 'No'
                    break
            
                if re.search('INFO:   lxip', buff):
                    break
        else:
            play_url = 'http://%s:%s/%s/%s.flv?cchost_tag=%s' % (ghost_ip, ghost_port, ghost_location, stream_name, ghost_name)
            
            process = subprocess.Popen('curl -svo /dev/null "%s"' % play_url, shell=True, 
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            
            buffers = ""
            while True:
                buff = process.stdout.readline()
                print 'buff:', buff
                buffers += '%s' % buff
        
                if re.search('403|404|500', buff):
                    play_flag = 'No'
                    break
            
                if re.search('HTTP/1.1 200 OK', buff):
                    break
    
        return play_flag, buffers, process.pid
    
    # Play the video using st-load
    def stloadPlay(self, ghost_ip=None, ghost_username=None, ghost_password=None, ghost_port=None, ghost_name=None, ghost_location=None, stream_name="stream", play_type=None):
        if sys.platform == "win32":
            print "The function can only run at linux system."
            return 
        
        print 'It is the time to play video!'
        play_flag = 'Yes'
        if self._play_type == 'rtmp':
            play_url = 'rtmp://%s:%s/%s?vhost=%s/%s' % (ghost_ip, ghost_port, ghost_location,  ghost_name, stream_name)
            
            process = subprocess.Popen('/root/st-load/objs/sb_rtmp_load -c 1 -r -i "%s"' % play_url, shell=True, 
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
            buffers = ""
            while True:
                buff = process.stdout.readline()
                print 'buff:', buff
                buffers += '%s' % buff
        
                if re.search('read header from server failed', buff):
                    play_flag = 'No'
                    break
            
                if re.search('threads:1 alive:1', buff):
                    break
        else:
            play_url = 'http://%s:%s/%s/%s.flv?cchost_tag=%s' % (ghost_ip, ghost_port, ghost_location, stream_name, ghost_name)
            
            process = subprocess.Popen('/root/st-load/objs/sb_http_load -c 1 -r -i "%s"' % play_url, shell=True, 
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
            buffers = ""
            while True:
                buff = process.stdout.readline()
                print 'buff:', buff
                buffers += '%s' % buff
        
                if re.search('http client parse response failed', buff):
                    play_flag = 'No'
                    break
            
                if re.search('threads:1 alive:1', buff):
                    break

    
        return play_flag, buffers, process.pid
    
    # multi play
    def multiHttpPlay(self, ghost_ip=None, ghost_username=None, ghost_password=None, ghost_port=None, ghost_name=None, ghost_location=None, stream_name="stream", play_type=None, play_num=1):
        
        print 'It is the time to play video!'
        play_flag = 'Yes'
        play_url = 'http://%s:%s/%s/%s.flv?cchost_tag=%s' % (ghost_ip, ghost_port, ghost_location, stream_name, ghost_name)        
        print 'play_url:', play_url
        
        urls = []
        for _ in range(play_num):
            urls.append(play_url)

        # Make the Pool of workers
        pool = ThreadPool() 
        try:
            results = pool.map(requests.get, urls)
            print results
        except:
            print 'done error!'
            play_flag =  'No'
            
        return play_flag
    
if __name__ == "__main__":
    login_ip = '192.168.32.220'
    login_username = 'root'
    login_password = '123456'
    ghost_ip = '192.168.32.219'
    ghost_username = 'root'
    ghost_password = '123456'
    ghost_port = '8081'
    ghost_name = 'issedge'
    ghost_location = 'httpflv'
    stream_name = 'stream'
    play_type = 'http'
    PLAY = Play(ghost_ip=ghost_ip, ghost_username=ghost_username, ghost_password=ghost_password)
    PLAY.linuxPlay(ghost_port=ghost_port, ghost_name=ghost_name, ghost_location=ghost_location, stream_name=stream_name, play_type=play_type)
