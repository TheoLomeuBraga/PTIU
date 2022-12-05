import os
import subprocess

#variables

installation_commands = []

install_pakages_comand = ""

add_repository_comand = ""

update_repository_comand = ""

afirmation_key = ""

#classes

class device_info:
    def __init__(self):
        self.size=0
        self.free=0
        self.used=0

#keyboard
def separate_file_in_lines(file):
    ret = []
    file1 = open(file, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        ret.append("{1}".format(count, line.strip()))
    return ret

def get_keybord_layouts():
    return separate_file_in_lines("layouts/base.txt")

def get_keybord_variant_layouts(layout):
    return separate_file_in_lines("layouts/variants/"+layout+".txt")


#devices

def get_all_avaliable_devices():#em andamento 
    comand_result=subprocess.check_output(['lsblk', '-l'])
    #https://codereview.stackexchange.com/questions/152486/parsing-the-lsblk-output







    



#instalation comands

def add_installation_command(command):
    installation_commands.append(command)

def begin_installation():
    print("begin installation")
    for c in installation_commands:
        os.system(c)

#pakages
def add_repository(repository):
    print("add: ",repository)
    add_installation_command(add_repository_comand + " " + repository  + " <<< " + afirmation_key)
    add_installation_command(update_repository_comand)

def install_pakages(pakages):
    command = install_pakages_comand
    for p in pakages:
        command += " " + p
    print(command)
    add_installation_command(command + " <<< " + afirmation_key)

#add user

def add_user_acount(name,password):
    print("creating acount to: ",name)
    os.system("sudo useradd " + name)
    os.system("sudo passwd "+ name + " <<< " + password)



def set_locale(locale):
    print("locale seted to: ",locale)

def set_keyboard_layout(layout):
    print("keyboar layout seted to: ",layout)

def create_base_os(device):
    print("creating base")

def install_boot_loaders():
    print("installing boot loaders")





