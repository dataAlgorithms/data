#coding=utf-8
'''
数据收集或者采集的方法

1. 从某个网站直接下载
适合： 政府类公开的数据 （比如： 航班历史数据）
技术： wget
      使用： wget -P data http://s3.amazonaws.com/agile_data_science/On_Time_On_Time_Performance_2015.csv.bz2

2. 使用爬虫到网站去爬
适合： 无法直接获取
技术： python requests + beautifulSoup4 或者python scrapy
'''

# download the flight data
import wget # pip install wget (https://pypi.python.org/pypi/wget/)
url = "http://s3.amazonaws.com/agile_data_science/On_Time_On_Time_Performance_2015.csv.bz2"
filename = wget.download(url, bar=bar_thermometer)
print(filename)

# check the csv data
'''
"Year","Quarter","Month","DayofMonth","DayOfWeek","FlightDate","UniqueCarrier","
AirlineID","Carrier","TailNum","FlightNum","OriginAirportID","OriginAirportSeqID
","OriginCityMarketID","Origin","OriginCityName","OriginState","OriginStateFips"
,"OriginStateName","OriginWac","DestAirportID","DestAirportSeqID","DestCityMarke
tID","Dest","DestCityName","DestState","DestStateFips","DestStateName","DestWac"
,"CRSDepTime","DepTime","DepDelay","DepDelayMinutes","DepDel15","DepartureDelayG
roups","DepTimeBlk","TaxiOut","WheelsOff","WheelsOn","TaxiIn","CRSArrTime","ArrT
ime","ArrDelay","ArrDelayMinutes","ArrDel15","ArrivalDelayGroups","ArrTimeBlk","
Cancelled","CancellationCode","Diverted","CRSElapsedTime","ActualElapsedTime","A
irTime","Flights","Distance","DistanceGroup","CarrierDelay","WeatherDelay","NASD
elay","SecurityDelay","LateAircraftDelay","FirstDepTime","TotalAddGTime","Longes
tAddGTime","DivAirportLandings","DivReachedDest","DivActualElapsedTime","DivArrD
elay","DivDistance","Div1Airport","Div1AirportID","Div1AirportSeqID","Div1Wheels
On","Div1TotalGTime","Div1LongestGTime","Div1WheelsOff","Div1TailNum","Div2Airpo
rt","Div2AirportID","Div2AirportSeqID","Div2WheelsOn","Div2TotalGTime","Div2Long
estGTime","Div2WheelsOff","Div2TailNum","Div3Airport","Div3AirportID","Div3Airpo
rtSeqID","Div3WheelsOn","Div3TotalGTime","Div3LongestGTime","Div3WheelsOff","Div
3TailNum","Div4Airport","Div4AirportID","Div4AirportSeqID","Div4WheelsOn","Div4T
otalGTime","Div4LongestGTime","Div4WheelsOff","Div4TailNum","Div5Airport","Div5A
irportID","Div5AirportSeqID","Div5WheelsOn","Div5TotalGTime","Div5LongestGTime",
"Div5WheelsOff","Div5TailNum",
2015,1,1,1,4,2015-01-01,"AA",19805,"AA","N001AA","1519",11298,1129803,30194,"DFW
","Dallas/Fort Worth, TX","TX","48","Texas",74,13244,1324402,33244,"MEM","Memphi
s, TN","TN","47","Tennessee",54,"1345","1342",-3.00,0.00,0.00,-1,"1300-1359",16.
00,"1358","1457",7.00,"1510","1504",-6.00,0.00,0.00,-1,"1500-1559",0.00,"",0.00,
85.00,82.00,59.00,1.00,432.00,2,,,,,,"",,,0,,,,,"",,,"",,,"","","",,,"",,,"","",
"",,,"",,,"","","",,,"",,,"","","",,,"",,,"","",
-- More  --
'''

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Loads CSV with header parsing and type inference, in one line!
on_time_dataframe = spark.read.format('com.databricks.spark.csv')\
  .options(
    header='true',
    treatEmptyValuesAsNulls='true',
  )\
  .load('data/On_Time_On_Time_Performance_2015.csv.bz2')
on_time_dataframe.registerTempTable("on_time_performance")

trimmed_cast_performance = spark.sql("""
SELECT
  Year, Quarter, Month, DayofMonth, DayOfWeek, FlightDate,
  Carrier, TailNum, FlightNum,
  Origin, OriginCityName, OriginState,
  Dest, DestCityName, DestState,
  DepTime, cast(DepDelay as float), cast(DepDelayMinutes as int),
  cast(TaxiOut as float), cast(TaxiIn as float),
  WheelsOff, WheelsOn,
  ArrTime, cast(ArrDelay as float), cast(ArrDelayMinutes as float),
  cast(Cancelled as int), cast(Diverted as int),
  cast(ActualElapsedTime as float), cast(AirTime as float),
  cast(Flights as int), cast(Distance as float),
  cast(CarrierDelay as float), cast(WeatherDelay as float), cast(NASDelay as float),
  cast(SecurityDelay as float), cast(LateAircraftDelay as float),
  CRSDepTime, CRSArrTime
FROM
  on_time_performance
""")

# Replace on_time_performance table with our new, trimmed table and show its contents
trimmed_cast_performance.registerTempTable("on_time_performance")
trimmed_cast_performance.show()

''' be short
Year Quarter Month DayofMonth DayOfWeek FlightDate Carrier TailNum FlightNum Origin
2015 1 1 1 4 2015-01-01 AA N001AA 1519 DFW
2015 1 1 1 4 2015-01-01 AA N001AA 1519 MEM
2015 1 1 1 4 2015-01-01 AA N002AA 2349 ORD
2015 1 1 1 4 2015-01-01 AA N003AA 1298 DFW
2015 1 1 1 4 2015-01-01 AA N003AA 1422 DFW
'''

# Verify we can sum numeric columns
spark.sql("""SELECT
  SUM(WeatherDelay), SUM(CarrierDelay), SUM(NASDelay),
  SUM(SecurityDelay), SUM(LateAircraftDelay)
FROM on_time_performance
""").show()

'''be short
sum(WeatherDelay) sum(CarrierDelay) sum(NASDelay) sum(SecurityDelay) sum(LateAircraftDelay)
3100233.0 2.0172956E7 1.4335762E7 80985.0 2.4961931E7
'''
# Save records as gzipped json lines
trimmed_cast_performance.toJSON()\
  .saveAsTextFile(
    'data/on_time_performance.jsonl.gz',
    'org.apache.hadoop.io.compress.GzipCodec'
  )

# View records on filesystem
# gunzip -c data/on_time_performance.jsonl.gz/part-00000.gz | head

'''
[root@localhost workspace]# ls data/on_time_performance.jsonl.gz/
part-00000.gz  part-00001.gz  _SUCCESS
[root@localhost workspace]#  gunzip -c data/on_time_performance.jsonl.gz/part-00000.gz | head
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N001AA","FlightNum":"1519","Origin":"DFW","OriginCityName":"Dallas/Fort Worth, TX","OriginState":"TX","Dest":"MEM","DestCityName":"Memphis, TN","DestState":"TN","DepTime":"1342","DepDelay":-3.0,"DepDelayMinutes":0,"TaxiOut":16.0,"TaxiIn":7.0,"WheelsOff":"1358","WheelsOn":"1457","ArrTime":"1504","ArrDelay":-6.0,"ArrDelayMinutes":0.0,"Cancelled":0,"Diverted":0,"ActualElapsedTime":82.0,"AirTime":59.0,"Flights":1,"Distance":432.0,"CRSDepTime":"1345","CRSArrTime":"1510"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N001AA","FlightNum":"1519","Origin":"MEM","OriginCityName":"Memphis, TN","OriginState":"TN","Dest":"DFW","DestCityName":"Dallas/Fort Worth, TX","DestState":"TX","DepTime":"1546","DepDelay":-4.0,"DepDelayMinutes":0,"TaxiOut":9.0,"TaxiIn":9.0,"WheelsOff":"1555","WheelsOn":"1712","ArrTime":"1721","ArrDelay":-9.0,"ArrDelayMinutes":0.0,"Cancelled":0,"Diverted":0,"ActualElapsedTime":95.0,"AirTime":77.0,"Flights":1,"Distance":432.0,"CRSDepTime":"1550","CRSArrTime":"1730"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N002AA","FlightNum":"2349","Origin":"ORD","OriginCityName":"Chicago, IL","OriginState":"IL","Dest":"DFW","DestCityName":"Dallas/Fort Worth, TX","DestState":"TX","DepTime":"1845","DepDelay":0.0,"DepDelayMinutes":0,"TaxiOut":31.0,"TaxiIn":16.0,"WheelsOff":"1916","WheelsOn":"2125","ArrTime":"2141","ArrDelay":26.0,"ArrDelayMinutes":26.0,"Cancelled":0,"Diverted":0,"ActualElapsedTime":176.0,"AirTime":129.0,"Flights":1,"Distance":802.0,"CarrierDelay":0.0,"WeatherDelay":0.0,"NASDelay":26.0,"SecurityDelay":0.0,"LateAircraftDelay":0.0,"CRSDepTime":"1845","CRSArrTime":"2115"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N003AA","FlightNum":"1298","Origin":"DFW","OriginCityName":"Dallas/Fort Worth, TX","OriginState":"TX","Dest":"ATL","DestCityName":"Atlanta, GA","DestState":"GA","DepTime":"2000","DepDelay":100.0,"DepDelayMinutes":100,"TaxiOut":33.0,"TaxiIn":6.0,"WheelsOff":"2033","WheelsOn":"2306","ArrTime":"2312","ArrDelay":112.0,"ArrDelayMinutes":112.0,"Cancelled":0,"Diverted":0,"ActualElapsedTime":132.0,"AirTime":93.0,"Flights":1,"Distance":731.0,"CarrierDelay":19.0,"WeatherDelay":0.0,"NASDelay":12.0,"SecurityDelay":0.0,"LateAircraftDelay":81.0,"CRSDepTime":"1820","CRSArrTime":"2120"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N003AA","FlightNum":"1422","Origin":"DFW","OriginCityName":"Dallas/Fort Worth, TX","OriginState":"TX","Dest":"HDN","DestCityName":"Hayden, CO","DestState":"CO","DepTime":"0918","DepDelay":78.0,"DepDelayMinutes":78,"TaxiOut":30.0,"TaxiIn":4.0,"WheelsOff":"0948","WheelsOn":"1039","ArrTime":"1043","ArrDelay":78.0,"ArrDelayMinutes":78.0,"Cancelled":0,"Diverted":0,"ActualElapsedTime":145.0,"AirTime":111.0,"Flights":1,"Distance":769.0,"CarrierDelay":78.0,"WeatherDelay":0.0,"NASDelay":0.0,"SecurityDelay":0.0,"LateAircraftDelay":0.0,"CRSDepTime":"0800","CRSArrTime":"0925"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N003AA","FlightNum":"1422","Origin":"HDN","OriginCityName":"Hayden, CO","OriginState":"CO","Dest":"DFW","DestCityName":"Dallas/Fort Worth, TX","DestState":"TX","DepTime":"1537","DepDelay":332.0,"DepDelayMinutes":332,"TaxiOut":16.0,"TaxiIn":15.0,"WheelsOff":"1553","WheelsOn":"1841","ArrTime":"1856","ArrDelay":336.0,"ArrDelayMinutes":336.0,"Cancelled":0,"Diverted":0,"ActualElapsedTime":139.0,"AirTime":108.0,"Flights":1,"Distance":769.0,"CarrierDelay":254.0,"WeatherDelay":0.0,"NASDelay":4.0,"SecurityDelay":0.0,"LateAircraftDelay":78.0,"CRSDepTime":"1005","CRSArrTime":"1320"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N004AA","FlightNum":"2287","Origin":"JAC","OriginCityName":"Jackson, WY","OriginState":"WY","Dest":"DFW","DestCityName":"Dallas/Fort Worth, TX","DestState":"TX","DepTime":"0756","DepDelay":-4.0,"DepDelayMinutes":0,"TaxiOut":49.0,"TaxiIn":10.0,"WheelsOff":"0845","WheelsOn":"1211","ArrTime":"1221","ArrDelay":21.0,"ArrDelayMinutes":21.0,"Cancelled":0,"Diverted":0,"ActualElapsedTime":205.0,"AirTime":146.0,"Flights":1,"Distance":1047.0,"CarrierDelay":0.0,"WeatherDelay":0.0,"NASDelay":21.0,"SecurityDelay":0.0,"LateAircraftDelay":0.0,"CRSDepTime":"0800","CRSArrTime":"1200"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N005AA","FlightNum":"1080","Origin":"EGE","OriginCityName":"Eagle, CO","OriginState":"CO","Dest":"ORD","DestCityName":"Chicago, IL","DestState":"IL","Cancelled":1,"Diverted":0,"Flights":1,"Distance":1007.0,"CRSDepTime":"1415","CRSArrTime":"1755"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N005AA","FlightNum":"1080","Origin":"ORD","OriginCityName":"Chicago, IL","OriginState":"IL","Dest":"EGE","DestCityName":"Eagle, CO","DestState":"CO","Cancelled":1,"Diverted":0,"Flights":1,"Distance":1007.0,"CRSDepTime":"1145","CRSArrTime":"1335"}
{"Year":"2015","Quarter":"1","Month":"1","DayofMonth":"1","DayOfWeek":"4","FlightDate":"2015-01-01","Carrier":"AA","TailNum":"N005AA","FlightNum":"2332","Origin":"DFW","OriginCityName":"Dallas/Fort Worth, TX","OriginState":"TX","Dest":"ORD","DestCityName":"Chicago, IL","DestState":"IL","Cancelled":1,"Diverted":0,"Flights":1,"Distance":802.0,"CRSDepTime":"0740","CRSArrTime":"0955"}
'''
# Save records using Parquet
trimmed_cast_performance.write.mode("overwrite").parquet("data/on_time_performance.parquet")

# Load JSON records back
on_time_dataframe = spark.read.json('data/on_time_performance.jsonl.gz')
on_time_dataframe.show()

'''
+-----------------+-------+--------+---------------+-------+----------+----------+---------+-------+------------+---------+----------+--------+---------------+-------+----+--------------------+---------+--------+--------+----------+---------+-------+-----------------+-----+--------+------+--------------------+-----------+-------+-------------+-------+------+-------+------------+---------+--------+----+
|ActualElapsedTime|AirTime|ArrDelay|ArrDelayMinutes|ArrTime|CRSArrTime|CRSDepTime|Cancelled|Carrier|CarrierDelay|DayOfWeek|DayofMonth|DepDelay|DepDelayMinutes|DepTime|Dest|        DestCityName|DestState|Distance|Diverted|FlightDate|FlightNum|Flights|LateAircraftDelay|Month|NASDelay|Origin|      OriginCityName|OriginState|Quarter|SecurityDelay|TailNum|TaxiIn|TaxiOut|WeatherDelay|WheelsOff|WheelsOn|Year|
+-----------------+-------+--------+---------------+-------+----------+----------+---------+-------+------------+---------+----------+--------+---------------+-------+----+--------------------+---------+--------+--------+----------+---------+-------+-----------------+-----+--------+------+--------------------+-----------+-------+-------------+-------+------+-------+------------+---------+--------+----+
|             82.0|   59.0|    -6.0|            0.0|   1504|      1510|      1345|        0|     AA|        null|        4|         1|    -3.0|              0|   1342| MEM|         Memphis, TN|       TN|   432.0|       0|2015-01-01|     1519|      1|             null|    1|    null|   DFW|Dallas/Fort Worth...|         TX|      1|         null| N001AA|   7.0|   16.0|        null|     1358|    1457|2015|
|             95.0|   77.0|    -9.0|            0.0|   1721|      1730|      1550|        0|     AA|        null|        4|         1|    -4.0|              0|   1546| DFW|Dallas/Fort Worth...|       TX|   432.0|       0|2015-01-01|     1519|      1|             null|    1|    null|   MEM|         Memphis, TN|         TN|      1|         null| N001AA|   9.0|    9.0|        null|     1555|    1712|2015|
|            176.0|  129.0|    26.0|           26.0|   2141|      2115|      1845|        0|     AA|         0.0|        4|         1|     0.0|              0|   1845| DFW|Dallas/Fort Worth...|       TX|   802.0|       0|2015-01-01|     2349|      1|              0.0|    1|    26.0|   ORD|         Chicago, IL|         IL|      1|          0.0| N002AA|  16.0|   31.0|         0.0|     1916|    2125|2015|
|            132.0|   93.0|   112.0|          112.0|   2312|      2120|      1820|        0|     AA|        19.0|        4|         1|   100.0|            100|   2000| ATL|         Atlanta, GA|       GA|   731.0|       0|2015-01-01|     1298|      1|             81.0|    1|    12.0|   DFW|Dallas/Fort Worth...|         TX|      1|          0.0| N003AA|   6.0|   33.0|         0.0|     2033|    2306|2015|
|            145.0|  111.0|    78.0|           78.0|   1043|      0925|      0800|        0|     AA|        78.0|        4|         1|    78.0|             78|   0918| HDN|          Hayden, CO|       CO|   769.0|       0|2015-01-01|     1422|      1|              0.0|    1|     0.0|   DFW|Dallas/Fort Worth...|         TX|      1|          0.0| N003AA|   4.0|   30.0|         0.0|     0948|    1039|2015|
|            139.0|  108.0|   336.0|          336.0|   1856|      1320|      1005|        0|     AA|       254.0|        4|         1|   332.0|            332|   1537| DFW|Dallas/Fort Worth...|       TX|   769.0|       0|2015-01-01|     1422|      1|             78.0|    1|     4.0|   HDN|          Hayden, CO|         CO|      1|          0.0| N003AA|  15.0|   16.0|         0.0|     1553|    1841|2015|
|            205.0|  146.0|    21.0|           21.0|   1221|      1200|      0800|        0|     AA|         0.0|        4|         1|    -4.0|              0|   0756| DFW|Dallas/Fort Worth...|       TX|  1047.0|       0|2015-01-01|     2287|      1|              0.0|    1|    21.0|   JAC|         Jackson, WY|         WY|      1|          0.0| N004AA|  10.0|   49.0|         0.0|     0845|    1211|2015|
|             null|   null|    null|           null|   null|      1755|      1415|        1|     AA|        null|        4|         1|    null|           null|   null| ORD|         Chicago, IL|       IL|  1007.0|       0|2015-01-01|     1080|      1|             null|    1|    null|   EGE|           Eagle, CO|         CO|      1|         null| N005AA|  null|   null|        null|     null|    null|2015|
|             null|   null|    null|           null|   null|      1335|      1145|        1|     AA|        null|        4|         1|    null|           null|   null| EGE|           Eagle, CO|       CO|  1007.0|       0|2015-01-01|     1080|      1|             null|    1|    null|   ORD|         Chicago, IL|         IL|      1|         null| N005AA|  null|   null|        null|     null|    null|2015|
|             null|   null|    null|           null|   null|      0955|      0740|        1|     AA|        null|        4|         1|    null|           null|   null| ORD|         Chicago, IL|       IL|   802.0|       0|2015-01-01|     2332|      1|             null|    1|    null|   DFW|Dallas/Fort Worth...|         TX|      1|         null| N005AA|  null|   null|        null|     null|    null|2015|
|             null|   null|    null|           null|   null|      1445|      1150|        1|     AA|        null|        4|         1|    null|           null|   null| ATL|         Atlanta, GA|       GA|   731.0|       0|2015-01-01|      194|      1|             null|    1|    null|   DFW|Dallas/Fort Worth...|         TX|      1|         null| N006AA|  null|   null|        null|     null|    null|2015|
|            151.0|  122.0|     1.0|            1.0|   1806|      1805|      1640|        0|     AA|        null|        4|         1|    -5.0|              0|   1635| DFW|Dallas/Fort Worth...|       TX|   731.0|       0|2015-01-01|      356|      1|             null|    1|    null|   ATL|         Atlanta, GA|         GA|      1|         null| N006AA|  14.0|   15.0|        null|     1650|    1752|2015|
|            113.0|   94.0|   -11.0|            0.0|   1549|      1600|      1300|        0|     AA|        null|        4|         1|    -4.0|              0|   1256| ATL|         Atlanta, GA|       GA|   731.0|       0|2015-01-01|      356|      1|             null|    1|    null|   DFW|Dallas/Fort Worth...|         TX|      1|         null| N006AA|   4.0|   15.0|        null|     1311|    1545|2015|
|            125.0|   91.0|    86.0|           86.0|   0016|      2250|      1955|        0|     AA|         0.0|        4|         1|    76.0|             76|   2111| ATL|         Atlanta, GA|       GA|   731.0|       0|2015-01-01|     2396|      1|             71.0|    1|    10.0|   DFW|Dallas/Fort Worth...|         TX|      1|          0.0| N007AA|   4.0|   30.0|         5.0|     2141|    0012|2015|
|            145.0|  115.0|    -7.0|            0.0|   1208|      1215|      1045|        0|     AA|        null|        4|         1|    -2.0|              0|   1043| DFW|Dallas/Fort Worth...|       TX|   731.0|       0|2015-01-01|     1513|      1|             null|    1|    null|   ATL|         Atlanta, GA|         GA|      1|         null| N008AA|  17.0|   13.0|        null|     1056|    1151|2015|
|            105.0|   89.0|   -25.0|            0.0|   0940|      1005|      0700|        0|     AA|        null|        4|         1|    -5.0|              0|   0655| ATL|         Atlanta, GA|       GA|   731.0|       0|2015-01-01|     1513|      1|             null|    1|    null|   DFW|Dallas/Fort Worth...|         TX|      1|         null| N008AA|   5.0|   11.0|        null|     0706|    0935|2015|
|            122.0|  106.0|    17.0|           17.0|   1737|      1720|      1600|        0|     AA|        17.0|        4|         1|    35.0|             35|   1635| EGE|           Eagle, CO|       CO|   721.0|       0|2015-01-01|      937|      1|              0.0|    1|     0.0|   DFW|Dallas/Fort Worth...|         TX|      1|          0.0| N009AA|   4.0|   12.0|         0.0|     1647|    1733|2015|
|            113.0|   94.0|   -12.0|            0.0|   1908|      1920|      1805|        0|     AA|        null|        4|         1|    10.0|             10|   1815| LAX|     Los Angeles, CA|       CA|   748.0|       0|2015-01-01|      937|      1|             null|    1|    null|   EGE|           Eagle, CO|         CO|      1|         null| N009AA|   9.0|   10.0|        null|     1825|    1859|2015|
|             null|   null|    null|           null|   null|      1440|      1145|        1|     AA|        null|        4|         1|    null|           null|   null| SDF|      Louisville, KY|       KY|   733.0|       0|2015-01-01|     1212|      1|             null|    1|    null|   DFW|Dallas/Fort Worth...|         TX|      1|         null| N010AA|  null|   null|        null|     null|    null|2015|
|             null|   null|    null|           null|   null|      1640|      1520|        1|     AA|        null|        4|         1|    null|           null|   null| DFW|Dallas/Fort Worth...|       TX|   733.0|       0|2015-01-01|     1212|      1|             null|    1|    null|   SDF|      Louisville, KY|         KY|      1|         null| N010AA|  null|   null|        null|     null|    null|2015|
+-----------------+-------+--------+---------------+-------+----------+----------+---------+-------+------------+---------+----------+--------+---------------+-------+----+--------------------+---------+--------+--------+----------+---------+-------+-----------------+-----+--------+------+--------------------+-----------+-------+-------------+-------+------+-------+------------+---------+--------+----+
only showing top 20 rows
'''

# Load the parquet file back
on_time_dataframe = spark.read.parquet('data/on_time_performance.parquet')
on_time_dataframe.show() 

'''
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
