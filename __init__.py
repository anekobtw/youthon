"""A lightweight YouTube data scraper."""

__description__ = "A lightweight YouTube data scraper."
__url__ = "https://github.com/anekobtw/youthon"

__title__ = "youthon"
__author__ = "anekobtw"
__license__ = "MIT"
__version__ = "0.2.0"

from src.channel import Channel
from src.video import Video

__all__ = ("Channel", "Video")
