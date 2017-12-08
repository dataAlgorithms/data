#!/usr/bin/env python3
#!coding=utf-8

# Accept any number of positional arguments
def positionArguments(first, *rest):
    return (first + sum(rest)) / ( 1 + len(rest))

# Function to test positional arguments
def test_positionArguments():

    theSum = positionArguments(1, 2) 
    print('theSum:', theSum)

    theSum = positionArguments(1, 2, 3, 4)
    print('theSum:', theSum)

# Accept any number of keyword arguments 
import html

def keywordArguments(name, value, **attrs):
    keyvalues = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvalues)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                   name=name,
                   attrs=attr_str,
                   value=html.escape(value))
    return element

# Function to test keyword arguments
def test_keywordArguments():

    theEle = keywordArguments('item', 'Albaatross', size='larger', quantity=6)
    print('theEle:', theEle)

    theEle = keywordArguments('p', '<spam>')
    print('theEle:', theEle)

# Accept any number of positional and keyword arguments
def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)

# Function to test positional and keyword arguments
def test_anyargs():

    anyargs(1, 2, 3, name='zp', age='100')

'''
theSum: 1.5
theSum: 2.5
theEle: <item size="larger" quantity="6">Albaatross</item>
theEle: <p>&lt;spam&gt;</p>
(1, 2, 3)
{'age': '100', 'name': 'zp'}
'''
if __name__ == "__main__":
    test_positionArguments()
    test_keywordArguments()
    test_anyargs()
