import urllib.request

from bs4 import BeautifulSoup

from funcs import get_initial_data


class Channel:
    def __init__(self, url: str) -> None:
        response = urllib.request.urlopen(url).read().decode("utf8")
        soup = BeautifulSoup(response, "html.parser")
        initial_data = get_initial_data(script_content=str(soup.find_all("script")[24]))

        self.name = self._get_meta_content(soup, 5)
        self.description: str = self._get_meta_content(soup, 11)
        self.channel_url: str = self._get_meta_content(soup, 7)
        self.profile_photo_url: str = self._get_meta_content(soup, 8)

        metadataParts = initial_data["header"]["pageHeaderRenderer"]["content"]["pageHeaderViewModel"]["metadata"]["contentMetadataViewModel"]["metadataRows"][1]["metadataParts"]
        self.subscribers_count: str = metadataParts[0]["text"]["content"].split(" ")[0]
        self.video_count: str = metadataParts[1]["text"]["content"].split(" ")[0]
        self.channel_id: str = initial_data["metadata"]["channelMetadataRenderer"]["externalId"]

        self.videos_page: str = self.channel_url + "/videos"
        self.shorts_page: str = self.channel_url + "/shorts"
        self.playlists_page: str = self.channel_url + "/playlists"
        self.community_page: str = self.channel_url + "/community"
        self.featured_channels_page: str = self.channel_url + "/channels"
        self.about_page: str = self.channel_url + "/about"

    @staticmethod
    def _get_meta_content(soup: BeautifulSoup, index: int) -> str:
        try:
            return str(soup.find_all("meta")[index]["content"])
        except (IndexError, KeyError):
            return ""
