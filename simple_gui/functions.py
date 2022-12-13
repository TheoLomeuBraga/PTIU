import sys
import os
from enum import Enum
sys.path.append('../')
from ptiu_lib import *

def open_gparted():
    os.system("sudo gparted")