import os
import subprocess






#variables

installation_commands = []

install_pakages_comand = ""

add_repository_comand = ""

update_repository_comand = ""

afirmation_key = ""



#functions

def separate_file_in_lines(file):
    ret = []
    file1 = open(file, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        ret.append("{1}".format(count, line.strip()))
    return ret

def compare_first_chars(n,s1,s2):
    ret=True
    if len(s1) < n or len(s2) < n:
        ret=False
    else:
        i=0
        while i < n:
            ret = s1[i] == s2[i]
            i+=1

    return ret



#keyboard

def get_keybord_layouts():
    return separate_file_in_lines("layouts/base.txt")

def get_keybord_variant_layouts(layout):
    return separate_file_in_lines("layouts/variants/"+layout+".txt")


#devices

class partition_info:
    def __init__(self):
        self.name = ""
        self.size = 0
        self.mount_point = ""
    def __init__(self,partition_info_list):
        self.name = partition_info_list[0]
        self.size = partition_info_list[3]
        if len(partition_info_list) > 6 :
            self.mount_point = partition_info_list[6]
        else:
            self.mount_point = ""
    def print_info(self):
        print("name: " + self.name + " " + "size: " + self.size + " " + "mount_point: " + self.mount_point," ",)
    
    

class device_info:

    def __init__(self):
        self.name = ""
        self.size = 0
        self.partitions = []

    
    def __init__(self,device_info_list):
        self.name = device_info_list[0][0]
        self.size = device_info_list[0][3]
        self.partitions = []
        device_info_list.pop(0)
        for l in device_info_list:
            self.partitions.append(partition_info(l))

    
    def __init__(self,name,size,partitions):
        self.name = name
        self.size = size
        self.partitions = partitions
    
    def print_info(self):
        print("name: " + self.name + " " + "size: " + self.size)
    

def get_list_all_partitions():
    comand_result = subprocess.check_output(['lsblk', '-l'])
    result_procesed_lines = comand_result.splitlines()
    result_procesed_lines.pop(0)
    
    #remove p''
    result_procesed_lines_procesed = []
    for l in result_procesed_lines:
        result_procesed_lines_procesed.append(str( l, 'utf-8' ))
    
    #separate data
    ret = []
    for l in result_procesed_lines_procesed:
        ret.append(partition_info(l.split()))

    return ret


    ret = []
    devices_str_list = get_list_all_avaliable_devices()

    i = 0
    devices_str_list_2 = []
    devices_str_list_2.append([])
    for l in devices_str_list:
        if l == []:
            devices_str_list_2[i].append([])
            i += 1
        else:
            devices_str_list_2[i].append(l)
            


    
    for l in devices_str_list_2:
        print(l)
    return ret
def separe_partitions_bt_devices():
    ret = []
    partitions = get_list_all_partitions()
    partitions_devices = []
    for p in partitions:
        if len(p.name) == 3 and compare_first_chars(2,"sd",p.name):
            partitions_devices.append(device_info(p.name,p.size,[]))
        else:
            partitions_devices.append(p)

    i = 0
    for p in partitions_devices:
        #if p.__class__.__name__
        print("")

    return ret




    



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





