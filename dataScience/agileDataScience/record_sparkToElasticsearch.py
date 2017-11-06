#!/usr/bin/env python

'''
1. create index for elasticsearch to search quickly
curl -XPUT 'http://localhost:9200/agile_data_science/' -d '{
    "settings" : {
        "index" : {
            "number_of_shards" : 1,
            "number_of_replicas" : 1
        }
    }
}'

2. drop the index
curl -XDELETE 'http://localhost:9200/agile_data_science/'

3. query
curl 'localhost:9200/agile_data_science/on_time_performance/search?q=Origin:ATL&pretty'
'''

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("pyspark to elasticsearch") \
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
