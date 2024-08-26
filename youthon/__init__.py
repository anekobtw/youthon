"""A lightweight YouTube data scraper."""

__description__ = "A lightweight YouTube data scraper."
__url__ = "https://github.com/anekobtw/youthon"

__title__ = "youthon"
__author__ = "anekobtw"
__license__ = "MIT"
__version__ = "0.3.2"

from channel import Channel
from playlist import Playlist
from video import Video

__all__ = ("Channel", "Video", "Playlist")
