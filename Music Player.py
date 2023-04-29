from tkinter.filedialog import askopenfilename
from tkinter import *
import pygame
import os
file = None
def add():
    file = askopenfilename(defaultextension=".mp3",
                    filetypes=[("MP3", "*.mp3"),
                               ("AAC","*.aac"),
                               ("FLAC","*.flac"),
                               ("WAV","*.wav"),
                               ("OGG","*.ogg"),
                               ("All Files","*.*")])
    
    global current_music
    current_music.insert(0, os.path.basename(file))
    # file = os.path.basename(file)
    print(file)
    pygame.mixer.init()
    pygame.mixer.music.load(f"{file}")
    pygame.mixer.music.set_volume(10)
root = Tk()

root.title("Open Source Music Player")
root.iconbitmap("Music Player.ico")
root.geometry("344x555")
current_music = Listbox(root)
current_music.pack()
Button(root,text="Add Music",command=add).pack()
def add():
    file = askopenfilename(defaultextension=".mp3",
                    filetypes=[("MP3", "*.mp3"),
                               ("AAC","*.aac"),
                               ("FLAC","*.flac"),
                               ("WAV","*.wav"),
                               ("OGG","*.ogg"),
                               ("All Files","*.*")])
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    global current_music
    current_music.insert(ACTIVE, os.path.basename(file))
root.mainloop()