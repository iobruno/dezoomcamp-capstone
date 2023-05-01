from typing import List

import httpx

from pipelines.youtube import Video, VideoCategory


class YoutubeAPI:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = "https://www.googleapis.com/youtube/v3"

    def fetch_video_analytics(self,
                              region_code: str = "US",
                              max_results: int = 50,
                              page_token: str = "") -> List:
        params = {
            "key": self.api_key,
            "part": ["topicDetails", "snippet", "statistics"],
            "chart": "mostPopular",
            "regionCode": region_code,
            "maxResults": max_results,
            "pageToken": page_token,
        }
        response = httpx.get(f"{self.endpoint}/videos", params=params)
        data = response.json()
        items: List = data["items"]

        if "nextPageToken" in data:
            return items + self.fetch_video_analytics(page_token=data["nextPageToken"])

        return items

    def fetch_trending_videos(self, region_code: str = "US") -> List[Video]:
        items = self.fetch_video_analytics(region_code=region_code)
        trending_videos = list(map(lambda item: Video(
            item.get("id"),
            item.get("snippet", {}).get("title"),
            item.get("snippet", {}).get("categoryId"),
            item.get("snippet", {}).get("publishedAt"),
            item.get("topicDetails", {}).get("topicCategories"),
            region_code,
        ), items))

        return trending_videos

    def fetch_categories(self, region_code: str = "US") -> List[VideoCategory]:
        params = {"key": self.api_key, "regionCode": region_code}
        response = httpx.get(f"{self.endpoint}/videoCategories", params=params)

        items = response.json().get("items")
        categories = list(map(lambda cat: VideoCategory(
            cat.get("id"),
            cat.get("snippet", {}).get("title")
        ), items))

        return categories
