[root@RND-SM-1-59Q pytmp]# zcat 06015733WS_FVSS_STREAM_20171009172000.log.gz 
1507540791      300     rtmp://lxlive1.mengliaoba.cn    0       0       0       0       361397333       5       66
1507540796      300     rtmp://edum.jcx999.com  0       0       0       0       23179240        1       2
1507540791      300     rtmp://zb.kangfuxigu.com        0       0       0       0       23762865        1       0
1507540791      300     rtmp://v.hhkcdn.com     0       0       0       0       235371885       2       30
1507540791      300     rtmp://agqj.yzbabyu.com 0       0       0       0       30560678        1       11
1507540796      300     rtmp://ucc.live.duobeiyun.com   0       0       5511760 3839115 0       0       0
1507540791      300     rtmp://ftv.sun0769.com  0       0       0       0       31881661        1       0
1507540796      300     rtmp://ptvlivef.people.com.cn   0       0       0       0       1101848124      1       0
1507540791      300     rtmp://flv.china.com.cn 0       0       0       0       241394292       2       0
1507540796      300     rtmp://vlive.people.com.cn      0       0       0       0       3175255 1       17
1507540791      300     rtmp://fms.lucky188.cn  0       0       0       0       13900251        1       2
1507540791      300     rtmp://play2.fqcj.tv    0       0       0       0       8957192 1       4
[root@RND-SM-1-59Q pytmp]# zcat 06015733WS_FVSS_STREAM_20171009172500.log.gz 
1507541091      300     rtmp://lxlive1.mengliaoba.cn    0       0       0       0       296100670       9       95
1507541096      300     rtmp://edum.jcx999.com  0       0       0       0       48860249        1       12
1507541091      300     rtmp://zb.kangfuxigu.com        0       0       0       0       23739792        1       0
1507541091      300     rtmp://v.hhkcdn.com     0       0       0       0       227142925       3       35
1507541091      300     rtmp://agqj.yzbabyu.com 0       0       0       0       17583488        1       5
1507541096      300     rtmp://ucc.live.duobeiyun.com   0       0       5085974 1291330 0       0       0
1507541091      300     rtmp://ftv.sun0769.com  0       0       0       0       32318601        1       0
1507541096      300     rtmp://ptvlivef.people.com.cn   0       0       0       0       1172412634      1       8
1507541091      300     rtmp://flv.china.com.cn 0       0       0       0       241670497       2       0
1507541091      300     rtmp://vlive.people.com.cn      0       0       0       0       3535008 3       22
1507541041      300     rtmp://fms.lucky188.cn  0       0       0       0       39153040        0       1
1507541091      300     rtmp://play2.fqcj.tv    0       0       0       0       9360136 1       1
[root@RND-SM-1-59Q pytmp]# python dataprocess.py 
1507540791      300     rtmp://lxlive1.mengliaoba.cn    0       0       0       0       361397333       5       66
1507540796      300     rtmp://edum.jcx999.com  0       0       0       0       23179240        1       2
1507540791      300     rtmp://zb.kangfuxigu.com        0       0       0       0       23762865        1       0
1507540791      300     rtmp://v.hhkcdn.com     0       0       0       0       235371885       2       30
1507540791      300     rtmp://agqj.yzbabyu.com 0       0       0       0       30560678        1       11
1507540796      300     rtmp://ucc.live.duobeiyun.com   0       0       5511760 3839115 0       0       0
1507540791      300     rtmp://ftv.sun0769.com  0       0       0       0       31881661        1       0
1507540796      300     rtmp://ptvlivef.people.com.cn   0       0       0       0       1101848124      1       0
1507540791      300     rtmp://flv.china.com.cn 0       0       0       0       241394292       2       0
1507540796      300     rtmp://vlive.people.com.cn      0       0       0       0       3175255 1       17
1507540791      300     rtmp://fms.lucky188.cn  0       0       0       0       13900251        1       2
1507540791      300     rtmp://play2.fqcj.tv    0       0       0       0       8957192 1       4
1507541091      300     rtmp://lxlive1.mengliaoba.cn    0       0       0       0       296100670       9       95
1507541096      300     rtmp://edum.jcx999.com  0       0       0       0       48860249        1       12
1507541091      300     rtmp://zb.kangfuxigu.com        0       0       0       0       23739792        1       0
1507541091      300     rtmp://v.hhkcdn.com     0       0       0       0       227142925       3       35
1507541091      300     rtmp://agqj.yzbabyu.com 0       0       0       0       17583488        1       5
1507541096      300     rtmp://ucc.live.duobeiyun.com   0       0       5085974 1291330 0       0       0
1507541091      300     rtmp://ftv.sun0769.com  0       0       0       0       32318601        1       0
1507541096      300     rtmp://ptvlivef.people.com.cn   0       0       0       0       1172412634      1       8
1507541091      300     rtmp://flv.china.com.cn 0       0       0       0       241670497       2       0
1507541091      300     rtmp://vlive.people.com.cn      0       0       0       0       3535008 3       22
1507541041      300     rtmp://fms.lucky188.cn  0       0       0       0       39153040        0       1
1507541091      300     rtmp://play2.fqcj.tv    0       0       0       0       9360136 1       1
[root@RND-SM-1-59Q pytmp]# cat dataprocess.py 
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

lognames = gen_find('06015733WS*', './')
files = gen_opener(lognames)
lines = gen_concatenate(files)
rtmplines = gen_grep('(?i)rtmp', lines)
for line in rtmplines:
    print(line, end='')
[root@RND-SM-1-59Q pytmp]# 
