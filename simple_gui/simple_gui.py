import sys
sys.path.append('../PTIU')
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


def instructions_window(window):
    global window_id
    window.title("instructions window")
    window.geometry("300x500")
    fm = Frame(window)
    
    fm.pack(fill=BOTH, expand=YES)
window_list.append(instructions_window)



window_list[0](window)


window.mainloop()
