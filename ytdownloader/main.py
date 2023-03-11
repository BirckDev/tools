from pytube import YouTube
from halo import Halo
from time import sleep


def download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        with Halo(text='Downloading...', spinner='dots'):
            youtube_object.download('youtubes/')
    except:
        print('Downloading went wrong...')
    print('Download succeded.')



link = input('Enter YouTube video url: ')
download(link)

