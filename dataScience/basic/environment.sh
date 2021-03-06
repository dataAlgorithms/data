'''
环境变量文件： /etc/profile或者~/.bashrc
'''

1. Java install
下载：(http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
jdk-8u141-linux-x64.rpm 

安装：
rpm -Uvh jdk-8u141-linux-x64.rpm 

环境变量： 
vi ~/.bashrc

# JAVA home
export JAVA_HOME=/usr/java/jdk1.8.0_141
export JAVA_HOME
export PATH=$JAVA_HOME/bin:$PATH
export PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export CLASSPATH

2. Anaconda install
下载：(http://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh)
安装：
Anaconda3-4.2.0-Linux-x86_64.sh" -b -p root/anaconda
环境变量：
export PATH="/root/anaconda3/bin:$PATH"

3. Hadoop install
下载：
  curl -Lko hadoop-2.7.3.tar.gz http://apache.osuosl.org/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
解压：
  tar -xvf /tmp/hadoop-2.7.3.tar.gz -C hadoop --strip-components=1
环境变量：
  export PROJECT_HOME=/root/workspace
  export HADOOP_HOME=$PROJECT_HOME/hadoop
  export PATH=$PATH:$HADOOP_HOME/bin
  export HADOOP_CLASSPATH=$(hadoop classpath)
  export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

4. Spark install
下载：
  curl -Lko /tmp/spark-2.1.0-bin-without-hadoop.tgz http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-without-hadoop.tgz
解压：
  tar -zxvf spark-2.1.0-bin-without-hadoop.tgz
  mv spark-2.1.0-bin-without-hadoop spark
环境变量：
export SPARK_HOME=$PROJECT_HOME/spark
export HADOOP_CONF_DIR=$PROJECT_HOME/hadoop/etc/hadoop/
export SPARK_DIST_CLASSPATH=`$HADOOP_HOME/bin/hadoop classpath`
export PATH=$PATH:$SPARK_HOME/bin
配置：
 # Have to set spark.io.compression.codec in Spark local mode
  cp spark/conf/spark-defaults.conf.template spark/conf/spark-defaults.conf
  echo 'spark.io.compression.codec org.apache.spark.io.SnappyCompressionCodec' >> spark/conf/spark-defaults.conf

  # Give Spark 8GB of RAM
  echo "spark.driver.memory 8g" >> $SPARK_HOME/conf/spark-defaults.conf

  echo "PYSPARK_PYTHON=python3" >> $SPARK_HOME/conf/spark-env.sh
  echo "PYSPARK_DRIVER_PYTHON=python3" >> $SPARK_HOME/conf/spark-env.sh

  # Setup log4j config to reduce logging output
  cp $SPARK_HOME/conf/log4j.properties.template $SPARK_HOME/conf/log4j.properties
  sed -i 's/INFO/ERROR/g' $SPARK_HOME/conf/log4j.properties

5. Mongodb install
下载：
  curl -Lko mongodb-linux-x86_64-amazon-3.4.1.tgz https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-amazon-3.4.2.tgz
解压：
  tar -zxvf mongodb-linux-x86_64-amazon-3.4.1.tgz
  mv mongodb-linux-x86_64-amazon-3.4.1 mongodb
启动：
mkdir -p mongodb/data/db
mongodb/bin/mongod --dbpath mongodb/data/db &
包：
mkdir lib
curl -Lko lib/mongo-java-driver-3.4.0.jar http://central.maven.org/maven2/org/mongodb/mongo-java-driver/3.4.0/mongo-java-driver-3.4.0.jar
curl -Lko mongo-hadoop-r2.0.2.tar.gz https://github.com/mongodb/mongo-hadoop/archive/r2.0.2.tar.gz
tar -zxvf mongo-hadoop-r1.5.2.tar.gz 
mv mongo-hadoop-r1.5.2 mongo-hadoop
cd mongo-hadoop
./gradlew jar
cd ..
cp mongo-hadoop/spark/build/libs/mongo-hadoop-spark-*.jar lib/
cp mongo-hadoop/build/libs/mongo-hadoop-*.jar lib/
cd mongo-hadoop/spark/src/main/python
python setup.py install
cd $PROJECT_HOME# to $PROJECT_HOME
cp mongo-hadoop/spark/src/main/python/pymongo_spark.py lib/
export PYTHONPATH=$PYTHONPATH:$PROJECT_HOME/lib
echo 'export PYTHONPATH=$PYTHONPATH:$PROJECT_HOME/lib' >> ~/.bash_profile

异常处理说明：
gradlew jar执行不了

解决办法：
So, I changed distributionUrl property in gradle-wrapper.properties(mongo-hadoop/gradle/wrapper/gradle-wrapper.properties) to

distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=gradle-1.11-bin.zip
Then, I made a copy of gradle-1.11-bin.zip in gradle/wrapper/.

参考：
https://stackoverflow.com/questions/22896569/how-to-use-gradle-zip-in-local-system-without-downloading-when-using-gradle-wrap

6. elasticsearch
下载：
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.5/elasticsearch-2.3.5.tar.gz
解压：
tar -zxvf elasticsearch-2.3.5.tar.gz
mv elasticsearch-2.3.5 elasticsearch
启动：
elasticsearch/bin/elasticsearch -Des.insecure.allow.root=true

异常处理说明：
Exception in thread "main" java.lang.RuntimeException: don't run elasticsearch as root.
方法A: 
elasticsearch/bin/elasticsearch -Des.insecure.allow.root=true
方法B：
https://my.oschina.net/topeagle/blog/591451

7. elaticsearch hadoop
# Install Elasticsearch for Hadoop
echo "Installing elasticsearch-hadoop to $PROJECT_HOME/elasticsearch-hadoop ..."
curl -Lko /tmp/elasticsearch-hadoop-5.0.0-alpha5.zip http://download.elastic.co/hadoop/elasticsearch-hadoop-5.0.0-alpha5.zip
unzip /tmp/elasticsearch-hadoop-5.0.0-alpha5.zip
mv elasticsearch-hadoop-5.0.0-alpha5 elasticsearch-hadoop
cp elasticsearch-hadoop/dist/elasticsearch-hadoop-5.0.0-alpha5.jar lib/
cp elasticsearch-hadoop/dist/elasticsearch-spark-20_2.10-5.0.0-alpha5.jar lib/
echo "spark.speculation false" >> $PROJECT_HOME/spark/conf/spark-defaults.conf

8. spark jars
# Install and add snappy-java and lzo-java to our classpath below via spark.jars
echo "Installing snappy-java and lzo-hadoop to $PROJECT_HOME/lib ..."
curl -Lko lib/snappy-java-1.1.2.6.jar http://central.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.2.6/snappy-java-1.1.2.6.jar
curl -Lko lib/lzo-hadoop-1.0.5.jar http://central.maven.org/maven2/org/anarres/lzo/lzo-hadoop/1.0.0/lzo-hadoop-1.0.0.jar

# Setup mongo and elasticsearch jars for Spark
echo "spark.jars $PROJECT_HOME/lib/mongo-hadoop-spark-1.5.2.jar,\
$PROJECT_HOME/lib/mongo-java-driver-3.4.0.jar,\
$PROJECT_HOME/lib/mongo-hadoop-1.5.2.jar,\
$PROJECT_HOME/lib/elasticsearch-spark-20_2.10-5.0.0-alpha5.jar,\
$PROJECT_HOME/lib/snappy-java-1.1.2.6.jar,\
$PROJECT_HOME/lib/lzo-hadoop-1.0.5.jar" \
  >> spark/conf/spark-defaults.conf

# Setup spark classpath for snappy for parquet... required for OS X 10.11, others can skip
echo "SPARK_CLASSPATH=$PROJECT_HOME/lib/snappy-java-1.1.2.6.jar" >> spark/conf/spark-env.sh

9. zeppelin
# Install Apache Zeppelin
curl -Lko /tmp/zeppelin-0.6.2-bin-all.tgz \
http://www-us.apache.org/dist/zeppelin/zeppelin-0.6.2/ \
zeppelin-0.6.2-bin-all.tgz
mkdir zeppelin
tar -xvzf /tmp/zeppelin-0.6.2-bin-all.tgz -C zeppelin --strip-components=1
# Configure Zeppelin
cp zeppelin/conf/zeppelin-env.sh.template zeppelin/conf/zeppelin-env.sh
echo "export SPARK_HOME=$PROJECT_HOME/spark" >> zeppelin/conf/zeppelin-env.sh
echo "export SPARK_MASTER=local" >> zeppelin/conf/zeppelin-env.sh
echo "export SPARK_CLASSPATH=" >> zeppelin/conf/zeppelin-env.sh
To start Zeppelin, run zeppelin/bin/zeppelin-daemon.sh start and then visit
http://localhost:8080 to check out the user interface. 

10. airflow
 pip install airflow
  mkdir ~/airflow
  mkdir ~/airflow/dags
  mkdir ~/airflow/logs
  mkdir ~/airflow/plugins
  airflow initdb
  airflow webserver -D

11. vi ~/.bash_profile
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

# project
export PROJECT_HOME=/root/workspace

# python
export PATH="$HOME/anaconda/bin:$PATH"
export PYTHONPATH=$PYTHONPATH:$PROJECT_HOME/lib

# scala
export SCALA_HOME=/usr/local/scala
export PATH=$PATH:${SCALA_HOME}/bin

# java hadoop spark
export JAVA_HOME=/usr/java/jdk1.8.0_141

export HADOOP_HOME=$PROJECT_HOME/hadoop
export HADOOP_CLASSPATH=$(/root/workspace/hadoop/bin/hadoop classpath)
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native

export SPARK_HOME=$PROJECT_HOME/spark
export SPARK_DIST_CLASSPATH=`$HADOOP_HOME/bin/hadoop classpath`

export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH

export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:${SPARK_HOME}/bin:$PATH

12. spark env
PYSPARK_PYTHON=python3
PYSPARK_DRIVER_PYTHON=python3
SPARK_CLASSPATH=/root/workspace/lib/snappy-java-1.1.2.6.jar
export SPARK_DIST_CLASSPATH=$(hadoop classpath)
