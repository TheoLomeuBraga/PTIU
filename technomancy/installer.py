#!/bin/python3

import os
from tkinter import *

import sys
sys.path.append('../')
sys.path.append('../ptiu_lib')
for p in sys.path:
    print(p)
import ptiu_lib.instalation as ins
import ptiu_lib.partition_manager as pm

install_configs = []

window_id=0
window_list = []

window = Tk()

is_a_test = False

args = []
if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        args.append(arg)

for a in args:
    if a == "test":
        is_a_test = True

def next():
    global window_id,window
    window_list[window_id].ok()
    window_id += 1
    window.destroy()
    window = Tk()
    window_list[window_id].start(window)

def previous():
    global window_id,window
    window_id -= 1
    window.destroy()
    window = Tk()
    window_list[window_id].start(window)
    install_configs.pop()

def reload():
    global window_id,window
    window.destroy()
    window = Tk()
    window_list[window_id].start(window)
    install_configs.pop()


def start():
    window_list[0].start(window)
    window.mainloop()

text_color="white"
background_color="dark blue"
button_color="light blue"

def config_frame_color(fm):
    fm["background"]=background_color


def config_text_color(lable):
    lable.config(fg=text_color)
    #lable.config(bg="yellow")
    lable.config(background=background_color)

def config_button_color(lable):
    lable.config(fg=background_color)
    
    lable.config(background=button_color)

class welcome_window:
    def __init__(self):
        print("")
    def start(self,window):
        window.title("welcome")
        window.geometry("300x100")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        

        fm = Frame(window)
        config_frame_color(fm)
        text = Label(fm, text = "welcome.\n lets install technomancy",background=background_color)
        config_text_color(text)
        text.pack(side=TOP)

        next_button = Button(fm,text="next>>",command=next,borderwidth=0)
        config_button_color(next_button)
        next_button.pack(side=BOTTOM)

        fm.pack(fill=BOTH, expand=YES)
    def ok(self):
        conf = ins.instalaton_config()
        install_configs.append(conf)
window_list.append(welcome_window())

class device_selection_window:
    def __init__(self):
        print("")
    def start(self,window):
        window.title("device selection window")
        window.geometry("300x100")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        

        fm = Frame(window)
        config_frame_color(fm)
        text = Label(fm, text = "welcome.\n lets install technomancy",background=background_color)
        config_text_color(text)
        text.pack(side=TOP)

        next_button = Button(fm,text="next>>",command=next)
        config_text_color(next_button)
        next_button.pack(side=BOTTOM)

        fm.pack(fill=BOTH, expand=YES)
    def ok(self):
        conf = ins.instalaton_config()
        install_configs.append(conf)
window_list.append(device_selection_window())




start()