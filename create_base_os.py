def create_base_os():
    ret = []
    ret.append("sudo debootstrap focal /mnt https://mirror.leaseweb.com/ubuntu/")
    ret.append("sudo cd /usr/share/debootstrap/scripts && ln -sf gutsy jammy")
    return ret

def copy_network_configurations():
    ret = []
    ret.append("sudo cp /etc/network/interfaces /mnt/etc/network/interfaces")
    return ret

def edit():
    ret = []
    ret.append("sudo apt-get install arch-install-scripts")
    ret.append("genfstab /mnt > /mnt/etc/fstab")
    return ret

def mount_file_system_and_chroot():
    ret = []
    ret.append("sudo apt-get install arch-install-scripts")
    ret.append("sudo arch-chroot /mnt")
    ret.append("sudo mount --bind /dev /mnt/dev")
    ret.append("sudo mount -t proc none /mnt/proc")
    ret.append("sudo mount -t sysfs sys /mnt/sys")
    ret.append("sudo chroot /mnt /bin/bash")
    return ret





def all():
    ret = create_base_os() + copy_network_configurations() + edit() + mount_file_system_and_chroot()
    return ret