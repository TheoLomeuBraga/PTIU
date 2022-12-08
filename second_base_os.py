import pakages as pk

def conect_to_internet():
    ret = []
    #ret.append('echo "nameserver 8.8.8.8" > /etc/resolv.conf')
    return ret

def install_localization():
    ret = []
    ret.append("dpkg-reconfigure tzdata")
    ret.append("dpkg-reconfigure locales")
    return ret


def install_boot_loader(dev):
    ret = []
    ret.append("grub-install /dev/"+dev)
    ret.append("grub-install --target=x86_64-efi /dev/"+dev+" --force")
    ret.append("grub-install --target=i386-pc /dev/"+dev+" --force")
    ret.append("update-grub")
    return ret



def install_pakages():
    ret = []
    for pak in pk.base_pakages:
        ret.append("sudo apt install "+pak)
    for pak in pk.extra_pakages:
        ret.append("sudo apt install "+pak)
    return ret

def all(dev):
    ret = conect_to_internet() + install_pakages() + install_localization() + install_boot_loader(dev)
    return ret