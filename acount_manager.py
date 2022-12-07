class user:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.host_name = "HOSTNAME"
    def __init__(self,name,password,host_name):
        self.name = name
        self.password = password
        self.host_name = host_name

def add_user_acount2(name,password,host_name):
    ret = []
    ret.append("sudo useradd " + name)
    ret.append("sudo passwd " + " <<< " + name + ":" + password)
    ret.append("echo " + host_name + " > /etc/hostname")
    return ret

def add_user_acount(usr):
    return add_user_acount2(usr.name,usr.password,usr.host_name)