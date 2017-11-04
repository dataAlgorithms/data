#!/usr/bin/env python

import sys, os, re
from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import json_util
import config
import json


# Process elasticsearch hits and return flights records
def process_search(results):
  records = []
  if results['hits'] and results['hits']['hits']:
    total = results['hits']['total']
    hits = results['hits']['hits']
    for hit in hits:
      record = hit['_source']
      records.append(record)
  return records, total

# Calculate offsets for fetching lists of flights from MongoDB
def get_navigation_offsets(offset1, offset2, increment):
  offsets = {}
  offsets['Next'] = {'top_offset': offset2 + increment, 'bottom_offset': 
  offset1 + increment}
  offsets['Previous'] = {'top_offset': max(offset2 - increment, 0), 
 'bottom_offset': max(offset1 - increment, 0)} # Don't go < 0
  return offsets

# Strip the existing start and end parameters from the query string
def strip_place(url):
  try:
    p = re.match('(.+)&start=.+&end=.+', url).group(1)
  except AttributeError as e:
    return url
  return p

# Set up Flask and Mongo
app = Flask(__name__)
client = MongoClient()

# Controller: Fetch all flights between cities on a given day and display them
@app.route("/flights/<origin>/<dest>/<flight_date>")
def list_flights(origin, dest, flight_date):
  
  start = request.args.get('start') or 0
  start = int(start)
  end = request.args.get('end') or config.RECORDS_PER_PAGE
  end = int(end)
  width = end - start
  
  nav_offsets = get_navigation_offsets(start, end, config.RECORDS_PER_PAGE)
  
  flights = client.agile_data_science.on_time_performance.find(
    {
      'Origin': origin,
      'Dest': dest,
      'FlightDate': flight_date
    },
    sort = [
      ('DepTime', 1),
      ('ArrTime', 1)
    ]
  )
  flight_count = flights.count()
  flights = flights.skip(start).limit(width)
    
  return render_template(
    'flights.html', 
    flights=flights, 
    flight_date=flight_date, 
    flight_count=flight_count,
    nav_path=request.path,
    nav_offsets=nav_offsets
    )

if __name__ == "__main__":
  app.run(debug=True)

'''
a. 浏览器： http://localhost:5000/flights/ATL/SFO/2015-01-01
//输出
Agile Data Science

9 Flights on 2015-01-01
Airline 	Flight Number 	Origin 	Destination 	Departure Time 	Tail Number 	Air Time 	Distance
UA 	1746 	ATL 	SFO 	0741 	N18223 	300.0 	2139.0
DL 	2049 	ATL 	SFO 	0815 	N6709 	278.0 	2139.0
WN 	1579 	ATL 	SFO 	0848 	N429WN 	292.0 	2139.0
DL 	1680 	ATL 	SFO 	1043 	N129DL 	277.0 	2139.0
DL 	1366 	ATL 	SFO 	1400 	N6703D 	281.0 	2139.0
DL 	241 	ATL 	SFO 	1745 	N666DN 	283.0 	2139.0
DL 	2265 	ATL 	SFO 	1925 	N584NW 	268.0 	2139.0
WN 	545 	ATL 	SFO 	1943 	N262WN 	285.0 	2139.0
DL 	753 	ATL 	SFO 	2147 	N810DN 	285.0 	2139.0
Previous Next

Agile Data Science by Russell Jurney, 2016

b. 浏览器： http://localhost:5000/flights/ATL/SFO/2015-01-01?start=5&end=10
//输出
Agile Data Science

9 Flights on 2015-01-01
Airline 	Flight Number 	Origin 	Destination 	Departure Time 	Tail Number 	Air Time 	Distance
DL 	241 	ATL 	SFO 	1745 	N666DN 	283.0 	2139.0
DL 	2265 	ATL 	SFO 	1925 	N584NW 	268.0 	2139.0
WN 	545 	ATL 	SFO 	1943 	N262WN 	285.0 	2139.0
DL 	753 	ATL 	SFO 	2147 	N810DN 	285.0 	2139.0
Previous Next

Agile Data Science by Russell Jurney, 2016

'''
