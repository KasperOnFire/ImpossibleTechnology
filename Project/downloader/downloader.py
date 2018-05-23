from __future__ import unicode_literals
import youtube_dl
import sys
import os

link = sys.argv[1]

# Renames a file from format "artist - title.ext" to  "artist-name--title-name.ext"
def parse_title(file_name):
    words = file_name.split("-")
    artist = words[0].replace(" ", "-")
    title = words[1].replace(" ", "-")
    title_format = artist + title
    return title_format

# Define the options for youtube downloader. Most important is outtmpl - defines the template for the filename afterwards.
# Downloads the video as a stream, so it can start converting while still downloading. This means max speed is your net speed.
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': True,
    'outtmpl': os.path.join('mp3', '%(title)s.%(ext)s') #TODO Name parsing
}

#Download the file with the given options
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

# rename files in mp3 folder according to dajvu file names
for filename in os.listdir("mp3"):
    os.replace(os.path.join("mp3", filename), os.path.join("mp3", parse_title(filename)))