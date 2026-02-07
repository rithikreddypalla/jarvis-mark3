import os
import time
import urllib.request
import re
from pytube import YouTube
import pafy

def youtube(a):
    yt = YouTube(a)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='.')
    base, ext = os.path.splitext(out_file)
    os.rename(out_file, 'song.mp3')
    videoy = pafy.new(a)
    os.system('aplay song.mp3')
    time.sleep((videoy.length) + 2)
    os.remove('song.mp3')

def songs(sk):
    sk = sk.replace(" ", "+")
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={sk}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    youtube(f"https://www.youtube.com/watch?v={video_ids[0]}")
