### Designed by SHiROU     ###
##  LinkedIn:aliburaksan45 ##
#   YouTube MP3 Indirici   #

from tkinter import END
import pyperclip
from pytube import YouTube
import customtkinter
import tkinter
import os



# Indirme Fonksiyon
def Download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.filter(only_audio=True).first()
        destination = ''
        out_file = video.download(output_path=destination)
        base, ext = os.path.split(out_file)
        new_file = video.title + '.mp3'
        os.rename(out_file,new_file)
        finishLabel.configure(text="Başarıyla İndirildi!")
        title.configure(text=video.title,text_color="black")
        link.delete(0, customtkinter.END)
    except:
        finishLabel.configure(text="Programda hata oluştu!!", text_color="red")


# Uygulama
app = customtkinter.CTk()
app.geometry("480x220")
app.title("YouTube MP3 İndirici")
app.iconbitmap(default='profile.ico')

# Uygulama Tema
customtkinter.set_appearance_mode("gray")
customtkinter.set_default_color_theme("blue")

# Uygulama Başlık
title = customtkinter.CTkLabel(app, text="YouTube MP3 İndirici", font=('Arial', 16, "bold"))
title.pack(padx=10,pady=10)

# Link Girme
url_var = customtkinter.StringVar()
link = customtkinter.CTkEntry(app,width=400)
link.pack(padx=10,pady=10)

# Bildirim
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

# İndirme Butonu
button = customtkinter.CTkButton(app,text="İndir!",command=Download)
button.pack(padx=10,pady=10)


# Uygulama Başlat
app.mainloop()
