from pytubefix import YouTube

link = input('введите ссылку на видео, которое хочтите скачать: ')
yt = YouTube(link)

yt.streams.get_highest_resolution().download('C:/Users/destr/Downloads')