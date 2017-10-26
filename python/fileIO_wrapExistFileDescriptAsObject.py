In [1]: # Open a low-level file descriptor

In [2]: import os

In [3]: fd = os.open('somefile.txt', os.O_WRONLY|os.O_CREAT)

In [4]: # Turn into a proper file

In [5]: f = open(fd, 'wt')

In [6]: f.write('hello world\n')
Out[6]: 12

In [7]: f.close()

In [8]: !more somefile.txt
hello world

from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                        closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                        closedfd=False)

    # Echo lines back to the client using file IO
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

