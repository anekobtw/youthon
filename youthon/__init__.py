"""A lightweight YouTube data scraper."""

__description__ = "A lightweight YouTube data scraper."
__url__ = "https://github.com/anekobtw/youthon"

__title__ = "youthon"
__author__ = "anekobtw"
__license__ = "MIT"
__version__ = "0.4.1"

from youthon.channel import Channel
from youthon.playlist import Playlist
from youthon.video import Video

__all__ = ("Channel", "Video", "Playlist")
