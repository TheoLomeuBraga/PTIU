#pakages

install_pakages_comand = ""

add_repository_comand = ""

update_repository_comand = ""

afirmation_key = ""

def setup(instalation_cmd,add_repo_cmd,update_repo_cmd,yes_key):
    global install_pakages_comand,add_repository_comand,update_repository_comand,afirmation_key
    
    install_pakages_comand = instalation_cmd
    add_repository_comand = add_repo_cmd
    update_repository_comand = update_repo_cmd
    afirmation_key = yes_key

def add_repository(repository):
    ret = []
    ret.append(add_repository_comand + " " + repository  + " <<< " + afirmation_key)
    ret.append(update_repository_comand)

def update_pakage_manager():
    ret = []
    ret.append(update_repository_comand)
    return ret

def install_pakages(pakages):
    ret = []
    command = install_pakages_comand
    for p in pakages:
        command += " " + p
    ret.append(command + " <<< " + afirmation_key)