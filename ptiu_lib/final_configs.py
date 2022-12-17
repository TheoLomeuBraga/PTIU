
def final_configs(root_name):
    ret = [
        #"dpkg-reconfigure locales",
        #"dpkg-reconfigure keyboard-configuration",
        #"service keyboard-setup restart",
        "apt -y upgrade",
        #configure console
        "chsh -s /bin/bash",
        "chsh -s /bin/bash "+root_name,
        #configure sudo
        "apt -y install sudo",
        "usermod -aG sudo "+root_name,
    ]
    return ret