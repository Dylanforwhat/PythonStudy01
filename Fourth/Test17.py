from pyspark import SparkConf,SparkContext
import os
import json  #json转字典的时候需要import
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1") # 设置全局并行数默认为1
sc = SparkContext(conf = conf)