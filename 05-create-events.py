# producer.py
import boto3
import json
import time
import random
from dotenv import load_dotenv
import os
from datetime import datetime, timezone

load_dotenv()

stream_name = "demo-spark-streaming-events"

client = boto3.client(
    "kinesis", 
    region_name="us-east-1",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),           
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY") 
    )  


def generate_data():
    return {
        "id": random.randint(1, 1000),
        "event": random.choice(["click", "view", "purchase"]),
        "value": round(random.uniform(10.0, 100.0), 2),
        "event_time": datetime.utcnow().isoformat()  # Add this line
    }


while True:
    record = json.dumps(generate_data())
    print(f"Sending: {record}")
    response = client.put_record(
        StreamName=stream_name,
        Data=record,
        PartitionKey="partitionKey"
    )
    time.sleep(1)  # Send 1 record per second
