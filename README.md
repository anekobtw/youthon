# `youthon`
![version](https://img.shields.io/badge/Project_version-0.4.3-blue)
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
print(channel.keywords)  # pewdiepie pewds gaming "felix arvid ulf" felix kjellberg
print(channel.is_family_safe)  # True

# The following two variables may produce different results depending on your geolocation.
print(channel.subscribers_count)  # 110M
print(channel.video_count)  # 4.6K
```

### Fetching videos
```py
import youthon

video = youthon.Video("https://youtu.be/XqZsoesa55w")

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
```

### Fetching playlists
```py
import youthon

playlist = youthon.Playlist("https://www.youtube.com/watch?v=K4DyBUG242c&list=PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD&ab_channel=NoCopyrightSounds")

print(playlist.title)  # NCS : The Top 100 Biggest Songs 📈
print(playlist.author.name)  # http://www.youtube.com/@NoCopyrightSounds
print(playlist.total_videos)  # 100
print(playlist.playlist_id)  # PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD
print(playlist.playlist_url)  # https://www.youtube.com/playlist?list=PLRBp0Fe2Gpgm_u2w2a2isHw29SugZ34cD
print(playlist.video_urls)  # ['https://youtube.com/watch/?v=K4DyBUG242c', 'https://youtube.com/watch/?v=3nQNiWdeH2Q', 'https://youtube.com/watch/?v=J2X5mJ3HDYE', ... ]
```

## About the project
### Authors
- [@anekobtw](https://www.github.com/anekobtw) 

## Contributing
Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's [code of conduct](https://github.com/anekobtw/youthon?tab=coc-ov-file).

## License
The project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
