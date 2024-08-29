import time
from functools import wraps

from youthon import Channel, Playlist, Video


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


@timeit
def example_channel():
    channel1 = Channel("https://www.youtube.com/@PewDiePie")

    print(channel1.name)  # PewDiePie
    print(channel1.description)  # I make videos.
    print(channel1.channel_url)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw
    print(channel1.profile_photo_url)  # https://yt3.googleusercontent.com/5oUY3tashyxfqsjO5SGhjT4dus8FkN9CsAHwXWISFrdPYii1FudD4ICtLfuCw6-THJsJbgoY=s900-c-k-c0x00ffffff-no-rj
    print(channel1.channel_id)  # UC-lHJZR3Gqxm24_Vd_AJ5Yw

    # The following two variables may produce different results depending on your geolocation.
    print(channel1.subscribers_count)
    print(channel1.video_count)

    print(channel1.videos_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/videos
    print(channel1.shorts_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/shorts
    print(channel1.community_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/community
    print(channel1.featured_channels_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/channels
    print(channel1.playlists_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/playlists
    print(channel1.about_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/about


@timeit
def example_video():
    video = Video("https://youtu.be/XqZsoesa55w")

    print(video.title)  #  Baby Shark Dance | #babyshark Most Viewed Video | Animal Songs | PINKFONG Songs for Children
    print(video.description)  # a loooong description :)
    print(video.author_name)  # Baby Shark - Pinkfong Kids’ Songs & Stories
    print(video.video_url)  # https://www.youtube.com/watch?v=XqZsoesa55w

    print(video.views)  # 14941899516
    print(video.thumbnail_url)  # https://i.ytimg.com/vi_webp/XqZsoesa55w/maxresdefault.webp
    print(video.length_seconds)  # 136
    print(video.isLiveContent)  # False
    print(video.is_private)  # False
    print(video.allowRatings)  # True
    print(video.keywords)  # ['baby shark', 'baby shark dance', 'baby shark song', 'cute dance for children' ...


@timeit
def example_shorts_video():
    video = Video("https://www.youtube.com/shorts/JfbnpYLe3Ms")

    print(video.title)
    print(video.description)
    print(video.author_name)
    print(video.video_url)

    print(video.views)
    print(video.thumbnail_url)
    print(video.length_seconds)
    print(video.isLiveContent)
    print(video.is_private)
    print(video.allowRatings)
    print(video.keywords)


@timeit
def example_playlist():
    playlist1 = Playlist("https://www.youtube.com/watch?v=K4DyBUG242c&list=PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD&ab_channel=NoCopyrightSounds")
    print(playlist1.title)  # NCS : The Top 100 Biggest Songs 📈
    print(playlist1.author_url)  # http://www.youtube.com/@NoCopyrightSounds
    print(playlist1.total_videos)  # 100
    print(playlist1.playlist_id)  # PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD
    print(playlist1.playlist_url)  # https://www.youtube.com/playlist?list=PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD
    print(playlist1.video_urls)  # ['https://youtube.com/watch/?v=K4DyBUG242c', 'https://youtube.com/watch/?v=3nQNiWdeH2Q', 'https://youtube.com/watch/?v=J2X5mJ3HDYE', ... ]


example_channel()
example_video()
example_shorts_video()
example_playlist()
