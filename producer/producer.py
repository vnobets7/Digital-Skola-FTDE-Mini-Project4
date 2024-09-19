#!python3

import json
import time
import kafka
import pandas as pd

from kafka import KafkaProducer

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

if __name__ == "__main__":
    data = pd.read_csv('New_Information.csv')
    json_data = data.to_dict(orient='records')
    
    producer = KafkaProducer(bootstrap_servers=['localhost:9093'],api_version=(0,11,5),value_serializer=json_serializer)
    while True:
        for data in json_data:
            print(data)
            producer.send("ftde02-project4", data)
            time.sleep(10)