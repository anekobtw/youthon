import json
import re

from requests import Response


def get_yt_initial_data(response: Response):
    pattern = re.compile(r"ytInitialData\s*=\s*({.*?});", re.DOTALL)
    match = pattern.search(response.text)
    if not match:
        raise Exception("ytInitialData not found in the page")

    json_str = match.group(1)
    return json.loads(json_str)


def get_initial_player_response(response: Response):
    pattern = re.compile(r"var ytInitialPlayerResponse\s*=\s*({.*?});", re.DOTALL)
    match = pattern.search(response.text)
    if not match:
        raise Exception("ytInitialPlayerResponse not found in the page")

    json_str = match.group(1)
    return json.loads(json_str)
