from confluent_kafka.admin import AdminClient

# Configuration for the AdminClient
conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker address
}

# Create an AdminClient instance
admin_client = AdminClient(conf)

# Specify the topic name you want to describe
topic_name = "financial_transactions"  # Replace with your topic name

# Fetch metadata for the topic
metadata = admin_client.list_topics(timeout=10)

# Check if the topic exists
if topic_name not in metadata.topics:
    print(f"Topic '{topic_name}' does not exist.")
else:
    # Get the topic metadata
    topic_metadata = metadata.topics[topic_name]

    # Print general topic information
    print(f"Topic: {topic_name}")
    print(f"Partitions: {len(topic_metadata.partitions)}")
    print(f"Replication Factor: {len(topic_metadata.partitions[0].replicas)}")  # Assumes all partitions have the same replication factor

    # Print details for each partition
    print("\nPartition Details:")
    for partition_id, partition_metadata in topic_metadata.partitions.items():
        print(f"  Partition ID: {partition_id}")
        print(f"    Leader: {partition_metadata.leader}")
        print(f"    Replicas: {partition_metadata.replicas}")
        print(f"    ISR (In-Sync Replicas): {partition_metadata.isrs}")