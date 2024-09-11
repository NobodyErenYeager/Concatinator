from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://youtube.com/watch?v=0b7QxdubrLI"

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

for stream in yt.streams:
  print(stream)