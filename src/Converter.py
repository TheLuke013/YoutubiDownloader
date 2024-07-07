from pytube import YouTube
from tkinter import messagebox
import os

class Converter:
    def __init__(self, output_path, progress_callback) -> None:
        self.output_path = output_path
        self.progress_callback = progress_callback

    def get_available_resolutions(self, url):
        try:
            yt = YouTube(url)
            streams = yt.streams.filter(file_extension='mp4')
            resolutions = []
            for stream in streams:
                if stream.resolution and stream.resolution not in resolutions:
                    resolutions.append(stream.resolution)
            return resolutions
        except Exception as e:
            print(f"Error getting resolutions: {e}")
            return []

    def download_video(self, url, resolution=None, output_path=None):
        try:
            if not output_path:
                output_path = self.output_path

            yt = YouTube(url, on_progress_callback=self.progress_callback)
            if resolution:
                stream = yt.streams.filter(progressive=False, file_extension='mp4', resolution=resolution.split()[0]).first()
            else:
                stream = yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()

            if stream:
                stream.download(output_path)
                messagebox.showinfo("Download Complete", f"Video downloaded successfully to {output_path}")
            else:
                messagebox.showerror("Error", "No stream available with the selected resolution.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def download_audio(self, url, output_path=None):
        try:
            if not output_path:
                output_path = self.output_path

            yt = YouTube(url, on_progress_callback=self.progress_callback)
            stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

            if stream:
                out_file = stream.download(output_path)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                messagebox.showinfo("Download Complete", f"Audio downloaded successfully to {output_path}")
            else:
                messagebox.showerror("Error", "No audio stream available.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")