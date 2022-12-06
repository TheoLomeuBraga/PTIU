#!/bin/python3
import functions as f
import partition_manager as pmanager
import cmd_manager as cm


cm.cmds.extend(pmanager.create_partitions_commands("/dev/sdc"))
cm.begin_installation()