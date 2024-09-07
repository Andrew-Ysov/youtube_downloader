from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os

link = input("введите ссылку на видео, которое хочтите скачать: ")
yt = YouTube(link)
available_streams = yt.streams
download_to = 'C:/Users/destr/Downloads'

def download_video(available_streams, path):
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

    video.download(output_path= path, filename=f'video of {video.title}.mp4', )

    video_name = f'video of {video.title}.mp4'
    return video_name

def download_audio(available_streams, path):
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

    audio.download(output_path= path, filename=f'audio of {audio.title} .mp4')
    
    audio_name = f'audio of {audio.title} .mp4'
    return audio_name

def concatinate_video_and_audio(v_name, a_name, path):

    v_path = (path + '/' + v_name)
    a_path = (path + '/' + a_name)
    full = (path + '/' + v_name[9:])

    video_clip = VideoFileClip(v_path)
    audio_clip = AudioFileClip(a_path)

    video_clip.audio = audio_clip
    video_clip.write_videofile(full)

    os.remove(path + '/' + a_name)
    os.remove(path + '/' + v_name)

type_of_content = input('Введите 1, если хотите скачать только видео, 2- только аудио, \n'
      'что-угодно или ничего, если хотите скачать и видео и аудио: ')

if type_of_content == str('1'):
    download_video(available_streams, download_to)
elif type_of_content == str('2'):
    download_audio(available_streams, download_to)
else:
    video_name = download_video(available_streams, download_to)
    audio_name = download_audio(available_streams, download_to)
    concatinate_video_and_audio(video_name, audio_name, download_to)