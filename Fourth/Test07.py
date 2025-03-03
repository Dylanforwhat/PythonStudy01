# filter 过滤的意思  传入一个参数，类型不限制，返回布尔
# 返回true留下  false被抛弃
from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)

rdd = sc.parallelize([1,2,3,4,5])
rdd2 = rdd.filter(lambda num:num % 2 == 0)
print(rdd2.collect())