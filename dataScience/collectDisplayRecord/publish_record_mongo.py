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
#if something goes wrong, drop the collection

mongo agile_data_science
> db.on_time_performance.drop()

#do the above program, then query

> db.on_time_performance.findOne()
or
> db.on_time_performance.findOne(
{Carrier: 'DL', FlightDate: '2015-01-01', FlightNum: 478}) 

# maintain indexes for query to make query return quickly
> db.on_time_performance.ensureIndex({Carrier: 1, FlightDate: 1, FlightNum: 1})
'''
