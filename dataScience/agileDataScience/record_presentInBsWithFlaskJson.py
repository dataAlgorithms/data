#!/usr/bin/env python

from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import json_util
import json

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

    return json_util.dumps(flight, indent=10)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
'''
浏览器中： http://127.0.0.1:5000/on_time_performance?Carrier=AA&FlightDate=2015-01-01&FlightNum=1519

{
    "WeatherDelay": null,
    "WheelsOff": "1358",
    "ActualElapsedTime": 82,
    "TaxiIn": 7,
    "DepDelayMinutes": 0,
    "_id": {
        "$oid": "599224cb4e95403a7319c0eb"
    },
    "Origin": "DFW",
    "FlightDate": "2015-01-01",
    "DestCityName": "Memphis, TN",
    "CarrierDelay": null,
    "LateAircraftDelay": null,
    "Cancelled": 0,
    "Month": "1",
    "AirTime": 59,
    "TailNum": "N001AA",
    "DepDelay": -3,
    "TaxiOut": 16,
    "FlightNum": "1519",
    "SecurityDelay": null,
    "NASDelay": null,
    "OriginState": "TX",
    "Quarter": "1",
    "DestState": "TN",
    "ArrTime": "1504",
    "OriginCityName": "Dallas/Fort Worth, TX",
    "DayofMonth": "1",
    "Flights": 1,
    "Carrier": "AA",
    "Diverted": 0,
    "CRSDepTime": "1345",
    "DepTime": "1342",
    "CRSArrTime": "1510",
    "WheelsOn": "1457",
    "ArrDelayMinutes": 0,
    "ArrDelay": -6,
    "Distance": 432,
    "Dest": "MEM",
    "Year": "2015",
    "DayOfWeek": "4"
}
'''
