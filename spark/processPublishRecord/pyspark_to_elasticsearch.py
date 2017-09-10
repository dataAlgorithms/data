#!/usr/bin/env python

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Load the Parquet file
on_time_dataframe = spark.read.parquet('data/on_time_performance.parquet')

# Sava the DataFrame to Elasticsearch
on_time_dataframe.write.format("org.elasticsearch.spark.sql")\
.option("es.resource","agile_data_science/on_time_performance")\
.option("es.batch.size.entries","100")\
.mode("overwrite")\
.save()
