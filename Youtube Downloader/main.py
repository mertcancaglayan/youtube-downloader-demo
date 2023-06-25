from tkinter import *
from tkinter.font import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import pytube
import os

# Path Choosing

def select_directory():
    path_select = filedialog.askdirectory()
    path_label.config(text=path_select)

#Download Fuction

def download_file():

    link = link_field.get()
    url = pytube.YouTube(link)
    folder = path_label.cget('text')
    form = cmb.get()

    if form == '.mp3':
        mp3 = url.streams.filter(only_audio=True).first()
        output = mp3.download(folder)
        base, ext = os.path.splitext(output)
        to_mp3 = base + '.mp3'
        os.rename(output,to_mp3)
    elif form == '.mp4':
        mp4 = url.streams.get_highest_resolution().download(folder)



screen = Tk()
#title image
screen.iconbitmap('/Youtube Downloader/youtube.ico') #add your image path
title = screen.title('Youtube Downloader')

canvas = Canvas(screen, width=500,height=500)
canvas.pack()

#open image
yt_logo = Image.open('/Youtube Downloader/youtubelogo.png') #add your image path

#resize image
resized = yt_logo.resize((200,140), Image.ANTIALIAS)

nyt_logo = ImageTk.PhotoImage(resized)

canvas.create_image(250,0,anchor='n',image=nyt_logo)
screen.resizable(width=False, height=False)
canvas.pack()

link_field = Entry(screen,width=50)
link_label = Label(screen,text='Youtube URL:',font=('Helvetica',12,BOLD),fg='#8c0a28')

# Url windows
canvas.create_window(250,175,window=link_field)
canvas.create_window(250,150,window=link_label)


# Path Button

path_button = Button(screen,text='Choose path', fg='white', bg='red', command=select_directory)
path_label = Label(screen,text='...',font=('Helvetica',8,BOLD),fg='green')
canvas.create_window(250,220,window=path_button )
canvas.create_window(250,250,window=path_label )

# Extansion

settings = [
    '.mp3',
    '.mp4'
]

cmb = ttk.Combobox(screen, value= settings, width=10)
canvas.create_window(140,220,window=cmb)
#cmb label
cmb_label = Label(screen,text='Choose format:',font=('Helvetica',10),fg='black')
canvas.create_window(50,220,window=cmb_label)

#download button
download_button = Button(screen,text='Download', fg='white', bg='red',command=download_file)
canvas.create_window(250,350,window=download_button )

#rename entry not added yet
"""rename_field = Entry(screen,width=20)
canvas.create_window(200,300, window=rename_field)
"""
#rename label not added yet
"""rename_label = Label(screen,text='Rename your file:',font=('Helvetica',10),fg='black')
canvas.create_window(70,300,window=rename_label)"""




screen.mainloop()