#coding=utf-8

import os

nobel_winners = [
    {'category': 'Physics',
    'name': 'Albert Einstein',
    'nationality': 'Swiss',
    'sex': 'male',
    'year': 1921},
    {'category': 'Physics',
    'name': 'Paul Dirac',
    'nationality': 'British',
    'sex': 'male',
    'year': 1933},
    {'category': 'Chemistry',
    'name': 'Marie Curie',
    'nationality': 'Polish',
    'sex': 'female',
    'year': 1911}
]

# Write data into csv using common way
cols = nobel_winners[0].keys()
cols.sort()
with open('data/nobel_winners.csv', 'w')  as f:
    f.write(','.join(cols) + os.linesep)

    for o in nobel_winners:
        row = [str(o[col]) for col in cols]
        f.write(','.join(row) + os.linesep)

# Read data from csv using common way
with open('data/nobel_winners.csv') as f:
    for line in f.readlines():
        print(line),

print("\r\n")

# Read and write csv file using csv
import csv

with open('data/nobel_winners_new.csv', 'wb') as f:
    fieldnames = nobel_winners[0].keys()
    fieldnames.sort()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)

with open('data/nobel_winners_new.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("\r\n")

# Read csv data into dict
import csv

with open('data/nobel_winners.csv') as f:
    reader = csv.DictReader(f)
    nobel_winners = list(reader)

for w in nobel_winners:
    w['year'] = int(w['year'])

print(nobel_winners)

'''
C:\Python27\python.exe D:/dataviz/readWriteCsvFile.py
category,name,nationality,sex,year
Physics,Albert Einstein,Swiss,male,1921
Physics,Paul Dirac,British,male,1933
Chemistry,Marie Curie,Polish,female,1911


['category', 'name', 'nationality', 'sex', 'year']
['Physics', 'Albert Einstein', 'Swiss', 'male', '1921']
['Physics', 'Paul Dirac', 'British', 'male', '1933']
['Chemistry', 'Marie Curie', 'Polish', 'female', '1911']


[{'category': 'Physics', 'nationality': 'Swiss', 'year': 1921, 'name': 'Albert Einstein', 'sex': 'male'}, 
{'category': 'Physics', 'nationality': 'British', 'year': 1933, 'name': 'Paul Dirac', 'sex': 'male'}, 
{'category': 'Chemistry', 'nationality': 'Polish', 'year': 1911, 'name': 'Marie Curie', 'sex': 'female'}]

'''
