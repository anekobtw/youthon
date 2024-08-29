import requests
from bs4 import BeautifulSoup

from youthon.funcs import get_yt_initial_data


class Channel:
    def __init__(self, url: str) -> None:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-61acac03-6279b8a6274777eb44d81aae", "X-Client-Data": "CJW2yQEIpLbJAQjEtskBCKmdygEIuevKAQjr8ssBCOaEzAEItoXMAQjLicwBCKyOzAEI3I7MARiOnssB"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        meta_tags = soup.find_all("meta")
        initial_data = get_yt_initial_data(response=response)

        self.name = meta_tags[5]["content"]
        self.description = meta_tags[11]["content"]
        self.channel_url = meta_tags[7]["content"]
        self.profile_photo_url = meta_tags[8]["content"]

        metadata_parts = initial_data["header"]["pageHeaderRenderer"]["content"]["pageHeaderViewModel"]["metadata"]["contentMetadataViewModel"]["metadataRows"][1]["metadataParts"]
        self.subscribers_count = metadata_parts[0]["text"]["content"].split(" ")[0]
        self.video_count = metadata_parts[1]["text"]["content"].split(" ")[0]
        self.channel_id = initial_data["metadata"]["channelMetadataRenderer"]["externalId"]

        self.videos_page = f"{self.channel_url}/videos"
        self.shorts_page = f"{self.channel_url}/shorts"
        self.playlists_page = f"{self.channel_url}/playlists"
        self.community_page = f"{self.channel_url}/community"
        self.featured_channels_page = f"{self.channel_url}/channels"
        self.about_page = f"{self.channel_url}/about"
