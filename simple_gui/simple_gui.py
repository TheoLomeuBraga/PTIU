#!/bin/python3

import os
from enum import Enum

from functions import *
from tkinter import *

import sys
sys.path.append('../ptiu_lib')
import ptiu_lib.instalation as ins
import ptiu_lib.partition_manager as pm

install_configs = []

window_id=0
window_list = []

window = Tk()

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







background_color="light blue"

class welcome_window:
    def __init__(self):
        print("")
    def start(self,window):
        window.title("welcome")
        window.geometry("300x100")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        

        fm = Frame(window)
        fm["background"]=background_color
        text = Label(fm, text = "welcome.\n lets mount a ubuntu based distro",background="light blue")
        text.pack(side=TOP)

        next_button = Button(fm,text="next>>",command=next)
        next_button["background"]=background_color
        next_button.pack(side=BOTTOM)

        fm.pack(fill=BOTH, expand=YES)
    def ok(self):
        conf = ins.instalaton_config()
        install_configs.append(conf)
window_list.append(welcome_window())


class select_partition_window():
    def __init__(self):
        print("")
        #self.avaliable_device_list = get_avaliable_devices()
    def start(self,window):
        
        window.title("warning")
        window.geometry("300x300")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        #warning
        fm = Frame(window,borderwidth=1,relief="raised")
        fm.place(x=10,y=10,width=50,height=50)
        fm["background"]=background_color

        text = Label(fm, text = "to proceed with the installation you must:\n select a device without partitions",background="light blue")
        text.pack(side=TOP)

        #partition frame
        partition_frame = Frame(window,borderwidth=0,relief="raised")
        partition_frame.place(x=50,y=75,width=200,height=200)
        partition_frame["background"]=background_color
    
        gparted_button = Button(partition_frame,text="gparted",command=open_gparted)
        gparted_button["background"]=background_color
        gparted_button.pack(side=TOP)

        #instructions = Label(partition_frame, text = "ex: sda, sdb, sdc",background="light blue")
        #instructions.pack(side=TOP)

        #self.inputtxt = Text(partition_frame,height = 5,width = 20)
        #self.inputtxt.pack(side=TOP)

        

        self.device_list = Listbox(partition_frame,height = 20,width = 10)
        self.device_list.pack(side=TOP)


        #final
        final_frame = Frame(window,borderwidth=0,relief="raised")
        final_frame.place(x=50,y=175,width=200,height=150)
        final_frame["background"]=background_color

        next_button = Button(final_frame,text="next>>",command=next)
        next_button["background"]=background_color
        next_button.pack(side=RIGHT)

        previous_button = Button(final_frame,text="<<previous",command=previous)
        previous_button["background"]=background_color
        previous_button.pack(side=LEFT)

        fm.pack(fill=BOTH, expand=YES)
    def ok(self):
        conf = ins.instalaton_config()
        #conf.deviceice = self.inputtxt.get(1.0, "end-1c")
        install_configs.append(conf)
        
window_list.append(select_partition_window())


class terminal_warning_window:
    def __init__(self):
        print("")
    def start(self,window):
        window.title("warning")
        window.geometry("300x100")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        fm = Frame(window,borderwidth=1,relief="raised")
        fm.place(x=10,y=10,width=50,height=50)
        fm["background"]=background_color

        text = Label(fm, text = "pay attention to the terminal.\npart of the installation will be done on it",background="light blue")
        text.pack(side=TOP)

        final_frame = Frame(window,borderwidth=0,relief="raised")
        final_frame.place(x=50,y=50,width=200,height=50)
        final_frame["background"]=background_color

        next_button = Button(final_frame,text="next>>",command=next)
        next_button["background"]=background_color
        next_button.pack(side=RIGHT)

        previous_button = Button(final_frame,text="<<previous",command=previous)
        previous_button["background"]=background_color
        previous_button.pack(side=LEFT)

        fm.pack(fill=BOTH, expand=YES)
    def ok(self):
        print("")
window_list.append(terminal_warning_window())













    




window_list[0].start(window)


window.mainloop()
