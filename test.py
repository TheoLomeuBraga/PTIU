#!/bin/python3
import functions as f
import partition_manager as pmanager
import cmd_manager as cm




cm.add_cmds(pmanager.create_mount_partitions("sdc",f.get_size_in_mb("30GB"),0))
cm.begin_installation()