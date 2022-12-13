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


class select_partition_window:
    def __init__(self):
        print("")
        self.avaliable_device_list = ["sda","sdb","sdc","sde","sdf"]
        if is_a_test == False:
            self.avaliable_device_list = get_avaliable_devices()
    def start(self,window):#https://www.pythontutorial.net/tkinter/tkinter-listbox/
        
        window.title("select device")
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
        partition_frame.place(x=50,y=100,width=200,height=200)
        partition_frame["background"]=background_color
    
        gparted_button = Button(partition_frame,text="gparted",command=open_gparted)
        gparted_button["background"]=background_color
        gparted_button.pack(side=TOP)

        
        list_items = Variable(value=self.avaliable_device_list)
        self.device_list = Listbox(partition_frame,height = 10,width = 20,listvariable=list_items)
        self.device_list.pack(side=TOP)


        #final
        final_frame = Frame(window,borderwidth=0,relief="raised")
        final_frame.place(x=50,y=250,width=200,height=50)
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
        conf.deviceice = self.avaliable_device_list[self.device_list.curselection()[0]]
        install_configs.append(conf)     
window_list.append(select_partition_window())

class select_wm_window:
    def __init__(self):
        print("")
        self.avaliable_wm_list = ["xfce","mate","lxqt","cinnamon","kde"]
    def start(self,window):#https://www.pythontutorial.net/tkinter/tkinter-listbox/
        
        window.title("window manager")
        window.geometry("300x300")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        #warning
        fm = Frame(window,borderwidth=1,relief="raised")
        fm.place(x=10,y=10,width=50,height=50)
        fm["background"]=background_color

        text = Label(fm, text = "select your window manager",background="light blue")
        text.pack(side=TOP)

        #partition frame
        partition_frame = Frame(window,borderwidth=0,relief="raised")
        partition_frame.place(x=50,y=75,width=200,height=200)
        partition_frame["background"]=background_color
    
        

        
        list_items = Variable(value=self.avaliable_wm_list)
        self.wm_list = Listbox(partition_frame,height = 10,width = 20,listvariable=list_items)
        self.wm_list.pack(side=TOP)


        #final
        final_frame = Frame(window,borderwidth=0,relief="raised")
        final_frame.place(x=50,y=250,width=200,height=50)
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
        # "xfce" "mate" "lxqt" "cinnamon" "kde"
        selected_wm = self.avaliable_wm_list[self.wm_list.curselection()[0]]
        print(selected_wm + " was selected")
        if selected_wm == "xfce":
            conf.pakages += ["lightdm","xfce4","xorg"]

        elif selected_wm == "mate":
            conf.pakages += ["lightdm","mate","xorg"]

        elif selected_wm == "lxqt":
            conf.pakages += ["sddm","lxqt","xorg"]

        elif selected_wm == "cinnamon":
            conf.repositorys.append("universe")
            conf.pakages += ["lightdm","cinnamon-desktop-environment","xorg"]

        elif selected_wm == "kde":
            conf.pakages += ["sddm","kde-full","xorg"]
            
        install_configs.append(conf)    
window_list.append(select_wm_window())


class select_kernel_window:
    def __init__(self):
        print("")
        self.avaliable_kernel_list = ["linux-image-generic",]
    def start(self,window):#https://www.pythontutorial.net/tkinter/tkinter-listbox/
        
        window.title("kernel")
        window.geometry("300x300")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        #warning
        fm = Frame(window,borderwidth=1,relief="raised")
        fm.place(x=10,y=10,width=50,height=50)
        fm["background"]=background_color

        text = Label(fm, text = "select your kernel",background="light blue")
        text.pack(side=TOP)

        #partition frame
        partition_frame = Frame(window,borderwidth=0,relief="raised")
        partition_frame.place(x=50,y=75,width=200,height=200)
        partition_frame["background"]=background_color
    
        

        
        list_items = Variable(value=self.avaliable_kernel_list)
        self.kernel_list = Listbox(partition_frame,height = 10,width = 20,listvariable=list_items)
        self.kernel_list.pack(side=TOP)


        #final
        final_frame = Frame(window,borderwidth=0,relief="raised")
        final_frame.place(x=50,y=250,width=200,height=50)
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
        conf.kernel =  self.avaliable_kernel_list[self.kernel_list.curselection()[0]]
        install_configs.append(conf)    
window_list.append(select_kernel_window())



class user_window:
    def __init__(self):
        print("")
    def start(self,window):
        window.title("register")
        window.geometry("300x350")
        window.iconbitmap("@"+os.getcwd()+"/PTIU.xbm")
        window["background"]=background_color

        #user
        fm = Frame(window,relief="raised")
        fm.place(x=10,y=10,width=280,height=275)
        fm["background"]=background_color

        text = Label(fm, text = "register:",background="light blue")
        text.grid(column=0, row=0)

        text_user_name = Label(fm, text = "user:\n",background="light blue")
        text_user_name.grid(column=0, row=1)

        self.input_user_name = Entry(fm, width=50)
        self.input_user_name.grid(column=0, row=2)

        text_password = Label(fm, text = "password:\n",background="light blue")
        text_password.grid(column=0, row=3)

        self.input_password = Entry(fm, width=50)
        self.input_password.config(show="*")
        self.input_password.grid(column=0, row=4)

        text_host_name = Label(fm, text = "host name:\n",background="light blue")
        text_host_name.grid(column=0, row=5)

        self.input_host_name = Entry(fm, width=50)
        self.input_host_name.grid(column=0, row=6)

        #final
        final_frame = Frame(window,borderwidth=0,relief="raised")
        final_frame.place(x=50,y=300,width=200,height=50)
        final_frame["background"]=background_color

        next_button = Button(final_frame,text="next>>",command=next)
        next_button["background"]=background_color
        next_button.pack(side=RIGHT)

        previous_button = Button(final_frame,text="<<previous",command=previous)
        previous_button["background"]=background_color
        previous_button.pack(side=LEFT)

    def ok(self):
        usr = user(self.input_user_name.get(),self.input_password.get(),self.input_host_name.get())
        conf = ins.instalaton_config()
        conf.user =  usr
        install_configs.append(conf) 
window_list.append(user_window())



    
    




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
        conf = ins.instalaton_config()
        conf.pakages.append("network-manager")
        install_configs.append(conf) 
        conf_final = fuse_install_configs(install_configs)
        conf_final.print_info()
        if is_a_test == False:
            conf_final.make_command()
            conf_final.install()
window_list.append(terminal_warning_window())













    




window_list[0].start(window)


window.mainloop()
