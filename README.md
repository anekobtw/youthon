# `youthon`
![version](https://img.shields.io/badge/Project_version-0.2.1-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![made with love](https://img.shields.io/badge/Made_with-Love-red)
[![pypi](https://img.shields.io/badge/youthon_on_PyPi-blue)](https://pypi.org/project/youthon/)

A lightweight YouTube data scraper.

# Installing
### pip
To install from PyPI with pip:
```
$ pip install youthon
```

### poetry
You can add youthon as a dependency with the following command
```
$ poetry add youthon
```

# Usage Examples
### Fetching channels
```py
import youthon

channel = youthon.Channel("https://www.youtube.com/@PewDiePie")

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
```

### Fetching videos
```py
import youthon

video = youthon.Video("https://youtu.be/XqZsoesa55w")

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
```

## About the project
### Authors
- [@anekobtw](https://www.github.com/anekobtw) 

## Contributing
Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

## License
The project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
