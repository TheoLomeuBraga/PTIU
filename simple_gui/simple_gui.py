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
    print("")
window_list.insert(instructions_window)




window.mainloop()
