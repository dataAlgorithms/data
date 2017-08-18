import org.apache.spark._
import SparkContext._
val sc1 = new SparkContext()

val config = new SparkConf().setMaster("spark://host:port").setAppName("big app")
val sc2 = new SparkContext(config)
