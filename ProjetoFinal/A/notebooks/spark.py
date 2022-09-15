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
    .option("subscribe", 'frases') \
    .load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    

df = df.withColumn("value",from_json(col("value"),schema)) \
    .select("value.*")

# seconds = 3

# query = df  \
#     .withColumn('word', explode(split(col('quote'), ' ')))\
#     .groupBy('word')\
#     .count()\
#     .sort('count', ascending=False)\
#     .writeStream  \
#     .outputMode("complete")  \
#     .format("console")  \
#     .option("truncate", "False")  \
#     .trigger(processingTime=f'{seconds} seconds')  \
#     .start() 

query = df  \
    .withColumn('word', explode(split(col('quote'), ' ')))\
    .groupBy('word')\
    .count()\

# Write query on kafka

query = query.selectExpr("CAST(word AS STRING) as key", "to_json(struct(*)) AS value") \
    .writeStream \
    .outputMode("complete") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", 'localhost:9092') \
    .option("topic", 'frases-tratadas') \
    .option("checkpointLocation", 'checkpoint') \
    .start()

query.awaitTermination()