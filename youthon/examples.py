import channel
import video


def example_channel():
    channel1 = channel.Channel("https://www.youtube.com/@PewDiePie")

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


def example_video():
    video1 = video.Video("https://youtu.be/XqZsoesa55w")

    print(video1.title)  #  Baby Shark Dance | #babyshark Most Viewed Video | Animal Songs | PINKFONG Songs for Children
    print(video1.description)  # a loooong description :)
    print(video1.author)  # Baby Shark - Pinkfong Kids’ Songs & Stories
    print(video1.video_url)  # https://www.youtube.com/watch?v=XqZsoesa55w

    print(video1.views)  # 14941899516
    print(video1.thumbnail_url)  # https://i.ytimg.com/vi/XqZsoesa55w/maxresdefault.jpg
    print(video1.date_published)  # 2016-06-17 16:00:30-07:00
    print(video1.legth_seconds)  # 136
    print(video1.isLiveContent)  # False
    print(video1.is_private)  # False
    print(video1.genre)  # Education


def example_shorts_video():
    video2 = video.Video("https://www.youtube.com/shorts/JfbnpYLe3Ms")

    print(video2.title)
    print(video2.description)
    print(video2.author)
    print(video2.video_url)

    print(video2.views)
    print(video2.thumbnail_url)
    print(video2.date_published)
    print(video2.legth_seconds)
    print(video2.isLiveContent)
    print(video2.is_private)
    print(video2.genre)


example_channel()
example_video()
example_shorts_video()
