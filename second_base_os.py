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



def all(dev):
    ret = install_localization() + install_boot_loader(dev) 
    return ret