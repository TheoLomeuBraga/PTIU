def create_base_os():
    ret = []
    ret.append("sudo debootstrap RELEASE /mnt http://archive.ubuntu.com/ubuntu")
    ret.append("cd /usr/share/debootstrap/scripts && ln -sf gutsy jammy")
    ret.append("sudo cp /etc/network/interfaces /mnt/etc/network/interfaces")
    return ret

def edit():
    ret = []
    ret.append("sudo apt-get install arch-install-scripts")
    ret.append("genfstab /mnt > /mnt/etc/fstab")
    return ret

def mount_file_system():
    print("")

def chroot():
    print("")

def all():
    ret = create_base_os() + edit() + mount_file_system() + chroot()
    return ret