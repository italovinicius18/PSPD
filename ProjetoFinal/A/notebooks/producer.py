from kafka import KafkaProducer
from quoters import Quote
import json
import re
import time

producer = KafkaProducer(
        value_serializer=lambda m: json.dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092']
    )

def get_quote():
    return Quote().quote

def format_clean_quote(quote):
    quote = quote.replace('“', '')
    quote = quote.replace('”', '')

    try:
        if '—' in quote:
            quote, author = quote.split('—')
        elif '―':
            quote, author = quote.split('―')
        elif '–':
            quote, author = quote.split('–')
        
    except Exception as e:
        # quote, author = quote.split('―')
        quote = quote
        author = 'unknown'
    
    quote = quote.strip().lower()
    quote = re.sub(r'[^a-zA-Z0-9\s]', '', quote)
    author = author.strip().lower()

    return quote, author

# produce asynchronously
while True:
    quote = Quote().print()
    quote,author = format_clean_quote(quote)
    
    data = {'quote': quote.lower(), 'author': author.lower()}
    print(data)
    producer.send('frases', data)
    time.sleep(1)