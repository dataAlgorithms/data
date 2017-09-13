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
