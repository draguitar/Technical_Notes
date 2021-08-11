
from pytube import YouTube

URL = "https://www.youtube.com/watch?v=os7kDPhtPxY"
video = YouTube(URL)

video_streams = video.streams
print(video_streams)

video_streams = video.streams.filter(file_extension='mp4').get_by_itag(22)
print(video_streams.title)

video_streams.download(filename = "my first YouTube download2",
	output_path = r"D:\小玉.mp4")

# %%
from enum import Enum
from enum import unique
@unique
class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3
	ORANGE = 4

print(Color.RED.value)


# %%
