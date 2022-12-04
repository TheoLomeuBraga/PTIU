import os
import psutil
import pyudev

#utilitary functions

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

def get_all_devices_partitions():
    ret = []
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block'):
        device_info = ('{0} ({1})'.format(device['DEVNAME'], device['DEVTYPE'])).split()
        ret.append(device_info[0])
    return ret

def get_all_devices_avaliable_partitions():
    all_devices = []
    all_devices = get_all_devices_partitions()


#instalation functions

commands = []

def set_locale(locale):
    print("locale seted to: ",locale)

def set_keyboard_layout(layout):
    print("keyboar layout seted to: ",layout)

def create_base_os(device):
    print("creating base")

def create_user_acount(name,password):
    print("creating acount to: ",name)

def install_boot_loaders():
    print("installing boot loaders")

def installing_additional_pakages(pakages):
    print("installing additional pakages")

def begin_installation():
    print("begin installation")
    for c in commands:
        os.system(c)