from pytubefix import YouTube

link = input("введите ссылку на видео, которое хочтите скачать: ")
yt = YouTube(link)
available_streams = yt.streams

video_qualities = set()
for s in available_streams.filter(mime_type='video/mp4'):
    if s.resolution == None:
        continue
    video_qualities.add(int(s.resolution[:-1]))

video_qualities = sorted(video_qualities)
for i,v in enumerate(video_qualities):
    video_qualities[i] = str(v) + 'p'
print(video_qualities)
video_quality = input('Выберите качество для видео: ')

if video_quality[-1] != 'p' or video_quality[-1].isdigit:
    video_quality += 'p'
if video_quality not in video_qualities:
    print('Выбрано недопустимое качество видео')

video = available_streams.filter(resolution= video_quality, mime_type='video/mp4').first()
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
    
audio = available_streams.filter(abr=audio_quality, mime_type= 'audio/mp4').first()
print(audio)

audio.download(output_path='C:/Users/destr/Downloads', filename='audio.mp4')
video.download(output_path='C:/Users/destr/Downloads', filename='video.mp4', )

# два файла объединяются в один полноценный файл, который сохраняется у пользователя
# а два старых файла нужно удалить