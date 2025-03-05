from pyspark import SparkConf,SparkContext
import os
import json  #json转字典的时候需要import
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1") # 设置全局并行数默认为1
sc = SparkContext(conf = conf)

# 第三阶段13-输出到文件  ※hadoop的依赖配置

# 输出到文件（将rdd的数据写入到文本文件中）
rdd1 = sc.parallelize([1,2,3,4,5],numSlices=1) #当前rdd分区为1

rdd2 = sc.parallelize()

rdd1.saveAsTextFile("d:/output1") # saveAsTestFile是根据rdd的分区（可能十几个分区：根据cpu核心数）输出多少个文件
