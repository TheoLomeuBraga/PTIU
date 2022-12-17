import os

cmds = []

def add_cmd(cmd):
    cmds.append(cmd)

def add_cmds(commands):
    global cmds
    cmds = cmds + commands 

cmds_cr = []

def add_cmd_cr(cmd):
    cmds_cr.append(cmd)

def add_cmds_cr(commands):
    global cmds_cr
    cmds_cr = cmds_cr + commands 

def begin_installation():
    print("begin installation")
    global cmds
    if os.path.isfile("command.sh"):
        os.remove("command.sh")
     
    f = open("command.sh", "w")
    for c in cmds:
        f.write(c+"\n")
    f.close()

    global cmds
    if os.path.isfile("command_cr.sh"):
        os.remove("command_cr.sh")
     
    f = open("command_cr.sh", "w")
    for c in cmds_cr:
        f.write(c+"\n")
    f.close()

def install():
    os.system('sudo sh command.sh')
    #chroot /mnt/gentoo myscript.sh
