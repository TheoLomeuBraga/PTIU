#!/bin/python3
import sys
import os
sys.path.append('../')
from ptiu_lib import *

from tkinter import *


window_id=0
window_list = []
window = Tk()

def next():
    global window_id,window
    window_id += 1
    window.destroy()
    window = Tk()
    window_list[window_id](window)

def previous():
    global window_id,window
    window_id -= 1
    window.destroy()
    window = Tk()
    window_list[window_id](window)


def welcome_window(window):
    global window_id
    window.title("welcome")
    window.geometry("300x100")
    window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
    window["background"]="light blue"

    fm = Frame(window)
    fm["background"]="light blue"
    text = Label(fm, text = "welcome.\n lets mount a ubuntu based distro",background="light blue")
    text.pack(side=TOP)

    next_button = Button(fm,text="next>>",command=next)
    next_button["background"]="light blue"
    next_button.pack(side=BOTTOM)

    fm.pack(fill=BOTH, expand=YES)
window_list.append(welcome_window)












def terminal_warning_window(window):
    global window_id
    window.title("warning")
    window.geometry("300x100")
    window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
    window["background"]="light blue"

    fm = Frame(window,borderwidth=1,relief="raised")
    fm.place(x=10,y=10,width=50,height=50)
    fm["background"]="light blue"

    text = Label(fm, text = "pay attention to the terminal.\npart of the installation will be done on it",background="light blue")
    text.pack(side=TOP)

    fm2 = Frame(window,borderwidth=0,relief="raised")
    fm2.place(x=50,y=50,width=200,height=50)
    fm2["background"]="light blue"

    next_button = Button(fm2,text="next>>",command=next)
    next_button["background"]="light blue"
    next_button.pack(side=RIGHT)

    previous_button = Button(fm2,text="<<previous",command=previous)
    previous_button["background"]="light blue"
    previous_button.pack(side=LEFT)

    fm.pack(fill=BOTH, expand=YES)
    #fm2.pack(fill=BOTH, expand=YES)
window_list.append(terminal_warning_window)



window_list[0](window)


window.mainloop()
