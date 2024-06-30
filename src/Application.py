import tkinter as tk

class Application:
    def __init__(self, title, width, height, icon=None) -> None:
        #application setting-up
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)

        if icon:
            self.root.iconbitmap(icon)

        #youtube-video-url-input
        self.yt_url_label = tk.Label(self.root, text="Youtube URL:")
        self.yt_url_label.pack(pady=20)

        self.url_entry = tk.Entry(self.root, width=80)
        self.url_entry.pack()

        self.convert_button = tk.Button(self.root, text="Convert Video", command=self.convert_video)
        self.convert_button.pack(pady=10)
    
    def convert_video(self):
        pass

    def run(self):
        self.root.mainloop()