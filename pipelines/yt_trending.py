import os

import httpx
from typing import List

YT_API_KEY = os.getenv("YT_API_KEY")


def fetch_trending_videos(region_code: str = "US",
                          max_results: int = 50,
                          page_token: str = "") -> List:
    params = {
        "key": YT_API_KEY,
        "regionCode": region_code,
        "maxResults": max_results,
        "pageToken": page_token,
        "part": ["topicDetails", "snippet", "statistics"],
        "chart": "mostPopular"
    }
    response = httpx.get(url="https://www.googleapis.com/youtube/v3/videos",
                         params=params)
    data = response.json()
    items: List = data["items"]

    if "nextPageToken" in data:
        return items + fetch_trending_videos(page_token=data["nextPageToken"])

    return items
