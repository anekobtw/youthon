import json
import re

from graphviz import Digraph
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


def visualize_dict(d, parent_key=None, graph=None):
    if graph is None:
        graph = Digraph()

    for key, value in d.items():
        node_key = f"{parent_key}.{key}" if parent_key else str(key)
        graph.node(node_key, str(key))

        if parent_key:
            graph.edge(parent_key, node_key)

        if isinstance(value, dict):
            visualize_dict(value, node_key, graph)
        else:
            value_node = f"{node_key}.value"
            graph.node(value_node, str(value))
            graph.edge(node_key, value_node)

    return graph
