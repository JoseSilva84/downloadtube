from cx_Freeze import setup, Executable

executables = [Executable("main.py", icon="tube.ico")]

packages = ["os", "kivymd", "pytubefix", "moviepy", "kivy", "subprocess", "threading"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': ["bg.jpg", "tube.png"]
    },
}

setup(
    name="DownloadeTube",
    options=options,
    version="1.0",
    description="Um sistema para download de vídeos ou áudio do YouTube",
    executables=executables
)