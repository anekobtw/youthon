import requests

from youthon.funcs import get_yt_initial_data


class Channel:
    def __init__(self, url: str) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-61acac03-6279b8a6274777eb44d81aae",
            "X-Client-Data": "CJW2yQEIpLbJAQjEtskBCKmdygEIuevKAQjr8ssBCOaEzAEItoXMAQjLicwBCKyOzAEI3I7MARiOnssB",
        }
        response = requests.get(url, headers=headers)

        initial_data = get_yt_initial_data(response=response)
        metadata = initial_data["metadata"]["channelMetadataRenderer"]

        assert initial_data["responseContext"]["serviceTrackingParams"][0]["params"][0]["value"] == "channel."

        self.name = metadata["title"]
        self.description = metadata["description"]
        self.channel_url = metadata["channelUrl"]
        self.channel_id = metadata["externalId"]
        self.profile_photo_url = metadata["avatar"]["thumbnails"][0]["url"]

        metadata_parts = initial_data["header"]["pageHeaderRenderer"]["content"]["pageHeaderViewModel"]["metadata"]["contentMetadataViewModel"]["metadataRows"][1]["metadataParts"]
        self.subscribers_count = metadata_parts[0]["text"]["content"].split(" ")[0]
        self.video_count = metadata_parts[1]["text"]["content"].split(" ")[0]

        self.keywords = metadata["keywords"]
        self.is_family_safe = metadata["isFamilySafe"]
