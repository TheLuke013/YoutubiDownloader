import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from Converter import Converter
import threading

class Application:
    def __init__(self, title, width, height, icon=None) -> None:
        #application setting-up
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        self.dir_path = ""
        self.icon = icon

        if icon:
            self.root.iconbitmap(icon)

        #youtube url label
        self.yt_url_label = tk.Label(self.root, text="Enter YouTube Video URL:")
        self.yt_url_label.pack(pady=20)

        #url user input
        self.url_entry = tk.Entry(self.root, width=80)
        self.url_entry.pack()

        #button to choose output dir
        self.choose_dir_button = tk.Button(self.root, text="Choose Output Directory", command=self.choose_output_dir)
        self.choose_dir_button.pack()

        #button to convert video
        self.convert_button = tk.Button(self.root, text="Download Video", command=self.show_resolution_options)
        self.convert_button.pack(pady=10)

        #label to display output directory chosen
        self.dir_label = tk.Label(self.root, text="")
        self.dir_label.pack(pady=10)

        #progress bar from downloading video
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.progress.pack()

        self.resolution_var = tk.StringVar()
        self.resolution_var.set("Select Resolution")
        self.resolution_label = tk.Label(self.root, textvariable=self.resolution_var)
        self.resolution_label.pack(pady=10)
    
    def show_resolution_options(self):
        url = self.url_entry.get()
        dir = self.dir_label.cget("text")

        if url and "Output Path" in dir:
            converter = Converter(self.dir_path, self.show_progress)
            resolutions = converter.get_available_resolutions(url)
            self.show_resolution_dialog(resolutions, converter)
        else:
            messagebox.showwarning("Warning", "You need to choose the Output Path and provide a valid URL.")

    def show_resolution_dialog(self, resolutions, converter):
        resolution_dialog = tk.Toplevel(self.root)
        resolution_dialog.title("Choose Resolution")
        resolution_dialog.resizable(False, False)
        resolution_dialog.wm_iconbitmap(self.icon)

        label = tk.Label(resolution_dialog, text="Select Resolution:")
        label.pack(pady=10)

        resolution_listbox = tk.Listbox(resolution_dialog, selectmode=tk.SINGLE)
        resolution_listbox.pack()

        for resolution in resolutions:
            resolution_listbox.insert(tk.END, resolution)

        select_button = tk.Button(resolution_dialog, text="Download", command=lambda: self.start_download_with_resolution(resolution_listbox, converter, resolution_dialog))
        select_button.pack(pady=10)

    def start_download_with_resolution(self, resolution_listbox, converter, resolution_dialog):
        selected_index = resolution_listbox.curselection()
        if selected_index:
            selected_resolution = resolution_listbox.get(selected_index[0])
            self.resolution_var.set(f"Selected Resolution: {selected_resolution}")

            url = self.url_entry.get()
            if url:
                converter.download_video(url, selected_resolution, self.dir_path)
                resolution_dialog.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter a valid YouTube URL.")
        else:
            messagebox.showwarning("Warning", "Please select a resolution.")

    def show_progress(self, stream, chunk, remaining_bytes):
        total_size = stream.filesize
        bytes_downloaded = total_size - remaining_bytes
        progress = (bytes_downloaded / total_size) * 100
        self.progress['value'] = progress

    def choose_output_dir(self):
        dir = filedialog.askdirectory()
        if dir:
            self.dir_path = dir
            self.dir_label.config(text=f"Output Path: {dir}")
        else:
            self.dir_label.config(text="No directory chosen.")

    def run(self):
        self.root.mainloop()