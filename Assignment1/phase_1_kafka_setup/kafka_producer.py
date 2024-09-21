from kafka import KafkaProducer
import json
import time

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to send messages to the Kafka topic
def send_message():
    for i in range(10):
        message = {'number': i, 'message': f"Message {i}"}
        producer.send('test_topic', message)  # Send the message to the topic
        print(f"Sent: {message}")
        time.sleep(1)  # Pause for 1 second between messages

if __name__ == '__main__':
    send_message()

    # Flush ensures all buffered messages are sent to Kafka before continuing
    producer.flush()

    # Close the producer to free resources, ensures flush is called
    producer.close()
