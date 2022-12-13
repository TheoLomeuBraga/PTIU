import sys
import os
from enum import Enum
sys.path.append('../')
from ptiu_lib import *

sys.path.append('../ptiu_lib')
import ptiu_lib.instalation as ins
import ptiu_lib.partition_manager as pm

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
    parts = pm.get_devices()
    for p in parts:
        if len(p.partitions) == 0:
            ret.append(p.name)
    return ret