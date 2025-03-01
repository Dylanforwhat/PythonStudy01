from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)

# reduceByKey 方法
# 针对KV型RDD，自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据的聚合操作
# kv就是二元元组  只有两个元素的元组
# rdd.reduceByKey(func)
#  func:(K,V) → V  接受2个传入参数，类型一致，返回一个返回值

rdd = sc.parallelize([('a',1),('a',1),('b',1),('b',1),('b',1)])
result = rdd.reduceByKey(lambda a,b:a-b)
print(result.collect())