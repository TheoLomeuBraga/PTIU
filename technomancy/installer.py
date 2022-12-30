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



def start():
    window_list[0].start(window)
    window.mainloop()


background_color="light blue"



start()