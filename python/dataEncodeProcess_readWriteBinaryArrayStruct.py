from struct import Struct
from collections import namedtuple

# write data into binary array file
def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

# read binary array file
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

# unpack records
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
              for offset in range(0, len(data), record_struct.size))


def nice_read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)
    return records

def nice_unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
             for offset in range(0, len(data), record_struct.size))

'''
"D:\Program Files\Anaconda3\python.exe" D:/dataviz/readWriteBinaryArray.py
(1, 2.3, 4.5)
(6, 7.8, 9.0)
(12, 13.4, 56.7)
(1, 2.3, 4.5)
(6, 7.8, 9.0)
(12, 13.4, 56.7)
(1, 2.3, 4.5)
(6, 7.8, 9.0)
(12, 13.4, 56.7)
(1, 2.3, 4.5)
(6, 7.8, 9.0)
(12, 13.4, 56.7)
[( 1,   2.3,   4.5) ( 6,   7.8,   9. ) (12,  13.4,  56.7)]
(1,  2.3,  4.5)

Process finished with exit code 0

'''
if __name__ == "__main__":
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    # write
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)

    # pack
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)

    with open('data.b', 'rb') as f:
        data = f.read()

    # unpack
    for rec in unpack_records('<idd', data):
        print(rec)

    # nice pack
    with open('data.b', 'rb') as f:
        for rec in nice_read_records('<idd', f):
            print(rec)

    with open('data.b', 'rb') as f:
        data = f.read()

    # nice unpack
    for rec in nice_unpack_records('<idd', data):
        print(rec)

    import numpy as np

    f = open('data.b', 'rb')
    records = np.fromfile(f, dtype='<i, <d, <d')
    print(records)
    print(records[0])

    '''
    not work 
    
    # named record
    Record = namedtuple('Record', ['kind', 'x', 'y'])

    with open('data.b', 'rb') as f:
        records = (Record(*r) for r in nice_read_records('<idd', f))

    for r in records:
        print(r.kind, r.x, r.y)    
    '''

