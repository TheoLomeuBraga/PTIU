import os

cmds = []

def add_cmd(cmd):
    cmds.append(cmd)

def add_cmds(commands):
    global cmds
    cmds += commands

def begin_installation():
    print("begin installation")
    global cmds
    for c in cmds:
        print(c)
        os.system(c)

