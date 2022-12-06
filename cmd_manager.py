import os

cmds = []

def add_cmd(cmd):
    cmds.append(cmd)

def add_cmds(cmds):
    cmds.extend(cmds)

def begin_installation():
    print("begin installation")
    for c in cmds:
        os.system(c)

