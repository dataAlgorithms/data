#!/usr/bin/env python3
#!coding=utf-8

def recv(maxsize, *, block):
    'Receive a message'
    pass

#recv(1024, True)   # Type Error
recv(1024, block=True)
