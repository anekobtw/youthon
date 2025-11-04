import time
from functools import wraps
from colorama import Fore

from youthon import Channel, Playlist, Video


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{Fore.RED}Function {Fore.CYAN}{func.__name__}{args} {kwargs} {Fore.RED} Took {total_time:.4f} seconds{Fore.RESET}")
        return result

    return timeit_wrapper


@timeit
def example_channel():
    channel = Channel("https://www.youtube.com/@PewDiePie")

    print(channel.name)  # PewDiePie
    print(channel.description)  # I make videos.
    print(channel.channel_url)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw
    print(channel.profile_photo_url)  # https://yt3.googleusercontent.com/5oUY3tashyxfqsjO5SGhjT4dus8FkN9CsAHwXWISFrdPYii1FudD4ICtLfuCw6-THJsJbgoY=s900-c-k-c0x00ffffff-no-rj
    print(channel.channel_id)  # UC-lHJZR3Gqxm24_Vd_AJ5Yw
    print(channel.keywords)  # pewdiepie pewds gaming "felix arvid ulf" felix kjellberg
    print(channel.is_family_safe)  # True

    # The following two variables may produce different results depending on your geolocation.
    print(channel.subscribers_count)  # 110M
    print(channel.video_count)  # 4.6K


@timeit
def example_video():
    video = Video("https://youtu.be/XqZsoesa55w")

    print(video.title)  #  Baby Shark Dance | #babyshark Most Viewed Video | Animal Songs | PINKFONG Songs for Children
    print(video.description)  # a loooong description :)
    print(video.author_name)  # Baby Shark - Pinkfong Kids’ Songs & Stories
    print(video.video_url)  # https://www.youtube.com/watch?v=XqZsoesa55w

    print(video.views)  # 16388060778
    print(video.thumbnail_url)  # https://i.ytimg.com/vi_webp/XqZsoesa55w/maxresdefault.webp
    print(video.length_seconds)  # 136
    print(video.isLiveContent)  # False
    print(video.is_private)  # False
    print(video.allowRatings)  # True
    print(video.keywords)  # ['baby shark', 'baby shark dance', 'baby shark song',  ... ]


@timeit
def example_shorts_video():
    video = Video("https://www.youtube.com/shorts/JfbnpYLe3Ms")

    print(video.title)  # If Cleaning Was a Timed Sport. Part 2
    print(video.description)  # Watch behind the scenes here: https://www.you ...
    print(video.author_name)  # Daniel LaBelle
    print(video.video_url)  # https://www.youtube.com/watch?v=JfbnpYLe3Ms

    print(video.views)  #BUG: always 0 for shorts
    print(video.thumbnail_url)  # https://i.ytimg.com/vi/JfbnpYLe3Ms/maxresdefault.jpg?sqp=-oaymwEoCIAKENAF8quKqQMcGADwAQH4AbYIgAKAD4oCDAgAEAEYZSBYKEcwDw==&rs=AOn4CLB2-XNEljrgIdrAYWG6crFFQh95VA
    print(video.length_seconds)  # 37
    print(video.isLiveContent)  # False
    print(video.is_private)  # False
    print(video.allowRatings)  # True
    print(video.keywords)  # ['cleaning', 'physical comedy', 'speed', 'fast']


@timeit
def example_playlist():
    playlist = Playlist("https://www.youtube.com/watch?v=K4DyBUG242c&list=PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD")
    print(playlist.title)  # NCS : The Top 100 Biggest Songs 📈
    print(playlist.author_name)  # NoCopyrightSounds
    print(playlist.author_url)  # http://www.youtube.com/@NoCopyrightSounds
    print(playlist.total_videos)  # 100
    print(playlist.playlist_id)  # PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD
    print(playlist.playlist_url)  # https://www.youtube.com/playlist?list=PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD
    print(playlist.video_urls)  # ['https://youtube.com/watch/?v=K4DyBUG242c', 'https://youtube.com/watch/?v=3nQNiWdeH2Q', 'https://youtube.com/watch/?v=J2X5mJ3HDYE', ... ]


example_channel()
example_video()
example_shorts_video()
example_playlist()
