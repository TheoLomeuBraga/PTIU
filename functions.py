import os
import psutil
import pyudev

#utilitary functions

def get_all_devices_names():
    ret = []
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block'):
        ret.append('{0} ({1})'.format(device['DEVNAME'], device['DEVTYPE']))
    return ret

        




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