from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

url = input("Digite o link do youtube: ")

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

titulo = r"C:\Users\curso\Downloads\Python\Baixar video com pytubefix\audio" + "\\" + yt.title + ".m4a"


destino = "audio"

ys = yt.streams.get_audio_only()

if ys:
    ys.download(output_path=destino)
    print("Download concluído!")
    caminho_atual = titulo
    caminho_novo = r"C:\Users\curso\Downloads\Python\Baixar video com pytubefix\audio\audio1.m4a"
    os.rename(caminho_atual, caminho_novo)
    print("Áudio renomeado com sucesso!")
else:
    print("Não foi possível encontrar um stream de vídeo adequado.")