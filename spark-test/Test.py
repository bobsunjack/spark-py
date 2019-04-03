from pyspark import *

import os
print(os.environ['SPARK_HOME'])
print(os.environ['HADOOP_HOME'])
if __name__ == '__main__':
    conf = SparkConf().setAppName("sss")
    conf = conf.setMaster("local[*]")
    sc = SparkContext(conf=conf)
    rdd = sc.parallelize("hello Pyspark world".split(" "))
    counts = rdd \
        .flatMap(lambda line: line) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .foreach(print)
    sc.stop