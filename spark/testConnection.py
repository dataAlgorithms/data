import os
import sys
 
# Path for spark source folder
os.environ['SPARK_HOME']="D:\Spark"
 
# Append pyspark  to Python Path
sys.path.append("D:\Spark\python")
sys.path.append("D:\Spark\python\lib\py4j-0.10.3-src.zip")
 
try:
    from pyspark import SparkContext
    from pyspark import SparkConf
 
    print ("Successfully imported Spark Modules")
 
except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)
