# Kafka

$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties

$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties

# Hadoop

sudo service ssh restart
ssh localhost
$HADOOP_HOME/sbin/start-all.sh

# Spark

$SPARK_HOME/sbin/start-all.sh

# ELK

sudo service elasticsearch start

sudo service kibana start