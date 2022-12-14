#!/bin/python3
import partition_manager as pmanager
import cmd_manager as cm
import create_base_os as cbos
import acount_manager as am
import second_base_os as sbos
import pakages as pk
import final_configs as fc
import repositorys as rp
import instalation as ins
import os

ins_config = ins.instalaton_config()

ins_config.user = am.user("user","password","8080")

ins_config.kernel = "linux-image-generic"

ins_config.deviceice = "sdb"

ins_config.repositorys = ["universe","ppa:kisak/kisak-mesa"]

ins_config.pakages = ["network-manager","firefox","xorg","lightdm","xfce4","xfce4-indicator-plugin","xfce4-battery-plugin"]

ins_config.make_command()
ins_config.install()