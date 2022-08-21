// spark-shell -i main.scala --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3

import org.apache.spark.sql.types.{StructType, StringType};

val df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe","my-topic").load()

val msg = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)").as[(String, String)]

val schema = new StructType().add("quote",StringType).add("author",StringType)

val msgDF = msg.select(from_json(col("value"), schema).as("data")).select("data.*")

msgDF.withColumn("word",explode(split(col("Quote"), " "))).groupBy("word").count().sort("word").writeStream.format("console").outputMode("complete").start().awaitTermination()