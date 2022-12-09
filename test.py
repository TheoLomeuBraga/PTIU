#!/bin/python3
import functions as f
import partition_manager as pmanager
import cmd_manager as cm
import create_base_os as cbos
import acount_manager as am
import second_base_os as sbos
import pakages as pk
import os

if os.path.isfile("commands.sh"):
        os.remove("commands.sh")

pk.add_pakages(["network-manager","xfce4","firefox","slim","xorg"])

#nao testar nesse computador
dev = "sdb"
cm.add_cmds(pmanager.create_mount_partitions(dev,0,1024))
cm.add_cmds(cbos.all())
cm.add_cmds(am.add_user_acount(am.user("user","password","AAAAA")))
cm.add_cmds(sbos.all(dev))
cm.add_cmds(sbos.all(dev))
cm.add_cmd("dpkg-reconfigure slim")


cm.begin_installation()