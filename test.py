#!/bin/python3
import functions as f
import partition_manager as pmanager
import cmd_manager as cm
import create_base_os as cbos



#nao testar nesse computador
cm.add_cmds(pmanager.create_mount_partitions("sdc",0,1024))
cm.add_cmds(cbos.all())
cm.begin_installation()