from tkinter import *
import customtkinter as ctk
from pytube import YouTube
import os 
import tkinter.messagebox
import  webbrowser
from PIL import Image,ImageTk

def temp_text(e):
    entry_link.delete(0,"end")
def get_video_title(video_url):
    try:
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Error: {e}")
        return ""
    
#Window
main_ctk = tkinter.Tk()
main_ctk.geometry("400x300")
main_ctk.title("YourLoader"),
main_ctk.configure(background= "grey")
main_ctk.resizable(False, False)

#Entry
entry_link = ctk.CTkEntry(master = main_ctk, 
                          width= 390, 
                          height= 30, 
                          corner_radius= 80,
                           fg_color="#C1C1CD")
entry_link.place(x = 5, 
                 y = 250)
entry_link.insert(0,
                   "Please insert the YouTube video link here.")
entry_link.bind("<FocusIn>",
                 temp_text)
#Download function
def video_downloader(video_url, download_path):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video_stream.download(download_path)
        tkinter.messagebox.showinfo(title="YouLoader", message="Download completed")
    except Exception as e:
        print(f"Error: {e}")
download_path = r'C:\Users\PC\Downloads' 
def download_button_click():
    video_url = entry_link.get()
    download_path = r'C:\Users\PC\Downloads' 
    video_downloader(video_url, download_path)

    # Obtém o título do vídeo e atualiza a label
    video_title = get_video_title(video_url)
    title_label.configure(text=f"Título do vídeo:{video_title}")
video_url = entry_link.get()
#Image layer
my_image = ctk.CTkImage(light_image=Image.open("images\logo-yourloader.png"))
img = Image.open("images\logo-yourloader.png")
img1 = img.resize((210, 150), Image.ANTIALIAS)
corret_image = ImageTk.PhotoImage(img1)
image_label = ctk.CTkLabel(master = main_ctk,
                            image = corret_image,
                            text= "")
image_label.place(x= 150, y= 100)
#YourLoader Label
loader_label = ctk.CTkLabel(master= main_ctk, 
                            text= "YourLoader",
                            width= 45 , 
                            height=10, 
                            font= ("Courier", 55, "underline"),
                            text_color= "black", 
                            corner_radius= 9)
loader_label.place(x= 32, y = 10)


#Help Button/redirect read.me
tab = ""
def help_button():
    webbrowser.open_new_tab(tab)


help_button1 = ctk.CTkButton(master= main_ctk,
                        fg_color="transparent", 
                          width= 20,
                            height=10,
                              text = "Help",
                                command=help_button)
help_button1.place(x= 365, y=5)
#Title Label
title_label = ctk.CTkLabel(master = main_ctk,
                            text="", 
                            font=("Helvetica", 13))
title_label.place(x= 50, y = 80)

#Button
downloader_button = ctk.CTkButton(master = main_ctk, 
                                  width= 100,
                                  height= 30,
                                  corner_radius= 15,
                                  text= "Download now!", font = ("Roman", 15),
                                  fg_color= "#4848D1",
                                  command= download_button_click
                                  )
downloader_button.place(x = 262, y= 210)

main_ctk.mainloop()