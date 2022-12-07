def install_localization():
    ret = []
    ret.append("dpkg-reconfigure tzdata")
    ret.append("apt-get install locales")
    ret.append("dpkg-reconfigure locales")
    return ret

def install_kernel(kernel_name):#in progerss
    ret = []
    ret.append("apt-get install "+ kernel_name)
    return ret

def install_boot_loader(dev):
    ret = []
    ret.append("apt-get install grub-pc")
    ret.append("apt-get install grub-efi")
    ret.append("grub-install /dev/"+dev)
    ret.append("grub-install /dev/"+dev)
    ret.append("update-grub")
    return ret

def install_extras(pakages):
    ret = []
    for p in pakages:
        ret.append("apt-get install " + p)
    return ret

def all(kernel_name,dev,extra_pakages):
    ret = install_localization() + install_kernel(kernel_name) + install_boot_loader(dev) + install_extras(extra_pakages)
    return ret