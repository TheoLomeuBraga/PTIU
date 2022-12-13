import sys
sys.path.append('../ptiu_lib')
from enum import Enum

#import ptiu_lib
from ptiu_lib.partition_manager import *
from ptiu_lib.cmd_manager import *
from ptiu_lib.create_base_os import *
from ptiu_lib.acount_manager import *
from ptiu_lib.second_base_os import *
from ptiu_lib.pakages import *
from ptiu_lib.final_configs import *
from ptiu_lib.repositorys import *

class instalaton_config:
    def __init__(self):
        self.device = ""
        self.kernel = ""
        self.user = user("user","password","host")
        self.repositorys = []
        self.pakages = []
        self.final_commands = []
    def install(self):
        print("installing")