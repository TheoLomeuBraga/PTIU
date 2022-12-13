import sys
import os
from enum import Enum

sys.path.append('../')
#from ptiu_lib import *

sys.path.append('../ptiu_lib')
import ptiu_lib.instalation as ins
import ptiu_lib.partition_manager as pm
import ptiu_lib.acount_manager as am

def open_gparted():
    os.system("sudo gparted")


def fuse_install_configs(install_configs):
    ret = ins.instalaton_config()
    for c in install_configs:
        ret = ret + c
    return ret
    #install_config.install()

def get_avaliable_devices():
    ret = []
    devs = pm.get_devices()
    for p in devs:
        if len(p.partitions) == 0:
            ret.append(p.name)
    return ret

def user(user,password,host_name):
    return am.user(user,password,host_name)