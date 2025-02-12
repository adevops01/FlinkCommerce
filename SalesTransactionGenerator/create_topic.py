from confluent_kafka.admin import AdminClient, NewTopic

# Configuration for the AdminClient
conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker address
}

# Create an AdminClient instance
admin_client = AdminClient(conf)

# Define the topic configuration
topic_name = "my_new_topic"
num_partitions = 3  # Number of partitions for the topic
replication_factor = 1  # Replication factor for the topic

# Create a NewTopic object
new_topic = NewTopic(
    topic=topic_name,
    num_partitions=num_partitions,
    replication_factor=replication_factor
)

# Create the topic
fs = admin_client.create_topics([new_topic])

# Wait for the topic creation to complete
for topic, future in fs.items():
    try:
        future.result()  # Wait for the topic to be created
        print(f"Topic '{topic}' created successfully!")
    except Exception as e:
        print(f"Failed to create topic '{topic}': {e}")