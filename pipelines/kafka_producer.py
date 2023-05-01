import json
import os
from typing import List

from confluent_kafka import Producer


class KafkaJsonProducer:

    def __init__(self, bootstrap_servers: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS")):
        self.producer = Producer({
            "bootstrap.servers": bootstrap_servers
        })

    def push(self, topic: str, messages: List):
        self.producer.poll(0)
        for msg in messages:
            json_message = json.dumps(msg.__dict__)
            self.producer.produce(topic, json_message.encode("utf-8"))
        self.producer.flush()


class KafkaAvroProducer:
    pass
