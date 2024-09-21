from kafka import KafkaConsumer
import json

# Initialize the Kafka consumer
# - 'test_topic' is the topic to subscribe to
# - 'bootstrap_servers' defines the Kafka server(s) to connect to
# - 'auto_offset_reset' controls where to start reading (earliest or latest)
# - 'enable_auto_commit' automatically commits the offset after consuming
# - 'value_deserializer' converts the received bytes into a Python dictionary using JSON
consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # Start reading from the beginning of the topic if no offset is stored
    enable_auto_commit=True,       # Automatically commit the message offset after it's read
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize JSON messages
)

# Function to consume messages from the topic
def consume_message():
    print("Starting consumer...")
    # Infinite loop to read and print messages from the topic
    for message in consumer:
        print(f"Received: {message.value}")  # Print the message value (deserialized JSON)

if __name__ == '__main__':
    consume_message()  # Start consuming messages
