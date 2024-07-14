import tkinter
import customtkinter
from pytubefix import YouTube
from tkinter import filedialog

def startDownload():
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        
        # Vraag de gebruiker om de downloadlocatie te kiezen
        download_folder = filedialog.askdirectory()
        if download_folder:
            video.download(output_path=download_folder)
            status_label.config(text="Download complete", text_color="green")
        else:
            status_label.config(text="Download cancelled", text_color="red")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", text_color="red")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# The app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert your video link below")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Status label
status_label = customtkinter.CTkLabel(app, text="")
status_label.pack(padx=10, pady=10)

# Run app
app.mainloop()
