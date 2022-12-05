def separate_file_in_lines(file):
    ret = []
    file1 = open(file, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        ret.append("{1}".format(count, line.strip()))
    return ret

def compare_first_chars(n,s1,s2):
    ret=True
    if len(s1) < n or len(s2) < n:
        ret=False
    else:
        i=0
        while i < n:
            ret = s1[i] == s2[i]
            i+=1

    return ret










    









def set_locale(locale):
    print("locale seted to: ",locale)

def set_keyboard_layout(layout):
    print("keyboar layout seted to: ",layout)

def create_base_os(device):
    print("creating base")

def install_boot_loaders():
    print("installing boot loaders")





