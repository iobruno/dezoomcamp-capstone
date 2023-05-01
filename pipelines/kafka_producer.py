import json
from abc import ABC, abstractmethod
from typing import List, Union

from confluent_kafka import Producer


class KafkaSerializable(ABC):
    @abstractmethod
    def message_key(self) -> Union[str, None]:
        pass


class KafkaJsonProducer:

    def __init__(self, bootstrap_servers: str):
        self.producer = Producer({
            "bootstrap.servers": bootstrap_servers
        })

    def push(self, topic: str, messages: List[KafkaSerializable]):
        self.producer.poll(0)
        for msg in messages:
            json_message = json.dumps(msg.__dict__)
            self.producer.produce(topic,
                                  value=json_message.encode("utf-8"),
                                  key=msg.message_key())
        self.producer.flush()


class KafkaAvroProducer:
    pass

