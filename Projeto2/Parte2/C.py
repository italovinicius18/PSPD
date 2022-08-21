import findspark
findspark.init()

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.1.3,org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3 pyspark-shell'

spark = SparkSession \
    .builder \
    .appName("Kafka") \
    .getOrCreate()

# Define schema of json
schema = StructType() \
        .add("quote", StringType(), True) \
        .add("author", StringType(), True) 

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", 'localhost:9092') \
    .option("subscribe", 'my-topic') \
    .load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    

df = df.withColumn("value",from_json(col("value"),schema)) \
    .select("value.*")

seconds = 3

query = df  \
    .withColumn('word', explode(split(col('quote'), ' ')))\
    .groupBy('word')\
    .count()\
    .filter((col("word").substr(1,1) == 'p') | (col("word").substr(1,1) == 'r') | (col("word").substr(1,1) == 's')) \
    .sort('count', ascending=False)\
    .writeStream  \
    .outputMode("complete")  \
    .format("console")  \
    .option("truncate", "False")  \
    .trigger(processingTime=f'{seconds} seconds')  \
    .start()
        
query.awaitTermination()