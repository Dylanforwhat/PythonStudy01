from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf = conf)

rdd1 = sc.parallelize([1,2,3,4,5,6])
rdd2 = sc.parallelize({1, 2, 3, 4, 5, 6})


print(rdd1.collect())
# sc.stop()