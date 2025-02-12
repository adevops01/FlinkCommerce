from confluent_kafka.admin import AdminClient

# Configuration for the AdminClient
conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker address
}

# Create an AdminClient instance
admin_client = AdminClient(conf)

# List all topics
metadata = admin_client.list_topics(timeout=10)

# Get the list of topics
topics = metadata.topics

# Print the topics
for topic_name, topic_info in topics.items():
    print(f"Topic: {topic_name}")

# Alternatively, you can get the topic names as a list
topic_names = list(topics.keys())
print("Topic Names:", topic_names)