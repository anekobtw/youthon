import requests

from youthon.funcs import get_initial_player_response


class Video:
    def __init__(self, url: str) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-61acac03-6279b8a6274777eb44d81aae",
            "X-Client-Data": "CJW2yQEIpLbJAQjEtskBCKmdygEIuevKAQjr8ssBCOaEzAEItoXMAQjLicwBCKyOzAEI3I7MARiOnssB",
        }
        response = requests.get(url, headers=headers)

        video_details = get_initial_player_response(response)["videoDetails"]

        self.title = video_details["title"]
        self.video_url = f'https://www.youtube.com/watch?v={video_details["videoId"]}'
        self.thumbnail_url = video_details["thumbnail"]["thumbnails"][-1]["url"]
        self.description = video_details["shortDescription"]
        self.author_name = video_details["author"]

        self.views = int(video_details.get("viewCount", 0))
        self.length_seconds = int(video_details.get("lengthSeconds", 0))

        self.allowRatings = video_details["allowRatings"]
        self.isLiveContent = video_details["isLiveContent"]
        self.is_private = video_details["isPrivate"]

        self.keywords = video_details.get("keywords", [])
