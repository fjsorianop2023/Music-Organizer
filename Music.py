import os

class MusicPlaylistOrganizer:
    def __init__(self):
        self.music_files = []

    def scan_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3") or filename.endswith(".wav"):
                self.music_files.append(filename)
        for idx, song in enumerate(self.music_files, start=1):
            print(f"{idx}. {song}")

organizer = MusicPlaylistOrganizer()
folder_path = input("Introduce la ruta de la carpeta con música: ")
organizer.scan_folder(folder_path)
