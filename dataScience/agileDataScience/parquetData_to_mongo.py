#!/usr/bin/env python

import pymongo
import pymongo_spark
pymongo_spark.activate()

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

'''
parquet data:


'''
on_time_dataframe = spark.read.parquet('data/on_time_performance.parquet')

as_dict = on_time_dataframe.rdd.map(lambda row: row.asDict())
as_dict.saveToMongoDB('mongodb://localhost:27017/agile_data_science.on_time_performance')

'''
mongodb ensure index (query quickly)

db.on_time_performance.ensureIndex({Carrier: 1, FlightDate: 1, FlightNum: 1})
'''

'''
mongodb query result:

mongo agile_data_science
MongoDB shell version v3.4.2
connecting to: mongodb://127.0.0.1:27017/agile_data_science
MongoDB server version: 3.4.2
Server has startup warnings: 
2017-08-09T15:01:54.581-0700 I STORAGE  [initandlisten] 
2017-08-09T15:01:54.581-0700 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2017-08-09T15:01:54.581-0700 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2017-08-09T15:01:55.840-0700 I CONTROL  [initandlisten] 
2017-08-09T15:01:55.840-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2017-08-09T15:01:55.840-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2017-08-09T15:01:55.840-0700 I CONTROL  [initandlisten] ** WARNING: You are running this process as the root user, which is not recommended.
2017-08-09T15:01:55.840-0700 I CONTROL  [initandlisten] 
2017-08-09T15:01:55.843-0700 I CONTROL  [initandlisten] 
2017-08-09T15:01:55.843-0700 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
2017-08-09T15:01:55.843-0700 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2017-08-09T15:01:55.844-0700 I CONTROL  [initandlisten] 
2017-08-09T15:01:55.844-0700 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/defrag is 'always'.
2017-08-09T15:01:55.844-0700 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
2017-08-09T15:01:55.844-0700 I CONTROL  [initandlisten] 
> db
agile_data_science
> db.on_time_performance.findOne()
{
	"_id" : ObjectId("599224cb4e95403a7319c0eb"),
	"Origin" : "DFW",
	"Quarter" : "1",
	"FlightNum" : "1519",
	"LateAircraftDelay" : null,
	"NASDelay" : null,
	"DestState" : "TN",
	"ArrTime" : "1504",
	"AirTime" : 59,
	"DepTime" : "1342",
	"Month" : "1",
	"Flights" : 1,
	"Carrier" : "AA",
	"DayofMonth" : "1",
	"Distance" : 432,
	"CRSDepTime" : "1345",
	"SecurityDelay" : null,
	"DayOfWeek" : "4",
	"Dest" : "MEM",
	"DepDelayMinutes" : 0,
	"DepDelay" : -3,
	"WheelsOff" : "1358",
	"TaxiIn" : 7,
	"Cancelled" : 0,
	"Diverted" : 0,
	"ArrDelay" : -6,
	"TaxiOut" : 16,
	"ActualElapsedTime" : 82,
	"CarrierDelay" : null,
	"FlightDate" : "2015-01-01",
	"OriginCityName" : "Dallas/Fort Worth, TX",
	"Year" : "2015",
	"OriginState" : "TX",
	"WeatherDelay" : null,
	"ArrDelayMinutes" : 0,
	"CRSArrTime" : "1510",
	"TailNum" : "N001AA",
	"WheelsOn" : "1457",
	"DestCityName" : "Memphis, TN"
}
> db.on_time_performance.findOne({Carrier: 'AA', FlightDate: '2015-01-01', FlightNum: "1519"})
{
	"_id" : ObjectId("599224cb4e95403a7319c0eb"),
	"Origin" : "DFW",
	"Quarter" : "1",
	"FlightNum" : "1519",
	"LateAircraftDelay" : null,
	"NASDelay" : null,
	"DestState" : "TN",
	"ArrTime" : "1504",
	"AirTime" : 59,
	"DepTime" : "1342",
	"Month" : "1",
	"Flights" : 1,
	"Carrier" : "AA",
	"DayofMonth" : "1",
	"Distance" : 432,
	"CRSDepTime" : "1345",
	"SecurityDelay" : null,
	"DayOfWeek" : "4",
	"Dest" : "MEM",
	"DepDelayMinutes" : 0,
	"DepDelay" : -3,
	"WheelsOff" : "1358",
	"TaxiIn" : 7,
	"Cancelled" : 0,
	"Diverted" : 0,
	"ArrDelay" : -6,
	"TaxiOut" : 16,
	"ActualElapsedTime" : 82,
	"CarrierDelay" : null,
	"FlightDate" : "2015-01-01",
	"OriginCityName" : "Dallas/Fort Worth, TX",
	"Year" : "2015",
	"OriginState" : "TX",
	"WeatherDelay" : null,
	"ArrDelayMinutes" : 0,
	"CRSArrTime" : "1510",
	"TailNum" : "N001AA",
	"WheelsOn" : "1457",
	"DestCityName" : "Memphis, TN"
}
> exit
bye

'''
