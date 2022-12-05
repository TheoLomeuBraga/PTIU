#!/bin/python3
import functions as f
import partition_manager as pmansger

for d in pmansger.get_devices():
    d.print_info()
