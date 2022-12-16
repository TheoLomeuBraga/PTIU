import pakages as pk
import repositorys as rp



def install_localization():#uncoment
    ret = []
    ret.append("dpkg-reconfigure tzdata")
    ret.append("dpkg-reconfigure locales")
    return ret


def install_boot_loader(dev):
    ret = []


    


    ret.append("grub-install /dev/"+dev)

    #tests install efi
    ret.append("grub-install --target=x86_64-efi /dev/"+dev+" --force")
    ret.append("grub-install --target=x86_64-efi --efi-directory=/boot /dev/"+dev+" --force")
    ret.append("grub-install --target=x86_64-efi --efi-directory=/boot/EFI /dev/"+dev+" --force")

    #install bios
    ret.append("grub-install --target=i386-pc /dev/"+dev+" --force")
    ret.append("update-grub")
    return ret



def install_base_pakages():
    ret = []
    ret.append("apt-get update")
    ret.append("apt -y dist-upgrade")
    for pak in pk.base_pakages:
        ret.append("apt -y install "+pak)
    #ret.append("apt upgrade")
    return ret

def install_extra_pakages():
    ret = []
    ret.append("apt -y install software-properties-common")
    for repo in rp.extra_repositorys:
        ret.append("add-apt-repository "+repo)
    ret.append("apt update")
    for pak in pk.extra_pakages:
        ret.append("apt -y install "+pak)
    return ret


def all(dev):
    ret = install_base_pakages() + install_extra_pakages() + install_localization() + install_boot_loader(dev)
    return ret