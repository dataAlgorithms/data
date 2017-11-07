#!/usr/bin/env python

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Load the Parquet file
on_time_dataframe = spark.read.parquet('data/on_time_performance.parquet')

# Use SQL to look at the total flights by month across 2015
on_time_dataframe.registerTempTable("on_time_dataframe")
total_flights_by_month = spark.sql(
"""Select Month, Year, Count(*) as total_flights
from on_time_dataframe
group by Year, Month
order by Year, Month"""
)

# This map/asDict trick makes the rows print a little prettier,
# It is optional
flights_chart_data = total_flights_by_month.rdd.map(lambda row: row.asDict())
print(flights_chart_data.collect())

# Save chart to MongoDB
import pymongo_spark
pymongo_spark.activate()
flights_chart_data.saveToMongoDB('mongodb://localhost:27017/agile_data_science.flights_by_month')

'''
[root@localhost workspace]# python total_flights.py 
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
17/11/07 14:35:03 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/11/07 14:35:03 WARN SparkConf: 
SPARK_CLASSPATH was detected (set to '/root/workspace/lib/snappy-java-1.1.2.6.jar').
This is deprecated in Spark 1.0+.

Please instead use:
 - ./spark-submit with --driver-class-path to augment the driver classpath
 - spark.executor.extraClassPath to augment the executor classpath
        
17/11/07 14:35:03 WARN SparkConf: Setting 'spark.executor.extraClassPath' to '/root/workspace/lib/snappy-java-1.1.2.6.jar' as a work-around.
17/11/07 14:35:03 WARN SparkConf: Setting 'spark.driver.extraClassPath' to '/root/workspace/lib/snappy-java-1.1.2.6.jar' as a work-around.
17/11/07 14:35:03 WARN Utils: Your hostname, localhost.localdomain resolves to a loopback address: 127.0.0.1; using 192.168.1.103 instead (on interface eth0)
17/11/07 14:35:03 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
17/11/07 14:35:06 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
[{'Year': '2015', 'Month': '1', 'total_flights': 469968}, {'Year': '2015', 'Month': '10', 'total_flights': 486165},
{'Year': '2015', 'Month': '11', 'total_flights': 467972}, {'Year': '2015', 'Month': '12', 'total_flights': 479230},
{'Year': '2015', 'Month': '2', 'total_flights': 429191}, {'Year': '2015', 'Month': '3', 'total_flights': 504312}, 
{'Year': '2015', 'Month': '4', 'total_flights': 485151}, {'Year': '2015', 'Month': '5', 'total_flights': 496993}, 
{'Year': '2015', 'Month': '6', 'total_flights': 503897}, {'Year': '2015', 'Month': '7', 'total_flights': 520718},
{'Year': '2015', 'Month': '8', 'total_flights': 510536}, {'Year': '2015', 'Month': '9', 'total_flights': 464946}]
'''

'''
[root@localhost workspace]# mongo agile_data_science
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
> db.flights_by_month.find().sort({"Year": 1, "Month": 1})
{ "_id" : ObjectId("599a09f14e9540530def1276"), "total_flights" : 469968, "Month" : "1", "Year" : "2015" }
{ "_id" : ObjectId("599a0aaf4e954054637f7559"), "total_flights" : 469968, "Month" : "1", "Year" : "2015" }
{ "_id" : ObjectId("5a0235464e954017f9eff004"), "total_flights" : 469968, "Month" : "1", "Year" : "2015" }
{ "_id" : ObjectId("599a09f34e9540530def1279"), "total_flights" : 486165, "Month" : "10", "Year" : "2015" }
{ "_id" : ObjectId("599a0ab04e954054637f755c"), "total_flights" : 486165, "Month" : "10", "Year" : "2015" }
{ "_id" : ObjectId("5a0235464e954017f9eff007"), "total_flights" : 486165, "Month" : "10", "Year" : "2015" }
{ "_id" : ObjectId("599a09f44e9540530def127c"), "total_flights" : 467972, "Month" : "11", "Year" : "2015" }
{ "_id" : ObjectId("599a0ab04e954054637f755f"), "total_flights" : 467972, "Month" : "11", "Year" : "2015" }
{ "_id" : ObjectId("5a0235464e954017f9eff00a"), "total_flights" : 467972, "Month" : "11", "Year" : "2015" }
{ "_id" : ObjectId("599a09f44e9540530def127f"), "total_flights" : 479230, "Month" : "12", "Year" : "2015" }
{ "_id" : ObjectId("599a0ab04e954054637f7562"), "total_flights" : 479230, "Month" : "12", "Year" : "2015" }
{ "_id" : ObjectId("5a0235464e954017f9eff00d"), "total_flights" : 479230, "Month" : "12", "Year" : "2015" }
{ "_id" : ObjectId("599a09f44e9540530def1282"), "total_flights" : 429191, "Month" : "2", "Year" : "2015" }
{ "_id" : ObjectId("599a0ab04e954054637f7565"), "total_flights" : 429191, "Month" : "2", "Year" : "2015" }
{ "_id" : ObjectId("5a0235464e954017f9eff010"), "total_flights" : 429191, "Month" : "2", "Year" : "2015" }
{ "_id" : ObjectId("599a09f44e9540530def1285"), "total_flights" : 504312, "Month" : "3", "Year" : "2015" }
{ "_id" : ObjectId("599a0ab04e954054637f7568"), "total_flights" : 504312, "Month" : "3", "Year" : "2015" }
{ "_id" : ObjectId("5a0235474e954017f9eff013"), "total_flights" : 504312, "Month" : "3", "Year" : "2015" }
{ "_id" : ObjectId("599a09f44e9540530def1288"), "total_flights" : 485151, "Month" : "4", "Year" : "2015" }
{ "_id" : ObjectId("599a0ab14e954054637f756b"), "total_flights" : 485151, "Month" : "4", "Year" : "2015" }
Type "it" for more
'''
