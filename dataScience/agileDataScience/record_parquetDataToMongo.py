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

# Load the parquet file back
on_time_dataframe = spark.read.parquet('data/on_time_performance.parquet')
on_time_dataframe.show() 

+----+-------+-----+----------+---------+----------+-------+-------+---------+------+--------------------+-----------+----+--------------------+---------+-------+--------+---------------+-------+------+---------+--------+-------+--------+---------------+---------+--------+-----------------+-------+-------+--------+------------+------------+--------+-------------+-----------------+----------+----------+
|Year|Quarter|Month|DayofMonth|DayOfWeek|FlightDate|Carrier|TailNum|FlightNum|Origin|      OriginCityName|OriginState|Dest|        DestCityName|DestState|DepTime|DepDelay|DepDelayMinutes|TaxiOut|TaxiIn|WheelsOff|WheelsOn|ArrTime|ArrDelay|ArrDelayMinutes|Cancelled|Diverted|ActualElapsedTime|AirTime|Flights|Distance|CarrierDelay|WeatherDelay|NASDelay|SecurityDelay|LateAircraftDelay|CRSDepTime|CRSArrTime|
+----+-------+-----+----------+---------+----------+-------+-------+---------+------+--------------------+-----------+----+--------------------+---------+-------+--------+---------------+-------+------+---------+--------+-------+--------+---------------+---------+--------+-----------------+-------+-------+--------+------------+------------+--------+-------------+-----------------+----------+----------+
|2015|      1|    1|         1|        4|2015-01-01|     AA| N001AA|     1519|   DFW|Dallas/Fort Worth...|         TX| MEM|         Memphis, TN|       TN|   1342|    -3.0|              0|   16.0|   7.0|     1358|    1457|   1504|    -6.0|            0.0|        0|       0|             82.0|   59.0|      1|   432.0|        null|        null|    null|         null|             null|      1345|      1510|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N001AA|     1519|   MEM|         Memphis, TN|         TN| DFW|Dallas/Fort Worth...|       TX|   1546|    -4.0|              0|    9.0|   9.0|     1555|    1712|   1721|    -9.0|            0.0|        0|       0|             95.0|   77.0|      1|   432.0|        null|        null|    null|         null|             null|      1550|      1730|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N002AA|     2349|   ORD|         Chicago, IL|         IL| DFW|Dallas/Fort Worth...|       TX|   1845|     0.0|              0|   31.0|  16.0|     1916|    2125|   2141|    26.0|           26.0|        0|       0|            176.0|  129.0|      1|   802.0|         0.0|         0.0|    26.0|          0.0|              0.0|      1845|      2115|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N003AA|     1298|   DFW|Dallas/Fort Worth...|         TX| ATL|         Atlanta, GA|       GA|   2000|   100.0|            100|   33.0|   6.0|     2033|    2306|   2312|   112.0|          112.0|        0|       0|            132.0|   93.0|      1|   731.0|        19.0|         0.0|    12.0|          0.0|             81.0|      1820|      2120|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N003AA|     1422|   DFW|Dallas/Fort Worth...|         TX| HDN|          Hayden, CO|       CO|   0918|    78.0|             78|   30.0|   4.0|     0948|    1039|   1043|    78.0|           78.0|        0|       0|            145.0|  111.0|      1|   769.0|        78.0|         0.0|     0.0|          0.0|              0.0|      0800|      0925|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N003AA|     1422|   HDN|          Hayden, CO|         CO| DFW|Dallas/Fort Worth...|       TX|   1537|   332.0|            332|   16.0|  15.0|     1553|    1841|   1856|   336.0|          336.0|        0|       0|            139.0|  108.0|      1|   769.0|       254.0|         0.0|     4.0|          0.0|             78.0|      1005|      1320|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N004AA|     2287|   JAC|         Jackson, WY|         WY| DFW|Dallas/Fort Worth...|       TX|   0756|    -4.0|              0|   49.0|  10.0|     0845|    1211|   1221|    21.0|           21.0|        0|       0|            205.0|  146.0|      1|  1047.0|         0.0|         0.0|    21.0|          0.0|              0.0|      0800|      1200|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N005AA|     1080|   EGE|           Eagle, CO|         CO| ORD|         Chicago, IL|       IL|   null|    null|           null|   null|  null|     null|    null|   null|    null|           null|        1|       0|             null|   null|      1|  1007.0|        null|        null|    null|         null|             null|      1415|      1755|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N005AA|     1080|   ORD|         Chicago, IL|         IL| EGE|           Eagle, CO|       CO|   null|    null|           null|   null|  null|     null|    null|   null|    null|           null|        1|       0|             null|   null|      1|  1007.0|        null|        null|    null|         null|             null|      1145|      1335|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N005AA|     2332|   DFW|Dallas/Fort Worth...|         TX| ORD|         Chicago, IL|       IL|   null|    null|           null|   null|  null|     null|    null|   null|    null|           null|        1|       0|             null|   null|      1|   802.0|        null|        null|    null|         null|             null|      0740|      0955|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N006AA|      194|   DFW|Dallas/Fort Worth...|         TX| ATL|         Atlanta, GA|       GA|   null|    null|           null|   null|  null|     null|    null|   null|    null|           null|        1|       0|             null|   null|      1|   731.0|        null|        null|    null|         null|             null|      1150|      1445|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N006AA|      356|   ATL|         Atlanta, GA|         GA| DFW|Dallas/Fort Worth...|       TX|   1635|    -5.0|              0|   15.0|  14.0|     1650|    1752|   1806|     1.0|            1.0|        0|       0|            151.0|  122.0|      1|   731.0|        null|        null|    null|         null|             null|      1640|      1805|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N006AA|      356|   DFW|Dallas/Fort Worth...|         TX| ATL|         Atlanta, GA|       GA|   1256|    -4.0|              0|   15.0|   4.0|     1311|    1545|   1549|   -11.0|            0.0|        0|       0|            113.0|   94.0|      1|   731.0|        null|        null|    null|         null|             null|      1300|      1600|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N007AA|     2396|   DFW|Dallas/Fort Worth...|         TX| ATL|         Atlanta, GA|       GA|   2111|    76.0|             76|   30.0|   4.0|     2141|    0012|   0016|    86.0|           86.0|        0|       0|            125.0|   91.0|      1|   731.0|         0.0|         5.0|    10.0|          0.0|             71.0|      1955|      2250|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N008AA|     1513|   ATL|         Atlanta, GA|         GA| DFW|Dallas/Fort Worth...|       TX|   1043|    -2.0|              0|   13.0|  17.0|     1056|    1151|   1208|    -7.0|            0.0|        0|       0|            145.0|  115.0|      1|   731.0|        null|        null|    null|         null|             null|      1045|      1215|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N008AA|     1513|   DFW|Dallas/Fort Worth...|         TX| ATL|         Atlanta, GA|       GA|   0655|    -5.0|              0|   11.0|   5.0|     0706|    0935|   0940|   -25.0|            0.0|        0|       0|            105.0|   89.0|      1|   731.0|        null|        null|    null|         null|             null|      0700|      1005|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N009AA|      937|   DFW|Dallas/Fort Worth...|         TX| EGE|           Eagle, CO|       CO|   1635|    35.0|             35|   12.0|   4.0|     1647|    1733|   1737|    17.0|           17.0|        0|       0|            122.0|  106.0|      1|   721.0|        17.0|         0.0|     0.0|          0.0|              0.0|      1600|      1720|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N009AA|      937|   EGE|           Eagle, CO|         CO| LAX|     Los Angeles, CA|       CA|   1815|    10.0|             10|   10.0|   9.0|     1825|    1859|   1908|   -12.0|            0.0|        0|       0|            113.0|   94.0|      1|   748.0|        null|        null|    null|         null|             null|      1805|      1920|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N010AA|     1212|   DFW|Dallas/Fort Worth...|         TX| SDF|      Louisville, KY|       KY|   null|    null|           null|   null|  null|     null|    null|   null|    null|           null|        1|       0|             null|   null|      1|   733.0|        null|        null|    null|         null|             null|      1145|      1440|
|2015|      1|    1|         1|        4|2015-01-01|     AA| N010AA|     1212|   SDF|      Louisville, KY|         KY| DFW|Dallas/Fort Worth...|       TX|   null|    null|           null|   null|  null|     null|    null|   null|    null|           null|        1|       0|             null|   null|      1|   733.0|        null|        null|    null|         null|             null|      1520|      1640|
+----+-------+-----+----------+---------+----------+-------+-------+---------+------+--------------------+-----------+----+--------------------+---------+-------+--------+---------------+-------+------+---------+--------+-------+--------+---------------+---------+--------+-----------------+-------+-------+--------+------------+------------+--------+-------------+-----------------+----------+----------+
only showing top 20 rows
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
