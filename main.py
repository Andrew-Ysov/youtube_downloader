from pytubefix import YouTube

link = input("введите ссылку на видео, которое хочтите скачать: ")
yt = YouTube(link)
available_streams = yt.streams

video_qualities = set()
for s in available_streams.filter(mime_type='video/mp4'):
    if s.resolution == None:
        continue
    video_qualities.add(s.resolution)

video_qualities = sorted(video_qualities)
print(", ".join(video_qualities[1:])+',', video_qualities[0])
video_quality = input('Выберите качество для видео: ')

if video_quality[-1] != 'p' or video_quality[-1].isdigit:
    video_quality += 'p'
if video_quality not in video_qualities:
    print('Выбрано недопустимое качество видео')

# отдельно скачиваются видео-файл и аудио-файл (стоит разобраться как они друг с другом взаимодействуют, какими бывают, в чём отличия)
# нужно выбрать видео и аудио файлы с правильным качеством и в правильном формате

video = available_streams.filter(resolution= video_quality, mime_type='"video/mp4"')
print(video)

audio_qualities = set()
for track in available_streams.filter(mime_type= 'audio/mp4'):
    print(track.abr)
    audio_qualities.add(track.abr)
audio_quality = input('Выберите качество звука: ')

if audio_quality[-1].isdigit():
    audio_quality += 'kbps'
if audio_quality not in audio_qualities:
    print('Выбрано недопустимое качество звука')
    
audio = available_streams.filter(abr=audio_quality, mime_type= 'audio/mp4')
print(audio)

# два файла объединяются в один полноценный файл, который сохраняется у пользователя