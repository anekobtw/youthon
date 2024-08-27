import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

from youthon.channel import Channel
from youthon.funcs import get_initial_data
from youthon.video import Video


class Playlist:
    def __init__(self, url="") -> None:
        response = urllib.request.urlopen(url).read().decode("utf8")
        soup = BeautifulSoup(response, "html.parser")
        initial_data = get_initial_data(str(soup.find_all("script")[45]))
        self.playlist_data = initial_data["contents"]["twoColumnWatchNextResults"]["playlist"]["playlist"]

        self.title: str = self.playlist_data["title"]
        self.author: Channel = Channel(soup.find_all("span")[0].find("link")["href"])
        self.playlist_id: str = self.playlist_data["playlistId"]
        self.playlist_url: str = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.total_videos: int = int(self.playlist_data["totalVideos"])
        self.is_infinite: bool = self.playlist_data["isInfinite"]

        self.video_urls: list[str] = [self.get_video(i) for i in range(self.total_videos)]

    def get_video(self, video_id: int) -> Video:
        video = self.playlist_data["contents"][video_id]["playlistPanelVideoRenderer"]["navigationEndpoint"]["watchEndpoint"]["videoId"]
        return f"https://youtube.com/watch/?v={video}"
