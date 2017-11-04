#!/usr/bin/env python

from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import json_util

# Set up Flask and Mongo
app = Flask(__name__)
client = MongoClient()

# Controller: Fetch a flight and display it
@app.route("/on_time_performance")
def on_time_performance():

    carrier = request.args.get('Carrier')
    flight_date = request.args.get('FlightDate')
    flight_num = request.args.get('FlightNum')

    flight = client.agile_data_science.on_time_performance.find_one({
        'Carrier': carrier,
        'FlightDate': flight_date,
        'FlightNum': flight_num
    })

    return render_template('flight.html', flight=flight)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
'''
浏览器： http://127.0.0.1:5000/on_time_performance?Carrier=AA&FlightDate=2015-01-01&FlightNum=1519

结果：
Agile Data Science

Flight 1519
Airline 	Origin 	Destination 	Tail Number 	Date 	Air Time 	Distance
AA 	DFW 	MEM 	N001AA 	2015-01-01 	59.0 	432.0

Agile Data Science by Russell Jurney, 2016

说明：
flight.html, layout.html在templates文件夹中
bootstrap.min.css,bootstrap-theme.min.css,bootstrap.min.js在static文件夹中
[root@localhost templates]# cat flight.html 
{% extends "layout.html" %}
{% block body %}
  <div>
    <p class="lead">Flight {{flight.FlightNum}}</p>
    <table class="table">
      <thead>
        <th>Airline</th>
        <th>Origin</th>
        <th>Destination</th>
        <th>Tail Number</th>
        <th>Date</th>
        <th>Air Time</th>
        <th>Distance</th>
      </thead>
      <tbody>
        <tr>
          <td><a href="/airline/{{flight.Carrier}}">{{flight.Carrier}}</a></td>
          <td>{{flight.Origin}}</td>
          <td>{{flight.Dest}}</td>
          <td>{{flight.TailNum}}</td>
          <td>{{flight.FlightDate}}</td>
          <td>{{flight.AirTime}}</td>
          <td>{{flight.Distance}}</td>
        </tr>
      </tbody>
    </table>
  </div>
{% endblock %}

[root@localhost templates]# cat layout.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Agile Data Science</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Chapter 5 example in Agile Data Science, 2.0">
    <meta name="author" content="Russell Jurney">
    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <link href="/static/bootstrap-theme.min.css" rel="stylesheet">
  </head>

  <body>
    <div id="wrap">

      <!-- Begin page content -->
      <div class="container">
        <div class="page-header">
          <h1>Agile Data Science</h1>
        </div>
        {% block body %}{% endblock %}
      </div>

      <div id="push"></div>
    </div>

    <div id="footer">
      <div class="container">
        <p class="muted credit"><a href="http://shop.oreilly.com/product/0636920025054.do">Agile Data Science</a> by <a href="http://www.linkedin.com/in/russelljurney">Russell Jurney</a>, 2016
      </div>
    </div>
    <script src="/static/bootstrap.min.js"></script>
  </body>
</html>
'''
