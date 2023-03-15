from pytube import YouTube
from halo import Halo
from pathlib import Path


def setup(download_path):
    Path(download_path).mkdir(parents=True, exist_ok=True)

def download(link, download_path):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        with Halo(text='Downloading...', spinner='dots'):
            youtube_object.download(download_path)
    except:
        print('Downloading went wrong...')
    print('Download succeded.')

download_directory = 'youtubes/'

setup(download_directory)
link = input('Enter YouTube video url: ')
download(link, download_directory)

