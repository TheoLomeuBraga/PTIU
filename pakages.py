base_pakages = ["grub-efi","grub-pc","grub-common","grub-pc-bin","grub-efi-amd64-bin","linux-image-generic","locales"]
extra_pakages = []

def add_pakage(pakage):
    global extra_pakages
    extra_pakages.append(pakage)

def add_pakages(pakages):
    global extra_pakages
    extra_pakages = extra_pakages + pakages