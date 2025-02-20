from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from moviepy import *
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
import subprocess
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
import time
from threading import Thread

Window.size = (700, 500)  # Define o tamanho da janela

class YouTubeDownloaderApp(MDApp):
    dialog1 = None
    normal_color = [1.00, 0.76, 0.03, 1]
    hover_color = [0.75, 0.85, 0.85, 1]

    def on_mouse_pos(self, window, pos):
        screen = self.screen  # Acessa a tela

        # Lista de botões a serem verificados
        buttons = [self.download_button, self.download_button2]
        
        cursor_set = False  # Inicializa o cursor_set como False

        for button in buttons:
            if button.collide_point(*pos):
                button.md_bg_color = self.hover_color
                Window.set_system_cursor('hand')  # Muda para a mãozinha
                cursor_set = True  # Marca que o cursor foi alterado
            else:
                button.md_bg_color = self.normal_color
        
        # Verifica se nenhum botão foi encontrado sob o cursor
        if not cursor_set:
            Window.set_system_cursor('arrow')  # Volta para o cursor padrão

    def build(self):
        Window.bind(on_mouse_pos=self.on_mouse_pos)
        self.screen = Screen()
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"
        self.icon = "tube.png"
        self.title = "PROGRAMA DOWNLOADTUBE"

        # Adicionar imagem de fundo
        self.background = Image(source="bg.jpg", allow_stretch=True, keep_ratio=False)
        self.screen.add_widget(self.background)

        self.url_input = MDTextField(
            hint_text="                                   Digite o link do YouTube aqui",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint_x=None,
            width=600,
            halign="center"  # Centralizar o texto
        )
        self.screen.add_widget(self.url_input)
        
        self.download_button = MDRaisedButton(
            text="Baixar vídeo",
            pos_hint={"center_x": 0.3, "center_y": 0.6},
            id="download_video",  # Adicionando ID
            on_release=self.funcionamento_botao
        )
        self.screen.add_widget(self.download_button)

        self.download_button2 = MDRaisedButton(
            text="Baixar áudio",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            id="download_audio",  # Adicionando ID
            on_release=self.funcionamento_botao2
        )
        self.screen.add_widget(self.download_button2)
        
        self.download_button3 = MDRaisedButton(
            text="Abrir pasta",
            pos_hint={"center_x": 0.7, "center_y": 0.6},
            id="abrir_pasta",  # Adicionando ID
            on_release=self.abrir_pasta
        )
        self.screen.add_widget(self.download_button3)
        
        self.status_label = MDLabel(
            text="",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.screen.add_widget(self.status_label)

        self.status_label2 = MDLabel(
            text="BAIXAR VÍDEO OU ÁUDIO DO YOUTUBE",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            markup=True,  # Habilitar a marcação para texto em negrito
            font_size="80sp"  # Definir o tamanho da fonte
        )
        self.screen.add_widget(self.status_label2)

        self.status_label3 = MDLabel(
            text="Desenvolvido por: José Evangelista da Silva Filho\nE-mail: juniornyanata@gmail.com",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.05}
        )
        self.screen.add_widget(self.status_label3)

        # Adicionar a barra de progresso
        self.progress_bar = ProgressBar(value=0, max=100, pos_hint={"center_x": 0.5, "center_y": 0.4}, size_hint_x=0.7)
        self.screen.add_widget(self.progress_bar)
        
        return self.screen
    
    def mostrar_dialogo_sucesso1(self):
            if not self.dialog1:
                self.dialog1 = MDDialog(
                    title="Salvo",
                    text="Dawnload feito com sucesso!",
                    buttons=[],
                )
            self.dialog1.open()

    def ponto_continuo(self, *args):
        self.status_label.text += "."
        if self.status_label.text.count('.') > 15:
            self.status_label.text = ""

    def funcionamento_botao(self, instance):
        if self.url_input.text == "":
            toast("Preencha o link do download!")
        else:
            self.status_label.text = "Baixando"
            toast("Iniciando o download!")
            self.event = Clock.schedule_interval(self.ponto_continuo, 0.5)
            Thread(target=self.download_and_merge, args=(instance,)).start()
    
    def funcionamento_botao2(self, instance):
        if self.url_input.text == "":
            toast("Preencha o link do download!")
        else:
            toast("Iniciando o download!")
            self.audio_baixar(instance)
            self.mostrar_dialogo_sucesso1()
    
    def download_and_merge(self, instance):
        url = self.url_input.text

        self.progress_bar.value = 0  # Certifique-se de que a barra de progresso está vazia
        
        # Defina o callback de progresso
        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            self.progress_bar.value = percentage_of_completion

        # Download do vídeo e áudio
        yt = YouTube(url, on_progress_callback=on_progress)
        yt2 = YouTube(url, on_progress_callback=on_progress)
        
        destino_video = "video"
        destino_audio = "audio"
        
        nome_do_video = yt.title

        ys = yt.streams.filter(adaptive=True).order_by("resolution").desc().first()
        ys2 = yt2.streams.get_audio_only()
        
        if ys and ys2:
            baixado_video = ys.download(output_path=destino_video)
            baixado_audio = ys2.download(output_path=destino_audio)
            
            caminho_novo_video = r"video1.mp4"
            caminho_novo_audio = r"audio1.m4a"
            
            os.rename(baixado_video, caminho_novo_video)
            os.rename(baixado_audio, caminho_novo_audio)
            
            # Mescla vídeo e áudio
            video = VideoFileClip(caminho_novo_video)
            audio = AudioFileClip(caminho_novo_audio)
            
            video_com_audio = video.with_audio(audio)
            video_com_audio.write_videofile(f"{nome_do_video}.mp4", codec="libx264", audio_codec="aac")

            os.remove(caminho_novo_video)
            os.remove(caminho_novo_audio)

            self.status_label.text = "Processo de download concluído!"
            self.progress_bar.value = 100  # Certifique-se de que a barra de progresso está completa
            if Clock.unschedule(self.event):
                self.mostrar_dialogo_sucesso1()

            if self.progress_bar.value:
                toast("O download terminou!")

        else:
            self.status_label.text = "Não foi possível encontrar um stream de vídeo adequado."

    def audio_baixar(self, instance):
        url = self.url_input.text

        self.progress_bar.value = 0  # Certifique-se de que a barra de progresso está vazia
        
        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            self.progress_bar.value = percentage_of_completion

        # Download do audio
        yt2 = YouTube(url, on_progress_callback=on_progress)
        
        destino_audio = "audio"
        
        ys2 = yt2.streams.get_audio_only()
        
        if ys2:
            baixado_audio = ys2.download(output_path=destino_audio)
            
            nome_do_audio = yt2.title
            caminho_novo_audio = f"{nome_do_audio}.m4a"
            
            os.rename(baixado_audio, caminho_novo_audio)

            self.progress_bar.value = 100  # Certifique-se de que a barra de progresso está completa

            self.status_label.text = "Download do áudio concluído!"
        else:
            self.status_label.text = "Não foi possível encontrar um stream de áudio adequado."
    
    def abrir_pasta(self, instance):
        destino_video = os.path.abspath("")  # Caminho absoluto da pasta de vídeos

        if os.name == 'nt':  # Windows
            os.startfile(destino_video)
        elif os.name == 'posix':  # Linux, Mac
            subprocess.Popen(['xdg-open', destino_video])
        else:
            toast("Sistema operacional não suportado para abrir pastas automaticamente.")

if __name__ == "__main__":
    YouTubeDownloaderApp().run()