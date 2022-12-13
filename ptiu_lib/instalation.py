import os

#import ptiu_lib
import partition_manager as pm
import cmd_manager as cm
import create_base_os as cbos
import acount_manager as am
import second_base_os as sbos
import pakages as pk
import final_configs as fc
import repositorys as rp

class instalaton_config:
    def __init__(self):
        self.deviceice = ""
        self.kernel = ""
        self.user = am.user("","","")
        self.repositorys = []
        self.pakages = []
        self.final_commands = []

    def print_info(self):
        print("devices: "+self.deviceice)
        print("kernel: "+self.kernel)
        print("user: "+self.user.name)

        print("repositorys: ")
        print(self.repositorys)

        print("pakages: ")
        print(self.pakages)

        print("final_commands: ")
        print(self.final_commands)

    def __add__(self, other):
        ret = instalaton_config()

        #device
        if other.deviceice == "":
            ret.deviceice = self.deviceice
        else:
            ret.deviceice = other.deviceice
        
        #kernel
        if other.kernel == "":
            ret.kernel = self.kernel
        else:
            ret.kernel = other.kernel
        
        #user
        if other.user == am.user("","",""):
            ret.user = self.user
        else:
            ret.user = other.user

        ret.repositorys = self.repositorys + other.repositorys

        ret.pakages = self.pakages + other.pakages

        ret.final_commands = self.final_commands + other.final_commands

        return ret

    def make_command(self):
        if os.path.isfile("commands.sh"):
            os.remove("commands.sh")

        rp.add_repositorys(self.repositorys)
        pk.add_pakages(self.pakages)
        cm.add_cmds(pm.create_mount_partitions(self.deviceice,0,1024))
        cm.add_cmds(cbos.all())
        cm.add_cmds(am.add_user_acount(self.user))
        cm.add_cmds(sbos.all(self.deviceice))
        cm.add_cmds(fc.final_configs(self.user.name))
        cm.add_cmds(self.final_commands)
        cm.begin_installation()
    def install(self):
        cm.install()