import os
from pytubefix import YouTube

link = input("введите ссылку на видео, которое хочтите скачать: ")
yt = YouTube(link)
available_streams = yt.streams.filter(file_extension='mp4')
print("Доступные варианты: ")
for stream in available_streams:
    resolution = stream.resolution if stream.resolution else "audio only"
    fps = f", fps: {stream.fps}" if hasattr(stream, 'fps') else ""
    print(f"itag: {stream.itag}, resolution: {resolution}{fps}, type: {stream.mime_type}")

itag_value = int(input("Введите номер тэга для нужного качества видео: "))
stream = yt.streams.get_by_itag(itag_value)

if stream:
    output_path = 'C:/Users/destr/Downloads'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    stream.download(output_path=output_path)
    print("Скачивание завершено")
else:
    print("Невозможно скачать видео с этим тэгом")
