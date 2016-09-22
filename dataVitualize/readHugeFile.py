#! coding=utf-8

def readHugeFile(filename='veryHugeFile'):

    validFileName = filename
    
    flag = 0
    with open(validFileName , 'rb') as hugefile:
        chunksize = 20
        readable = ''
        # if you want to stop after certain number of blocks
        # put condition in the while
        while hugefile:
            # if you want to start not from lst byte
            # do a hugefile.seek(skipbytes) to skip
            # skipbytes of bytes from the file start
            start = hugefile.tell()
            print "starting at:", start
            file_block = ''
            for _ in xrange(start, start+chunksize):
                try:
                    line = hugefile.next()
                    file_block = file_block + line
                    print "file_block", type(file_block), file_block
                except:
                    flag = 1
                    break
                
            readable = readable + file_block
            # tell where are we in file
            # file IP is usually buffered so tell()
            # will not be precise for every read
            stop = hugefile.tell()
            print 'readable', type(readable), readable
            print 'reading bytes from %s to %s' % (start, stop)
            print 'read bytes total:', len(readable)
    
            # if you want to pause read between chucks
            # uncomment following line
            # raw_input()
            
            if flag == 1:
                break
            
if __name__ == "__main__":
    readHugeFile('ch02-fixed-width-1M.data')
