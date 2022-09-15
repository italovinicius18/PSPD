from kafka import KafkaConsumer
import json
import sys

if len(sys.argv) != 2:
    print('Usage python3 consumer.py <topic>')
    exit()
else:
    topic = sys.argv[1]


consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

for message in consumer:

    print(message.value)