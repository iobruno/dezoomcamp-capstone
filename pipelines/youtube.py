from dataclasses import dataclass
from typing import List


@dataclass
class VideoCategory:
    id: str
    title: str


@dataclass
class Video:
    id: str
    title: str
    category_id: str
    published_at: str
    topics: List[str]
