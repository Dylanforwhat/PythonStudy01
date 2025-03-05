# 数据输出
# rdd.collect()  reduce()  take()  count()等等 输出的时候不再是rdd形式,数据计算还是rdd形式

from pyspark import SparkConf,SparkContext
import os
import json  #json转字典的时候需要import
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)

# 准备rdd
rdd = sc.parallelize([1,2,3,4,5,6])

# collect算子，输出rdd为list对象（rdd无法直接print）
rdd_list:list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子，与reduceByKey不同，不分组,reduce之后就不是rdd了，而是具体数字
num = rdd.reduce(lambda a,b:a + b)
print(num)

# take算子，就是取数
take_list = rdd.take(3)

# count算子，返回具体数字
countnum = rdd.count()

