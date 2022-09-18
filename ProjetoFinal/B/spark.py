import findspark
findspark.init()

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

from LeIA.leia import SentimentIntensityAnalyzer 

s = SentimentIntensityAnalyzer()

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.1.3,org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3 pyspark-shell'

spark = SparkSession \
    .builder \
    .appName("Kafka-politicos") \
    .getOrCreate()

# Define schema of json
schema = StructType() \
        .add("message", StringType(), True) \
        .add('politician', StringType(), True) \
        .add('id', IntegerType(), True)

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", 'localhost:9092') \
    .option("subscribe", 'mensagens') \
    .option("startingOffsets", "earliest") \
    .option("failOnDataLoss", "false") \
    .load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    

df = df.withColumn("value",from_json(col("value"),schema)) \
    .select("value.*")

# Apply sentiment analysis on each batch of dataframe

def sentiment_analysis_pos(str):
    return s.polarity_scores(str).get('pos')

def sentiment_analysis_neg(str):
    return s.polarity_scores(str).get('neg')

def sentiment_analysis_compound(str):
    return s.polarity_scores(str).get('compound')

def sentiment_analysis(str):
    compound = s.polarity_scores(str).get('compound')
    if compound > 0.05:
        return 'positive'
    elif compound < -0.05:
        return 'negative'
    else:
        return 'neutral'

sentiment_analysis_udf_pos = udf(sentiment_analysis_pos, StringType())

sentiment_analysis_udf_neg = udf(sentiment_analysis_neg, StringType())

sentiment_analysis_udf_compound = udf(sentiment_analysis_compound, StringType())

sentiment_analysis_udf = udf(sentiment_analysis, StringType())

df = df.withColumn("sentiment_pos", sentiment_analysis_udf_pos(df.message))

df = df.withColumn("sentiment_neg", sentiment_analysis_udf_neg(df.message))

df = df.withColumn("sentiment_compound", sentiment_analysis_udf_compound(df.message))

df = df.withColumn("sentiment", sentiment_analysis_udf(df.message))

# query = df \
#     .writeStream  \
#     .outputMode("update")  \
#     .format("console")  \
#     .option("truncate", "False")  \
#     .start() 

# Write query on kafka

query = df.selectExpr("CAST(id AS STRING) as key", "to_json(struct(*)) AS value") \
    .writeStream \
    .outputMode("update") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", 'localhost:9092') \
    .option("topic", 'mensagens-tratadas') \
    .option("truncate", "False") \
    .option("checkpointLocation", 'checkpointPoliticos') \
    .start()

query.awaitTermination()