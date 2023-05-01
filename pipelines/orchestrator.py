import os

from pipelines.kafka_producer import KafkaJsonProducer
from pipelines.youtube_api import YoutubeAPI

api_key = os.getenv("YOUTUBE_API_KEY")
boostrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")


def push_yt_trends(api, producer):
    country_trends = [
        api.fetch_trending_videos(region_code="US"),
        api.fetch_trending_videos(region_code="GE"),
        api.fetch_trending_videos(region_code="FR"),
        api.fetch_trending_videos(region_code="GB"),
        api.fetch_trending_videos(region_code="JP"),
        api.fetch_trending_videos(region_code="BR"),
    ]
    for trend in country_trends:
        producer.push(topic="yt-trend", messages=trend)


def push_yt_categories(api, producer):
    categories = api.fetch_categories()
    producer.push(topic="yt-categories", messages=categories)


def process():
    api = YoutubeAPI(api_key=api_key)
    producer = KafkaJsonProducer(bootstrap_servers=boostrap_servers)
    push_yt_categories(api, producer)
    push_yt_trends(api, producer)


if __name__ == "__main__":
    process()
