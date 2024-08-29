from datetime import datetime

import requests
from bs4 import BeautifulSoup

from youthon.funcs import get_initial_player_response


class Video:
    def __init__(self, url: str) -> None:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-61acac03-6279b8a6274777eb44d81aae", "X-Client-Data": "CJW2yQEIpLbJAQjEtskBCKmdygEIuevKAQjr8ssBCOaEzAEItoXMAQjLicwBCKyOzAEI3I7MARiOnssB"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        video_details = get_initial_player_response(response)["videoDetails"]
        meta_tags = {tag.get("name"): tag.get("content") for tag in soup.find_all("meta") if tag.get("name")}

        self.title = meta_tags.get("og:title", "")
        self.video_url = meta_tags.get("og:url", "")
        self.thumbnail_url = meta_tags.get("og:image", "")
        self.views = int(meta_tags.get("interactionCount", 0))
        self.genre = meta_tags.get("genre", "")

        self.is_private = video_details.get("isPrivate", False)
        self.isLiveContent = video_details.get("isLiveContent", False)
        self.description = video_details.get("shortDescription", "")
        self.author = video_details.get("author", "")
        self.length_seconds = int(video_details.get("lengthSeconds", 0))

        date_published_str = meta_tags.get("datePublished", "")
        self.date_published = datetime.fromisoformat(date_published_str) if date_published_str else None
