#!/usr/bin/env python

'''
1. Data source: csv

[root@localhost data]# cat example.csv 
Russell Jurney,Relato,CEO
Florian Liebert,Mesosphere,CEO
Don Brown,Rocana,CIO
Steve Jobs,Apple,CEO
Donald Trump,The Trump Organization,CEO
Russell Jurney,Data Syndrome,Principal Consultant
'''
import pymongo_spark
pymongo_spark.activate()

from pyspark import SparkContext
from pyspark import SparkConf 
 
print ("Successfully imported Spark Modules")
sc = SparkContext(appName="TestApp")

csv_lines = sc.textFile("data/example.csv")
data = csv_lines.map(lambda line: line.split(","))
schema_data = data.map(lambda x: ('key', {'name': x[0], 'company': x[1], 'title': x[2]}))

schema_data.saveAsNewAPIHadoopFile(
  path='-', 
  outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
  keyClass="org.apache.hadoop.io.NullWritable", 
  valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable", 
  conf={ "es.resource" : "agile_data_science/executives" })
  
'''
query:
  curl 'localhost:9200/agile_data_science/executives/_search?q=name:Russell*&pretty
'''

Use Python to query:

from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://localhost:9200/')
es.search('name:Russell', index='agile_data_science')


'''
2. Data source: parquet
'''
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
