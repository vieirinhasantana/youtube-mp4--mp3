from os import path

from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *

data = [
    {
        "folder": "mp4",
        "playlist_url": "https://www.youtube.com/watch?v=XXYlFuWEuKI&list=RDQMgEzdN5RuCXE&start_radio=1&ab_channel=TheWeekndVEVO"
    }
]


def download_playlist_youtube():
    for row in data:
        playlist = Playlist(row.get("playlist_url"))
        total = len(playlist)
        if not path.isdir(row.get("folder")):
            os.mkdir(row.get("folder"))

        for indx, url in enumerate(playlist):
            _id = total - indx
            YouTube(url).streams.filter(only_audio=True, file_extension='mp4').first().download(
                row.get("folder"),
                filename_prefix=f"{str(_id).zfill(6)}_"
            )
            print(url)


def converter_mp4_to_mp3():
    for row in data:
        if not path.isdir(f"converted-mp3/{row.get('folder')}"):
            os.mkdir(f"converted-mp3/{row.get('folder')}")

        for item in os.listdir(row.get('folder')):
            clip = AudioFileClip(f"{row.get('folder')}/{item}")
            clip.write_audiofile(f"converted-mp3/{row.get('folder')}/{item[:-4]}.mp3")
            clip.close()


if __name__ == '__main__':
    download_playlist_youtube()
    converter_mp4_to_mp3()

