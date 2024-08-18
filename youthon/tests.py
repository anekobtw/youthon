import channel
import video

channel = channel.Channel("https://www.youtube.com/@PewDiePie")

print(channel.name)  # PewDiePie
print(channel.description)  # I make videos.
print(channel.channel_url)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw
print(channel.profile_photo_url)  # https://yt3.googleusercontent.com/5oUY3tashyxfqsjO5SGhjT4dus8FkN9CsAHwXWISFrdPYii1FudD4ICtLfuCw6-THJsJbgoY=s900-c-k-c0x00ffffff-no-rj
print(channel.channel_id)  # UC-lHJZR3Gqxm24_Vd_AJ5Yw

# The following two variables may produce different results depending on your geolocation.
print(channel.subscribers_count)
print(channel.video_count)

print(channel.videos_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/videos
print(channel.shorts_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/shorts
print(channel.community_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/community
print(channel.featured_channels_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/channels
print(channel.playlists_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/playlists
print(channel.about_page)  # https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw/about


video = video.Video("https://youtu.be/XqZsoesa55w")

print(video.title)  #  Baby Shark Dance | #babyshark Most Viewed Video | Animal Songs | PINKFONG Songs for Children
print(video.description)  # a loooong description :)
print(video.author)  # Baby Shark - Pinkfong Kids’ Songs & Stories
print(video.video_url)  # https://www.youtube.com/watch?v=XqZsoesa55w

print(video.views)  # 14941899516
print(video.thumbnail_url)  #https://i.ytimg.com/vi/XqZsoesa55w/maxresdefault.jpg
print(video.date_published)  # 2016-06-17 16:00:30-07:00
print(video.legth_seconds)  # 136
print(video.isLiveContent)  # False
print(video.is_private)  # False
print(video.genre)  # Education