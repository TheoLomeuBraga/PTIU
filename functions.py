import os
import psutil

#utilitary functions

def disksinfo():
        values = []
        disk_partitions = psutil.disk_partitions(all=False)
        for partition in disk_partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            print(partition.device)
            device = {'device': partition.device,
                      'mountpoint': partition.mountpoint,
                      'fstype': partition.fstype,
                      'opts': partition.opts,
                      'total': usage.total,
                      'used': usage.used,
                      'free': usage.free,
                      'percent': usage.percent
                      }
            values.append(device)
        values = sorted(values, key=lambda device: device['device'])
        return values 




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