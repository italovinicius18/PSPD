from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json
import sys
from datetime import datetime

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

consumer = KafkaConsumer(
        'mensagens-tratadas',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

for message in consumer:
    # Add timestamp
    message.value['timestamp'] = datetime.now()
    resp = es.index(index="politics", document=message.value)
    print(resp)