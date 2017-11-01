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

