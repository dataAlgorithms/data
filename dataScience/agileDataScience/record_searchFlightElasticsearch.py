#!/usr/bin/env python

import sys, os, re
from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import json_util
import config
import json

from pyelasticsearch import ElasticSearch
elastic = ElasticSearch(config.ELASTIC_URL)

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

@app.route("/flights/search")
@app.route("/flights/search/")
def search_flights():
  
  # Search parameters
  carrier = request.args.get('Carrier')
  flight_date = request.args.get('FlightDate')
  origin = request.args.get('Origin')
  dest = request.args.get('Dest')
  tail_number = request.args.get('TailNum')
  flight_number = request.args.get('FlightNum')
  
  # Pagination parameters
  start = request.args.get('start') or 0
  start = int(start)
  end = request.args.get('end') or config.RECORDS_PER_PAGE
  end = int(end)
  
  print(request.args)
  # Navigation path and offset setup
  nav_path = strip_place(request.url)
  nav_offsets = get_navigation_offsets(start, end, config.RECORDS_PER_PAGE)
  
  # Build the base of our elasticsearch query
  query = {
    'query': {
      'bool': {
        'must': []}
    },
    'sort': [
      {'FlightDate': {'order': 'asc', 'ignore_unmapped' : True} },
      {'DepTime': {'order': 'asc', 'ignore_unmapped' : True} },
      {'Carrier': {'order': 'asc', 'ignore_unmapped' : True} },
      {'FlightNum': {'order': 'asc', 'ignore_unmapped' : True} },
      '_score'
    ],
    'from': start,
    'size': config.RECORDS_PER_PAGE
  }
  
  # Add any search parameters present
  if carrier:
    query['query']['bool']['must'].append({'match': {'Carrier': carrier}})
  if flight_date:
    query['query']['bool']['must'].append({'match': {'FlightDate': flight_date}})
  if origin: 
    query['query']['bool']['must'].append({'match': {'Origin': origin}})
  if dest: 
    query['query']['bool']['must'].append({'match': {'Dest': dest}})
  if tail_number: 
    query['query']['bool']['must'].append({'match': {'TailNum': tail_number}})
  if flight_number: 
    query['query']['bool']['must'].append({'match': {'FlightNum': flight_number}})
  
  # Query elasticsearch, process to get records and count
  print("QUERY")
  print(carrier, flight_date, origin, dest, tail_number, flight_number)
  print(json.dumps(query))
  results = elastic.search(query)
  flights, flight_count = process_search(results)
  
  # Persist search parameters in the form template
  return render_template(
    'search.html', 
    flights=flights, 
    flight_date=flight_date, 
    flight_count=flight_count,
    nav_path=nav_path,
    nav_offsets=nav_offsets,
    carrier=carrier,
    origin=origin,
    dest=dest,
    tail_number=tail_number,
    flight_number=flight_number
    )

'''
http://localhost:5000/flights/search/?Carrier=&Origin=JFK&Dest=LAX&FlightDate=2015-02-01&TailNum=&FlightNum=


Agile Data Science

33 Flights
Carrier Origin Dest FlightDate TailNum FlightNum
Airline 	Flight Number 	Origin 	Destination 	Date 	Departure Time 	Tail Number 	Air Time 	Distance
AA 	171 	JFK 	LAX 	2015-02-01 	0557 	N790AA 	331.0 	2475.0
B6 	23 	JFK 	LAX 	2015-02-01 	0628 	N934JB 	332.0 	2475.0
AA 	9 	JFK 	LAX 	2015-02-01 	0653 	N791AA 	334.0 	2475.0
AA 	33 	JFK 	LAX 	2015-02-01 	0754 	N795AA 	348.0 	2475.0
B6 	123 	JFK 	LAX 	2015-02-01 	0814 	N937JB 	333.0 	2475.0
UA 	443 	JFK 	LAX 	2015-02-01 	0831 	N502UA 	335.0 	2475.0
AA 	1 	JFK 	LAX 	2015-02-01 	0857 	N796AA 	323.0 	2475.0
'''
if __name__ == "__main__":
  app.run(debug=True)

'''
cat search.html

{% extends "layout.html" %}
{% block body %}
  <div>
    <p class="lead">{{flight_count}} Flights</p>
    <form action="/flights/search" method="get">
      <label for="Carrier">Carrier</label>
      <input name="Carrier" maxlength="3" style="width: 36px; margin-right: 10px;" value="{{carrier if carrier else ''}}"></input>
      <label for="Origin">Origin</label>
      <input name="Origin" maxlength="3" style="width: 36px; margin-right: 10px;" value="{{origin if origin else ''}}"></input>
      <label for="Dest">Dest</label>
      <input name="Dest" maxlength="3" style="width: 36px; margin-right: 10px;" value="{{dest if dest else ''}}"></input>
      <label for="FlightDate">FlightDate</label>
      <input name="FlightDate" style="width: 100px; margin-right: 10px;" value="{{flight_date if flight_date else ''}}"></input>
      <label for="TailNum">TailNum</label>
      <input name="TailNum" style="width: 100px; margin-right: 10px;" value="{{tail_number if tail_number else ''}}"></input>
      <label for="FlightNum">FlightNum</label>
      <input name="FlightNum" style="width: 50px; margin-right: 10px;" value="{{flight_number if flight_number else ''}}"></input>
      <button type="submit" class="btn btn-xs btn-default" style="height: 25px">Submit</button>
    </form>
    <table class="table table-condensed table-striped">
      <thead>
        <th>Airline</th>
        <th>Flight Number</th>
        <th>Origin</th>
        <th>Destination</th>
        <th>Date</th>
        <th>Departure Time</th>
        <th>Tail Number</th>
        <th>Air Time</th>
        <th>Distance</th>
      </thead>
      <tbody>
        {% for flight in flights %}
        <tr>
          <td><a href="/airline/{{flight.Carrier}}">{{flight.Carrier}}</a></td>
          <td><a href="/on_time_performance?Carrier={{flight.Carrier}}&FlightDate={{flight.FlightDate}}&FlightNum={{flight.FlightNum}}">{{flight.FlightNum}}</a></td>
          <td>{{flight.Origin}}</td>
          <td>{{flight.Dest}}</td>
          <td>{{flight.FlightDate}}</td>
          <td>{{flight.DepTime}}</td>
          <td>{{flight.TailNum}}</td>
          <td>{{flight.AirTime}}</td>
          <td>{{flight.Distance}}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  {% import "macros.jnj" as common %}
  {% if nav_offsets and nav_path -%}
    {{ common.display_nav(nav_offsets, nav_path, flight_count)|safe }}
  {% endif -%}
{% endblock %}
'''
