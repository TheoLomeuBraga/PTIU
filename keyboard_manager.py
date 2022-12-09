import functions as f

def get_keybord_layouts():
    return f.separate_file_in_lines("layouts/base.txt")

def get_keybord_variant_layouts(layout):
    return f.separate_file_in_lines("layouts/variants/"+layout+".txt")

def set_keyboard(layout):
    ret = []
    ret.append("sudo setxkbmap " + layout)
    return ret

