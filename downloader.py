from tkinter import *
import youtube_dl

root = Tk(className ="Svenos MP3 Downloader")
enter_url = Label(root,text="Enter the Youtube-URL of the music video:") # add a label to root window
enter_url.grid(row=0, column=0)
url = StringVar() # defines the widget state as string
url_widget = Entry(root,textvariable=url) # adds a textarea widget
url_widget.grid(row=0, column=1)
enter_name = Label(root, text="Enter the name of the song:")
enter_name.grid(row=1, column=0)
name = StringVar() # defines the widget state as string
name_widget = Entry(root,textvariable=name) # adds a textarea widget
name_widget.grid(row=1, column=1)

def act():
    youtube_url =  url.get()
    file_name = name.get()
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # only keep the audio
        'audioformat': "mp3",  # convert to mp3
        'outtmpl': "music/" +file_name + ".mp3",  # name the file the ID of the video
        'noplaylist': True,  # only download single song, not playlist
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([youtube_url])

def download(youtube_url):
    try:
        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,  # only keep the audio
            'audioformat': "mp3",  # convert to mp3
            'outtmpl': '%(id)s',  # name the file the ID of the video
            'noplaylist': True,  # only download single song, not playlist
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([youtube_url])
    except:
        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,  # only keep the audio
            'audioformat': "m4a",  # convert to m4a
            'outtmpl': '%(id)s',  # name the file the ID of the video
            'noplaylist': True,  # only download single song, not playlist
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([youtube_url])


download_button = Button(root,text="Download MP3", command=act)
download_button.grid(row=2, column=1)
root.mainloop()
