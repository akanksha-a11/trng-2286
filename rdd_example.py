from pyspark import SparkContext

sc = SparkContext(appName="SimpleRDDJob")

data = [10, 20, 30, 40, 50]
rdd = sc.parallelize(data)

squared = rdd.map(lambda x: x * x)
result = squared.collect()

print("Squared values:", result)

sc.stop()