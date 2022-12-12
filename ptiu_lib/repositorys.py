base_repositorys = [
    "deb http://us.archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse",
    "deb-src http://us.archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse",
    "deb http://us.archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse",
    "deb-src http://us.archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse",
    "deb http://us.archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse",
    "deb-src http://us.archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse",
]
extra_repositorys = []

def add_repository(repository):
    global extra_repositorys
    extra_repositorys.append(repository)

def add_repositorys(repositorys):
    global extra_repositorys
    for r in repositorys:
        add_repository(r)