from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

url = input("Digite o link do youtube: ")

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)
titulo = r"C:\Users\curso\Downloads\Python\Baixar video com pytubefix\video" + "\\" + yt.title + ".mp4"

destino = "video"

ys = yt.streams.filter(adaptive=True).order_by('resolution').desc().first()

if ys:
    ys.download(output_path=destino)
    print("Download concluído em alta resolução!")
    caminho_atual = titulo
    caminho_novo = r"C:\Users\curso\Downloads\Python\Baixar video com pytubefix\video\video1.mp4"
    os.rename(caminho_atual, caminho_novo)
    print("Vídeo renomeado com sucesso!")
else:
    print("Não foi possível encontrar um stream de vídeo adequado.")


