from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)

rdd1 = sc.parallelize([1,2,3,4,5])
# map方法 逐条处理
def func1(data):
    data = data*10
    return data
rdd2 = rdd1.map(func1)  #（T） - U  一个能够接收同时返回值的函数
print(rdd2.collect())