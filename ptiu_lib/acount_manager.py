import repositorys as rp

class user:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.host_name = ""
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.host_name = "8080"
    def __init__(self,name,password,host_name):
        self.name = name
        self.password = password
        self.host_name = host_name

def add_user_acount2(name,password,host_name):
    ret = []

    ret += rp.base_repositorys

    ret.append("useradd -m -d /home/" + name + " " + name)

    ret.append('echo "'+name+':'+password+'" | chpasswd')
    ret.append("echo " + host_name + " > /etc/hostname")

    #ret.append("mkdir /home/" + name)
    #ret.append("chowm " + name + ":"+ name + " /home/"+name)

    return ret

def add_user_acount(usr):
    return add_user_acount2(usr.name,usr.password,usr.host_name)

