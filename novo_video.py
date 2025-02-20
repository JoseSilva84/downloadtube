from moviepy import *


pasta_video = r'C:\Users\curso\Downloads\Python\Baixar video com pytubefix\video\video1.mp4'
pasta_audio = r'C:\Users\curso\Downloads\Python\Baixar video com pytubefix\audio\audio1.m4a'

video = VideoFileClip(pasta_video)
audio = AudioFileClip(pasta_audio)

video_com_audio = video.with_audio(audio)

video_com_audio.write_videofile("video_com_audio.mp4", codec="libx264", audio_codec="aac")

