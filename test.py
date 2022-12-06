#!/bin/python3
import functions as f
import partition_manager as pmanager
import cmd_manager as cm


cm.add_cmds(pmanager.create_partitions_commands("sdc",False))
cm.begin_installation()