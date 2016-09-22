#! coding=utf-8

def readStreamFile(filename=None):

    import time
    import os
    import sys

    if not os.path.isfile(filename):
        print "Given file: %s is not a file" % filename

    with open(filename, 'r') as f:
        # Move to the end of file
        filesize = os.stat(filename)[6]
        f.seek(filesize)

        # endlessly loop
        while True:
            where = f.tell()
            # try reading a line
            line = f.readline()
            # if empty, go back
            if not line:
                time.sleep(1)
                f.seek(where)
            else:
                # at the ned prevents print to add newline 
                print line