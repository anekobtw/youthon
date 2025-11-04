import requests
from bs4 import BeautifulSoup

from youthon.funcs import get_yt_initial_data


class Playlist:
    def __init__(self, url: str) -> None:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        initial_data = get_yt_initial_data(response)
        metadata = initial_data["contents"]["twoColumnWatchNextResults"]["playlist"]["playlist"]

        self.title = metadata["title"]
        self.author_name = metadata["ownerName"]["simpleText"]
        self.author_url = soup.find_all("span")[0].find("link")["href"]

        self.playlist_id = metadata["playlistId"]
        self.playlist_url = metadata["playlistShareUrl"]
        self.total_videos = int(metadata["totalVideos"])
        self.is_infinite = metadata.get("isInfinite", False)

        self.video_urls = [f'https://youtube.com/watch/?v={metadata["contents"][video_id]["playlistPanelVideoRenderer"]["navigationEndpoint"]["watchEndpoint"]["videoId"]}' for video_id in range(self.total_videos)]
