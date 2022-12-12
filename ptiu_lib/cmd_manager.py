import os

cmds = []



def add_cmd(cmd):
    cmds.append(cmd)

def add_cmds(commands):
    global cmds
    cmds = cmds + commands 

def begin_installation():
    print("begin installation")
    global cmds
    if os.path.isfile("command.sh"):
        os.remove("command.sh")
     
    f = open("command.sh", "w")
    for c in cmds:
        f.write(c+"\n")
    f.close()

def install():
    os.system("sudo sh command.sh")
