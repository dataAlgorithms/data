#!/usr/bin/env python

'''
1. Data source: parquet
'''
import pymongo
import pymongo_spark
pymongo_spark.activate()

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

on_time_dataframe = spark.read.parquet('data/on_time_performance.parquet')

as_dict = on_time_dataframe.rdd.map(lambda row: row.asDict())
as_dict.saveToMongoDB('mongodb://localhost:27017/agile_data_science.on_time_performance')

'''
2. Data source: csv
'''
import pymongo_spark
# Important: activate pymongo_spark
pymongo_spark.activate()
csv_lines = sc.textFile("data/example.csv")
data = csv_lines.map(lambda line: line.split(","))
schema_data = data.map(
    lambda x: {'name': x[0], 'company': x[1], 'title': x[2]}
)
schema_data.saveToMongoDB(
    'mongodb://localhost:27017/agile_data_science.executives'
)
