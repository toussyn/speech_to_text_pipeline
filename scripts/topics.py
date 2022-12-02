from kafka import KafkaAdminClient 

client = KafkaAdminClient(
    bootstrap_servers = ['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092','b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'],
    api_version=(0,11,5),
)
topics_list = client.list_topics()
g2_topics_list = []
for i in topics_list:
    if 'g2' in i:
        g2_topics_list.append(i)

print(g2_topics_list)