import os
import sys
 
def testConnection():
    
    # Path for spark source folder
    os.environ['SPARK_HOME']="D:\Spark"
 
    # Append pyspark  to Python Path
    sys.path.append("D:\Spark\python")
    sys.path.append("D:\Spark\python\lib\py4j-0.10.3-src.zip")
 
    try:
        from pyspark import SparkContext
        from pyspark import SparkConf 
 
        print ("Successfully imported Spark Modules")
 
        sc = SparkContext(appName="TestApp")
        lines = sc.textFile("d:\Spark\War_and_Peace.txt")
        print lines.count()
        print lines.first()
        
        return 0
    
    except ImportError as e:
        print ("Can not import Spark Modules", e)
        return 1
    
if __name__ == "__main__":
    retCode = testConnection()
    print 'retCode:', retCode
