import requests
from bs4 import BeautifulSoup

from youthon.funcs import get_yt_initial_data


class Playlist:
    def __init__(self, url: str) -> None:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        initial_data = get_yt_initial_data(response)

        playlist_data = initial_data["contents"]["twoColumnWatchNextResults"]["playlist"]["playlist"]

        self.title: str = playlist_data.get("title", "Unknown Title")
        self.author_url: str = soup.find_all("span")[0].find("link")["href"]
        self.playlist_id: str = playlist_data.get("playlistId", "")
        self.playlist_url: str = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.total_videos: int = int(playlist_data.get("totalVideos", 0))
        self.is_infinite: bool = playlist_data.get("isInfinite", False)

        self.video_urls = [self.get_video_url(i, playlist_data) for i in range(self.total_videos)]

    def get_video_url(self, video_id: int, playlist_data) -> str:
        try:
            return f'https://youtube.com/watch/?v={playlist_data["contents"][video_id]["playlistPanelVideoRenderer"]["navigationEndpoint"]["watchEndpoint"]["videoId"]}'
        except (IndexError, KeyError):
            return f"Error: Video ID {video_id} not found"
