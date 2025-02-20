import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base, icon="tube.ico")]

packages = ["os", "kivymd", "pytubefix", "moviepy", "kivy", "subprocess", "threading"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': ["bg.jpg", "tube.png"]
    },
}

setup(
    name="YouTubeDownloaderApp",
    options=options,
    version="1.0",
    description='An app to download YouTube videos and audios',
    executables=executables
)