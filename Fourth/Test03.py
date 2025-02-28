from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)

rdd = sc.parallelize(["itheima itcast 666","itheima itheima itcast"])

rdd2 = rdd.flatMap(lambda x:x.split(" ")) #flatMap 就是解除嵌套的意思
print(rdd2.collect())