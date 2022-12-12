import sys
import os
sys.path.append('../PTIU')
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



window_list[0](window)


window.mainloop()
