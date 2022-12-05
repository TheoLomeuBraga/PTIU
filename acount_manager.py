class user:
    def __init__(self,name,password):
        self.name = name
        self.password = password

def add_user_acount(name,password):
    ret = []
    ret.append("sudo useradd " + name)
    ret.append("sudo passwd "+ name + " <<< " + password)
    return ret

def add_user_acount(usr):
    return add_user_acount(usr.name,usr.password)