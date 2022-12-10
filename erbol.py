import tkinter as tk
from tkinter import ttk
from pytube import YouTube
 
 
def Download_Video():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(window, text = 'скачано!', font = 'arial 15',fg="White",bg="#EC7063").place(x= 10 , y = 140)  
 
window = tk.Tk()
window.geometry("600x200")
window.config(bg="#EC7063")
window.resizable(width=False,height=False)
window.title('YouTube')
 
link = tk.StringVar()
tk.Label(window,text = '                   Youtube скачать видео                    ', font ='arial 20 bold',fg="White",bg="Black").pack()
tk.Label(window, text = 'Вставь ссылку:', font = 'arial 20 bold',fg="Black",bg="#EC7063").place(x= 5 , y = 60)
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="lightgreen").place(x = 5, y = 100)
tk.Button(window,text = 'скачать', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=385 ,y = 140) 
window.mainloop()