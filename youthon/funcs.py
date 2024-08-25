import json
import re

from graphviz import Digraph


def get_initial_data(script_content: str) -> str | Exception:
    pattern = re.compile(r"var ytInitialData = ({.*?});", re.DOTALL)
    match = pattern.search(script_content)

    if match:
        json_str = match.group(1)
        return json.loads(json_str)
    else:
        raise Exception("ytInitialData not found.")


def get_initial_player_response(script_content: str) -> str | Exception:
    pattern = re.compile(r"var ytInitialPlayerResponse = ({.*?});", re.DOTALL)
    match = pattern.search(script_content)

    if match:
        json_str = match.group(1)
        return json.loads(json_str)
    else:
        raise Exception("ytInitialPlayerResponse not found.")


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
