from kafka import KafkaAdminClient 
from kafka.admin import NewTopic
from kafka_init import *


def create_topics():
    client = KafkaAdminClient(
            bootstrap_servers = ['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092','b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'],
            api_version=(0,11,5),
        )
    
    topic_list = ['g2-national_news','g2-sport','g2-politics','g2-international_news','g2-business','g2-entertainment']
    total = []
    for t in topic_list:
        total.append(NewTopic(name=t,num_partitions=3,replication_factor=1))
    client.create_topics(new_topics=total,validate_only=False)

# create_topics()    
read_topics()
