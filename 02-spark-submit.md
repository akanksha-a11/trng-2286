# Spark Cluster 

#### Spark Submit

`spark-submit` is the command-line tool used to submit Spark applications to a cluster. It accepts various flags to configure how and where your application will run.

#### Cluster Manager

The cluster manager handles resource allocation and job scheduling. Spark supports several types of cluster managers:

| Value                    | Cluster Manager Type    |
| ------------------------ | ----------------------- |
| `local[*]` or `local[2]` | Local mode (no cluster) |
| `spark://host:7077`      | Standalone cluster      |
| `yarn`                   | Hadoop YARN             |
| `k8s://...`              | Kubernetes              |
| `mesos://...`            | Apache Mesos            |

#####  Cluster Mode and client mode

| Deploy Mode | Driver Runs On         |
| ----------- | ---------------------- |
| `client`    | Your local machine     |
| `cluster`   | Inside the worker node |

<i><b>note:</b> For Python apps in Standalone, always use --deploy-mode client. </i>

#### Driver configuration

Controls resources for the driver program:

1. --driver-memory 1g

2. --driver-cores 1

#### Executors configeration

You can configure how many resources each executor (worker process) gets:

1. --executor-memory 2g - Memory per executor

2. --executor-cores 2 - CPU cores per executor

3. --num-executors 3  - Number of executors (optional in standalone)


### Starting the Standalone Cluster

```sh
$SPARK_HOME/sbin/start-master.sh
$SPARK_HOME/sbin/start-worker.sh spark://<hostname>:7077
```

rdd_example.py code

```py
from pyspark import SparkContext

sc = SparkContext(appName="SimpleRDDJob")

data = [10, 20, 30, 40, 50]
rdd = sc.parallelize(data)

squared = rdd.map(lambda x: x * x)
result = rdd.collect()

print("Squared values:", result)

sc.stop()

```
#### Submitting a Spark Job

```
spark-submit \
  --master spark://<hostname>:7077 \
  --deploy-mode client \
  --name SimpleRDDJob \
  --executor-memory 1g \
  --executor-cores 1 \
  rdd_example.py
```


**reference:**

- [submitting spark applicarions](https://spark.apache.org/docs/latest/submitting-applications.html)