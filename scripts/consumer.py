import os
import json
from kafka import KafkaConsumer, KafkaProducer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "g2-topics-test",
        bootstrap_servers=[
            'b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'
        ],
        value_deserializer=lambda value: json.loads(value),
    )
    # producer = KafkaProducer(
    #     bootstrap_servers=KAFKA_BROKER_URL,
    #     value_serializer=lambda value: json.dumps(value).encode(),
    # )
    for message in consumer:
        transaction: dict = message.value
        topic = "g2-topics-test"
        # producer.send(topic, value=transaction)
        print(topic, transaction)