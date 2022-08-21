from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .appName("PythonStreamingKafkaWordCount") \
    .getOrCreate()

# Subscribe to 1 topic
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "my-topic") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

spark.stop()