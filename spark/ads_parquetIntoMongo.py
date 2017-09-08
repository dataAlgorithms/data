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

on_time_dataframe = spark.read.parquet('data/on_time_performance.parquet')

as_dict = on_time_dataframe.rdd.map(lambda row: row.asDict())
as_dict.saveToMongoDB('mongodb://localhost:27017/agile_data_science.on_time_performance')

'''
If something goes wrong, you can drop the collection and try again

mongo agile_data_science
db.on_time_performance.drop()

db.on_time_performance.findOne()

if query is slow, try do the follow command.

db.on_time_performance.ensureIndex({Carrier: 1, FlightDate: 1, FlightNum: 1})
'''
