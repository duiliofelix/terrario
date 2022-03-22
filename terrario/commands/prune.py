import os

def prune(_args):
    print('This process will delete the .terraform folders in the live paths.')
    print('Confirm? (y/N)')

    confirm = input()
    if confirm != 'y':
        return

    projects = os.listdir('.')

    for project in projects:
        subpaths = os.listdir(project)
        if 'live' not in subpaths:
            continue

        live_path = os.path.abspath(os.path.join(project, 'live'))
        env_paths = os.listdir(live_path)
        for env_path_name in env_paths:
            env_path = os.path.join(live_path, env_path_name)
            env_subpaths = os.listdir(env_path)

            if '.terraform' in env_subpaths:
                tmp_path = os.path.join(env_path, '.terraform')
                print('Erasing ' + tmp_path)
                os.system('rm -rf ' + tmp_path)
                os.system('rm ' + env_path + '/.terraform.lock.hcl')

