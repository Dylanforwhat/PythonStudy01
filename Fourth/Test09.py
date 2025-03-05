from pyspark import SparkConf,SparkContext
import os
import json  #json转字典需要
os.environ['PYSPARK_PYTHON'] = "D:/python/python3.12.6/python.exe" #配置python解释器的环境变量，供spark调用
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)
# 一、城市销售额排名
# 1、读取文件  《第三阶段11-练习案例2》
file_rdd = sc.textFile('d:/xxx.xlsx')

# 2、取出每一个JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x:x.split("|"))

# 3、JSON字符串变成字典，变成字典的目的是好取数，比如用areaName就可以取到城市名称
dict_rdd = json_str_rdd.map(lambda x:json.loads(x)) # map就是地图炮的意思，每个人都来一下，lambda就是个匿名函数，就当是个函数

# 4、取出城市何销售额数据，通过上一步的字典，再取出一个（areaName，money）的元组，这里注意money是字符串
city_with_money_rdd = dict_rdd.map(lambda x:(x['areaName'],int(x['money'])))

# 5、按照城市按销售额聚合  ※reduceByKey很神奇，默认上面的二元元组的第一个就是key，第二个为value
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a,b:a + b)

# 6、按销售额聚合结果并排序  “x:x[1]”的意思是按二元元组的下标为1的元素进行排序，就是money排序
result1_rdd = city_result_rdd.sortBy(lambda x:x[1],ascending=False,numPartitions=1)

print(result1_rdd.collect())

# 二、全部城市中有哪些商品类别在售卖(就是map再去重)

# 1、取出全部的商品类别  distinct()是链式操作
category_rdd = dict_rdd.map(lambda x:x['category']).distinct()
print(category_rdd.collect())

# 三、北京市有哪些商品类别在售卖（就是先filter再distinct）
beijing_data_rdd = dict_rdd.filter(lambda x:x['areaName'] == '北京')

beijing_category_rdd = beijing_data_rdd.map(lambda x:x['category']).distinct()

print(beijing_category_rdd.collect())