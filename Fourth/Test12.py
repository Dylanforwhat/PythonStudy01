# 数据分析本质上都是单词统计
#
from turtledemo.sorting_animate import partition

from pyspark import SparkConf,SparkContext
import os
import json  #json转字典的时候需要import
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1") # 设置全局并行数默认为1
sc = SparkContext(conf = conf)

file_rdd = sc.textFile("d:/xxx.txt") # 链式调用太长的是否可以用斜杠分行
result1 = file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x: x[0][:2]).\
    map(lambda x:(x,1)).\
    reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending = False,numParttions =1).\
    take(3)