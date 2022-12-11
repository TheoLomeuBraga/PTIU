#!/bin/python3
import functions as f
import partition_manager as pmanager
import cmd_manager as cm
import create_base_os as cbos
import acount_manager as am
import second_base_os as sbos
import pakages as pk
import final_configs as fc
import repositorys as rp
import os

user = am.user("user","password","AAAAA")

if os.path.isfile("commands.sh"):
        os.remove("commands.sh")

pk.add_pakages(["network-manager","xfce4","firefox","xorg","lightdm",])

dev = "sdb"
cm.add_cmds(pmanager.create_mount_partitions(dev,0,1024))
cm.add_cmds(cbos.all())
cm.add_cmds(am.add_user_acount(user))
cm.add_cmds(sbos.all(dev))


cm.add_cmds(bi.change_boot_text("made with PTIU"))
#cm.add_cmd("dpkg-reconfigure lightdm")



cm.add_cmds(fc.final_configs(user.name))


cm.begin_installation()