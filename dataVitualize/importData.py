#! coding=utf-8

import xml.etree.ElementTree as etree
import json
import numpy 
import struct 

class FIXEDWIDTHConnector:
    def __init__(self, filepath, mask='9s14s5s'):
        self.data = []

        with open(filepath, 'r') as f:
            for line in f:
                self.data.append(struct.Struct(mask).unpack_from(line))
  
    @property
    def parsed_data(self):
        return self.data
    
class XLSXConnector:
    def __init__(self, filepath):
        self.data = []

        import xlrd
        wb = xlrd.open_workbook(filename=filepath)
        ws = wb.sheet_by_name('Sheet1')

        for r in xrange(ws.nrows):
            col = []
            for c in range(ws.ncols):
                col.append(ws.cell(r, c).value)

            self.data.append(col)
  
    @property
    def parsed_data(self):
        return self.data
    
class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

class CSVConnector:
    def __init__(self, filepath):
        self.data = numpy.loadtxt(filepath, dtype='string', delimiter=',')
        
        '''
        or 
        
        import csv
        with open(filename) as f:
            reader = csv.reader(f)
            self.data = [row for row in reader]
        '''
            
    @property
    def parsed_data(self):
        return self.data
    
def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    elif filepath.endswith('csv'):
        connector = CSVConnector
    elif filepath.endswith('xlsx'):
        connector = XLSXConnector
    elif filepath.endswith('data'):
        connector = FIXEDWIDTHConnector
    else:
        raise ValueError('Cannot connect to %' % filepath)

    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print ve

    return factory

def inputDataMain(filepath):

    factory = connect_to(filepath)
    data = factory.parsed_data

    return data
      
if __name__ == "__main__":
    
    print '::Input csv data'
    filename = 'ch02-data.csv'
    data = inputDataMain(filename)
    for datarow in data:
        print datarow

    print '\r::Input xlsx data'
    filename = 'ch02-xlsxdata.xlsx'     
    data = inputDataMain(filename)
    for datarow in data:
        print datarow   
        
    print '\r::Input fixed width data'
    filename = 'ch02-fixed-width-1M.data'     
    data = inputDataMain(filename)
    for datarow in data:
        print datarow   
