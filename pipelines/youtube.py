from dataclasses import dataclass
from typing import List, Union

from kafka_producer import KafkaSerializable


@dataclass
class VideoCategory(KafkaSerializable):
    id: str
    title: str

    def message_key(self) -> Union[str, None]:
        return None


@dataclass
class Video(KafkaSerializable):
    id: str
    title: str
    category_id: str
    published_at: str
    topics: List[str]
    region: str

    def message_key(self) -> Union[str, None]:
        return self.region
