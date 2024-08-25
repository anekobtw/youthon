import urllib.request
from datetime import datetime

from bs4 import BeautifulSoup

from funcs import get_initial_player_response


class Video:
    def __init__(self, url: str) -> None:
        response = urllib.request.urlopen(url).read().decode("utf8")
        soup = BeautifulSoup(response, "html.parser")
        videoDetails = get_initial_player_response(script_content=str(soup.find_all("script")[27 if "shorts" in url else 20]))["videoDetails"]

        self.title: str = self._get_meta_content(soup, property="og:title")
        self.video_url: str = self._get_meta_content(soup, property="og:url")
        self.thumbnail_url: str = self._get_meta_content(soup, property="og:image")
        self.views: str = int(self._get_meta_content(soup, itemprop="interactionCount"))
        self.genre: str = self._get_meta_content(soup, itemprop="genre")

        self.is_private: bool = videoDetails["isPrivate"]
        self.isLiveContent: bool = videoDetails["isLiveContent"]
        self.description: str = videoDetails["shortDescription"]
        self.author: str = videoDetails["author"]
        self.legth_seconds: int = int(videoDetails["lengthSeconds"])

        self.date_published: datetime = datetime.fromisoformat(soup.find("meta", itemprop="datePublished")["content"])

    @staticmethod
    def _get_meta_content(soup: BeautifulSoup, property: str = None, itemprop: str = None) -> str:
        try:
            if property:
                content = soup.find("meta", property=property)["content"]
            elif itemprop:
                content = soup.find("meta", itemprop=itemprop)["content"]
            return str(content)
        except (TypeError, KeyError, ValueError):
            return ""
