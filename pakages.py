base_pakages = ["grub","grub-pc","grub-efi","linux-image-generic","locales"]
extra_pakages = []

def add_pakage(pakage):
    extra_pakages.append(pakage)

def add_pakages(pakages):
    extra_pakages = extra_pakages + pakages