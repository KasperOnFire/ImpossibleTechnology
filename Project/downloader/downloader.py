from __future__ import unicode_literals
import youtube_dl
import sys
import os

seperator  = os

link = sys.argv[1]

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [my_hook],
    'noplaylist': True,
    'outtmpl': os.path.join('mp3', %(title)s.%(ext)s), #TODO Name parsing
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])