#! coding=utf-8

'''
Stdin and stdout

Usage:
Windows:
type SomeFile.txt|python egrep.py "[0-9]" | python line_count.py

Linux:
cat SomeFile.txt|python egrep.py "[0-9]" | python line_count.py
'''
# egrep.py
import sys, re

# sys.argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
        
# line_count.py
count = 0
for line in sys.stdin:
    count += 1

print count

# most_common_words.py
# usage: type the_bible.txt | python most_common_words.py 10
from collections import Counter

# pass in number of words as first argument
try:
    num_words = int(sys.argv[1])
except:
    print "usage: most_common_words.py num_words"
    sys.exit(1)

counter = Counter(word.lower()
                  for line in sys.stdin
                   for word in line.strip().split()
                   if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")

    sys.stdout.write(word)
    sys.stdout.write("\n")

'''
reading and writing file
'''
file_for_reading = open('reading_file.txt', 'r')
file_for_reading.close()

file_for_writing = open('writing_file.txt', 'w')
file_for_writing.close()

file_for_appending = open('appending_file.txt', 'a')
file_for_appending.close()

with open('filename', 'r') as f:
    data = f
    print data

starts_with_hash = 0
with open('input.txt', 'r') as f:
    for line in f:
        if re.match("^#", line):
            starts_with_hash += 1
            
def get_domain(email_address):
    """split on @ and return the last piece"""
    return email_address.lower().split("@")[-1]

with open('email_addresses.txt', 'r') as f:
    domains_counts = Counter(get_domain(line.strip())
              for line in f
                if "@" in line)

import csv

'''
6/20/2014    AAPL    90.91
6/20/2014    MSFT    41.68
6/20/2014    FB    64.5
6/19/2014    AAPL    91.86
6/19/2014    MSFT    41.51
6/19/2014    FB    64.34
'''
with open('tab_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date_ = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        print date_, symbol, closing_price

'''
date:symbol:closing_price
6/20/2014:AAPL:90.91
6/20/2014:MSFT:41.68
6/20/2014:FB:64.5
'''
with open('colon_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date_ = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        print date_,symbol,closing_price

today_prices = { 'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }
with open('comma_delimited_stock_prices.txt','wb') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])

results = [["test1", "success", "Monday"],
           ["test2", "success, kind of", "Tuesday"],
           ["test3", "failure, kind of", "Wednesday"],
           ["test4", "failure, utter", "Thursday"]]

with open('bad_csv.txt', 'wb') as f:
    for row in results:
        f.write(",".join(map(str, row)))
        f.write("\n")
