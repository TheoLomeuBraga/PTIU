kernel = "linux-image-generic"

base_pakages = [
    "locales",
    "grub-efi",
    "grub-pc",
    "grub-common",
    "grub-pc-bin",
    "grub-efi-amd64-bin",
    kernel,
    "plymouth-x11",
    "xinput",
    "software-properties-common",
    ]

extra_pakages = [
    "universe",
    ]



def add_pakage(pakage):
    global extra_pakages
    extra_pakages.append(pakage)

def add_pakages(pakages):
    global extra_pakages
    extra_pakages = extra_pakages + pakages