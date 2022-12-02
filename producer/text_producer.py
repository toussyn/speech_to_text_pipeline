from kafka import KafkaProducer
from json import dumps
import pandas as pd
import logging

logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)


def text_producer():
    producer = KafkaProducer(
    bootstrap_servers=['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092','b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'],
    client_id='g2-text-producer',value_serializer=lambda x: dumps(x).encode('utf-8'))
    data = pd.read_csv('/mnt/10ac-batch-6/notebooks/gedion_abebe/Amharic News Dataset.csv')
    random_text = data.sample(n=1)[["headline","category","article"]]
    random_text.reset_index(drop=True, inplace=True)
    if random_text['category'][0] == 'ሀገር አቀፍ ዜና':
        return producer.send("g2-national_news", value={"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()}).get(timeout=30)
    elif random_text['category'][0] == 'መዝናኛ':
        return producer.send("g2-entertainment", value={"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()}).get(timeout=30)
    elif random_text['category'][0] == 'ቢዝነስ':
        return producer.send("g2-business", value={"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()}).get(timeout=30)
    elif random_text['category'][0] == 'ዓለም አቀፍ ዜና':
        return producer.send("g2-international_news", value={"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()}).get(timeout=30)
    elif random_text['category'][0] == 'ፖለቲካ':
        return producer.send("g2-politics", value={"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()}).get(timeout=30)
    elif random_text['category'][0] == 'ስፖርት':
        return producer.send("g2-sport", value={"headline": random_text['headline'][0].strip(),"category":random_text['category'][0].strip(),"article":random_text['article'][0].strip()}).get(timeout=30)
    