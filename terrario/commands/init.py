import os
from terrario.services.project import isInGitProject

def init(args):
    if isInGitProject():
        print('Already in a git project!')
        return

    print('Type the env names (comma separated):')
    envs = input().split(',')

    name = args.name
    live_path = os.path.join(name, 'live')
    modules_path = os.path.join(name, 'modules')

    os.mkdir(name)
    os.mkdir(live_path)
    os.mkdir(modules_path)
    for env in envs:
        env_path = os.path.join(live_path, env)
        os.mkdir(env_path)
        os.system('touch ' + env_path + '/main.tf')
        os.system('touch ' + env_path + '/variables.tf')
        os.system('touch ' + env_path + '/terraform.auto.tfvars')
 
    os.chdir(name)
    os.system('touch README.md')
    os.system('touch .gitignore')
    os.system('git init')

