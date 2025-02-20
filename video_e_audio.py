from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

url = input("Digite o link do youtube: ")

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

yt2 = YouTube(url, on_progress_callback=on_progress)

destino_video = "video"
destino_audio = "audio"

# stream do vídeo
ys = yt.streams.filter(adaptive=True).order_by('resolution').desc().first()

# stream do aúdio do vídeo
ys2 = yt2.streams.get_audio_only()

if ys and ys2:
    # download do vídeo
    baixado_video = ys.download(output_path=destino_video)
    print("Download do vídeo concluído em alta resolução!")
    if baixado_video:
        caminho_novo_video = r"C:\Users\curso\Downloads\Python\Baixar video com pytubefix\video\video1.mp4"
        os.rename(baixado_video, caminho_novo_video)
        print("Vídeo renomeado com sucesso!")
    else:
        print("Não foi possível renomear o vídeo.")
    
    # download do aúdio do vídeo
    baixado_audio = ys2.download(output_path=destino_audio)
    print("Download do aúdio concluído!")
    if baixado_audio:
        caminho_novo_audio = r"C:\Users\curso\Downloads\Python\Baixar video com pytubefix\audio\audio1.m4a"
        os.rename(baixado_audio, caminho_novo_audio)
        print("Áudio renomeado com sucesso!")
    else:
        print("Não foi possível renomear o áudio.")
else:
    print("Não foi possível encontrar um stream de vídeo adequado.")