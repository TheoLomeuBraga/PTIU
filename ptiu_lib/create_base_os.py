import os
import shutil
import repositorys as rp

def create_repositorys_file():
    #/mnt/etc/apt/sources.list
    if os.path.isfile("sources.list"):
        os.remove("sources.list")
     
    f = open("sources.list", "w")
    for p in rp.base_repositorys:
        f.write(p+"\n")
    f.close()

def create_network_file():
    shutil.copyfile("/etc/resolv.conf","resolv.conf")

def create_base_os():
    ret = []
    debootstrap_command = "sudo debootstrap --arch=amd64 --variant=minbase focal /mnt https://mirror.leaseweb.com/ubuntu/"
    ret.append(debootstrap_command)
    ret.append("sudo cd /usr/share/debootstrap/scripts && ln -sf gutsy jammy")

    

    create_network_file()
    ret.append("sudo yes | sudo cp -rf ./resolv.conf /mnt/etc/")

    

    create_repositorys_file()
    ret.append("sudo yes | sudo cp -rf ./sources.list /mnt/etc/apt/")

    
    return ret


    

def edit():
    ret = []
    ret.append("genfstab /mnt > /mnt/etc/fstab")
    return ret

def mount_file_system():
    ret = []
    ret.append("sudo mount --bind /dev /mnt/dev")
    ret.append("sudo mount -t proc none /mnt/proc")
    ret.append("sudo mount -t sysfs sys /mnt/sys")
    ret.append("sudo mount -t sysfs sys /mnt/sys")
    #ret.append("sudo chroot /mnt << EOF")
    ret.append("sudo mv command_cr.sh /mnt")
    ret.append("sudo chroot /mnt sh command_cr.sh")
    return ret





def all():
    ret = create_base_os() + edit() + mount_file_system()
    return ret