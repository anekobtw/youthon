# `youthon`
![version](https://img.shields.io/badge/Project_version-0.1.0-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![made with love](https://img.shields.io/badge/Made_with-Love-red)

A lightweight YouTube data scraper.

# Installing
#### pip
To install from PyPI with pip:
```
$ pip install youthon
```

#### poetry
You can add youthon as a dependency with the following command
```
$ poetry add youthon
```

# Usage Examples
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

## About the project
### Authors
- [@anekobtw](https://www.github.com/anekobtw) 

## Contributing
Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

## License
The project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
