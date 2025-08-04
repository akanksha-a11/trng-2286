# Apache Spark

an opensource, distributed processing framework designed for large-scale data processing and analytics.


#### Spark Cluster

![spark cluster](./images/spark-cluster-overview.png)


##### Driver Program

- It creates SparkContext, defines RDDs, and submits tasks.
- It is responsible for:

    - Defining the job logic (transformations & actions).
    - Creating the Directed Acyclic Graph (DAG) of execution stages.
    - Communicating with the Cluster Manager to request resources.
    - Distributing tasks to executors and tracking execution.

- Coordinates everything.

##### Cluster Manager

Allocates resources (CPU & memory) across applications.

**Spark supports:**

- Standalone (built-in)
- YARN (Hadoop)
- Mesos
- Kubernetes

##### Worker Nodes

- Machines in the cluster managed by the Cluster Manager.
- Each worker runs executors to process tasks.


##### Executor

- A JVM process launched on each worker.

**Responsible for:**

- Running tasks
- Storing RDD partitions in memory (cache)
- Reporting back to the driver


##### Tasks

- The smallest unit of work in Spark.
- A job is split into stages, and each stage is made of tasks.
- Each task is run by an executor on a partition of data.


##### Cache/Storage (RDD Caching)

- RDDs can be cached in memory (or disk) using .cache() or .persist().
- Useful for reusing the same data across multiple actions (e.g. multiple .collect() or .count() calls).

#### Spark and Pyspark installation

[wsl installation](https://learn.microsoft.com/en-us/windows/wsl/install)

##### Python installation in gitpod

```sh
sudo apt-get update && sudo apt-get install -y python3 python3-pip
```

#### Java Installation and path setup

```sh
# install java 17
sudo apt update
sudo apt install openjdk-17-jdk -y

# verify installation
java -version

# get java path
readlink -f $(which java)

/usr/lib/jvm/java-17-openjdk-amd64/bin/java

# add java path

echo 'export JAVA_HOME=/path/to/java' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc

# apply changes
source ~/.bashrc

```

```sh
# download spark

wget https://dlcdn.apache.org/spark/spark-4.0.0/spark-4.0.0-bin-hadoop3.tgz


# tar command
tar xvf spark-4.0.0-bin-hadoop3.tgz

# change path
sudo mv spark-4.0.0-bin-hadoop3.tgz /opt/spark

# verify installation
/opt/spark/bin/spark-shell --version

# set environmental variables

echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.bashrc
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.bashrc

# apply changes

source ~/.bashrc

```

[spark on ubuntu](https://phoenixnap.com/kb/install-spark-on-ubuntu)

[apache spark download](https://spark.apache.org/downloads.html)

[pyspark installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)


### RDDs, DataFrames and Datasets

#### Resilient Distributed Dataset (RDD)

- immutable distributed collection of elements of data, partitioned across nodes that can be operated in parallel with a low level API.
- offers transformations and actions

##### When to use RDDs?


- You need fine-grained, low-level transformations and actions on your data.
- Your data is unstructured (e.g., media streams, text streams).
- You prefer functional programming constructs over domain-specific expressions.
- You don't require schema enforcement or column-based data access.
- You're willing to trade off some performance and optimization benefits available in DataFrames/Datasets.
