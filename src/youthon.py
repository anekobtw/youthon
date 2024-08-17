import json
import re
import urllib.request

from bs4 import BeautifulSoup


class Channel:
    def __init__(self, url: str) -> None:
        # IT WORKS, DON'T TOUCH IT (please)
        response = urllib.request.urlopen(f"{url}/?persist_gl=1&gl=US").read().decode("utf8")
        _soup = BeautifulSoup(response, "html.parser")
        _soup.prettify()
        _all_metas = _soup.find_all("meta")
        _all_scripts = _soup.find_all("script")
        initial_data = self.get_initial_data(script_content=str(_all_scripts[24]))

        self.name: str = str(_all_metas[5]["content"])
        self.description: str = str(_all_metas[11]["content"])
        self.channel_url: str = str(_all_metas[7]["content"])
        self.channel_id = initial_data["metadata"]["channelMetadataRenderer"]["externalId"]
        self.profile_photo_url: str = str(_all_metas[8]["content"])

        # WARNING: THIS MAY RETURN DIFFERENT RESULTS BASED ON
        subscribers_count_raw = initial_data["header"]["pageHeaderRenderer"]["content"]["pageHeaderViewModel"]["metadata"]["contentMetadataViewModel"]["metadataRows"][1]["metadataParts"][0]["text"]["content"].split(" ")[0]
        self.subscribers_count = subscribers_count_raw.split(" ")[0]
        video_count_raw = initial_data["header"]["pageHeaderRenderer"]["content"]["pageHeaderViewModel"]["metadata"]["contentMetadataViewModel"]["metadataRows"][1]["metadataParts"][1]["text"]["content"]
        self.video_count: int = video_count_raw.split(" ")[0]

        self.videos_page = self.channel_url + "/videos"
        self.shorts_page = self.channel_url + "/shorts"
        self.playlists_page = self.channel_url + "/playlists"
        self.community_page = self.channel_url + "/community"
        self.featured_channels_page = self.channel_url + "/channels"
        self.about_page = self.channel_url + "/about"

    @staticmethod
    def get_initial_data(script_content: str) -> str | Exception:
        pattern = re.compile(r"var ytInitialData = ({.*?});", re.DOTALL)
        match = pattern.search(script_content)

        if match:
            json_str = match.group(1)
            return json.loads(json_str)
        else:
            raise Exception("ytInitialData not found.")
