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

'''
