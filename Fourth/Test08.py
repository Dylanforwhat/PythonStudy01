from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)

# rdd.sortBy(func,ascending = False,numPartitions = 1)  false 降序

# 2、读取数文件
rdd = sc.textFile('d:/xx.txt')

# 3、取出全部单词,flatmap可以解嵌套
rdd1 = rdd.flatMap(lambda x:x.split(" "))

# 4、讲所有单词都转为二元元组，单词为key，value设置为1，map类似遍历所有元素应用新函数返回值
word_rdd = rdd1.map(lambda word:(word,1))

# 5、分组并求和， 用lambda函数，这里重新学一下lambda函数！！
result_rdd = word_rdd.reduceByKey(lambda a,b:a+b)

# 增加排序：
final_rdd = result_rdd.sortBy(lambda x:x[1],ascending=False,numPartitions=1)

# 6、打印结果
print(final_rdd.collect())