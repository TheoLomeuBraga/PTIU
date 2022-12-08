def create_base_os(extra_pakages):
    ret = []
    base_pakages = ["grub","grub-pc","grub-efi","linux-image-generic","locales"]
    pakages = extra_pakages + base_pakages
    debootstrap_command = "sudo debootstrap --include="
    for p in base_pakages:
        debootstrap_command += p + ","
    debootstrap_command += "focal /mnt https://mirror.leaseweb.com/ubuntu/"
    ret.append(debootstrap_command)
    ret.append("sudo cd /usr/share/debootstrap/scripts && ln -sf gutsy jammy")
    return ret


def edit():
    ret = []
    ret.append("sudo apt-get install arch-install-scripts")
    ret.append("genfstab /mnt > /mnt/etc/fstab")
    return ret

def mount_file_system_and_chroot():
    ret = []
    ret.append("sudo apt-get install arch-install-scripts")
    ret.append("sudo arch-chroot /mnt << EOF")
    ret.append("sudo mount --bind /dev /mnt/dev")
    ret.append("sudo mount -t proc none /mnt/proc")
    ret.append("sudo mount -t sysfs sys /mnt/sys")
    ret.append("exit")
    ret.append("EOF")
    ret.append("sudo chroot /mnt /bin/bash  << EOF")
    return ret





def all(extra_pakages):
    ret = create_base_os(extra_pakages) + edit() + mount_file_system_and_chroot()
    return ret