import functions as func
import subprocess


class partition_info:
    def __init__(self):
        self.name = ""
        self.size = 0
        self.mount_point = ""
    def __init__(self,name,size,mount_point):
        self.name = name
        self.size = size
        self.mount_point = mount_point
    def __init__(self,partition_info_list):
        self.name = partition_info_list[0]
        if len(partition_info_list) > 2 :
            self.size = partition_info_list[3]
        if len(partition_info_list) > 6 :
            self.mount_point = partition_info_list[6]
        else:
            self.mount_point = ""
    def print_info(self):
        print("name: " + self.name + " " + "size: " + self.size + " " + "mount_point: " + self.mount_point," ",)
        
    
    

class device_info:

    def __init__(self):
        self.name = ""
        self.size = 0
        self.partitions = []

    
    def __init__(self,device_info_list):
        self.name = device_info_list[0][0]
        self.size = device_info_list[0][3]
        self.partitions = []
        device_info_list.pop(0)
        for l in device_info_list:
            self.partitions.append(partition_info(l))

    
    def __init__(self,name,size,partitions):
        self.name = name
        self.size = size
        self.partitions = partitions
    
    def print_info(self):
        print("name: " + self.name + " " + "size: " + self.size)
        print("{")
        for p in self.partitions:
            p.print_info()
        print("}")
    #devices



def get_list_all_partitions():
    comand_result = subprocess.check_output(['lsblk', '-l'])
    result_procesed_lines = comand_result.splitlines()
    result_procesed_lines.pop(0)
    
    #remove p''
    result_procesed_lines_procesed = []
    for l in result_procesed_lines:
        result_procesed_lines_procesed.append(str( l, 'utf-8' ))
    
    #separate data
    ret = []
    for l in result_procesed_lines_procesed:
        ret.append(partition_info(l.split()))

    return ret

def compare_first_chars(n,s1,s2):
    ret=True
    if len(s1) < n or len(s2) < n:
        ret=False
    else:
        i=0
        while i < n:
            ret = s1[i] == s2[i]
            i+=1

    return ret

def get_devices():
    ret = []
    partitions = get_list_all_partitions()
    partitions_devices = []
    for p in partitions:
        if len(p.name) == 3 and compare_first_chars(2,"sd",p.name):
            partitions_devices.append(device_info(p.name,p.size,[]))
        else:
            partitions_devices.append(p)

    i = 0
    for p in partitions_devices:
        if p.__class__.__name__ == "device_info":
            i += 1
            ret.append(p)
        else:
            if compare_first_chars(2,p.name,"sd"): 
                ret[i - 1].partitions.append(p)

    return ret




#https://linuxhint.com/linux-parted-command-line-examples/
def create_mount_partitions(dev,home_size_mb,swap_size_mb):
    ret = []
    ret.append("sudo sh create_partition.sh " + dev + " " + str(home_size_mb)  + " " + str(swap_size_mb))
    return ret


def mount_partition():
    ret = []
    ret.append("")
    return ret