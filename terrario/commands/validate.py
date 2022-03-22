import os, sys
from terrario.services.project import gotoGitRoot

def validate(args):
    try:
        gotoGitRoot()
    except NotGitProjectException:
        print('Not in a git project!')
        return

    live_path = os.path.abspath('./live')

    if args.env:
        env_path = os.path.join(live_path, args.env)
        validate_env(env_path)
        return

    env_paths = os.listdir(live_path)
    for env_path_name in env_paths:
        env_path = os.path.join(live_path, env_path_name)
        validate_env(env_path)

def validate_env(env_path):
    os.chdir(env_path)
    os.system('terraform init --backend=false')

    validate_status = os.system('terraform validate')
    if validate_status > 0:
        sys.exit(validate_status)

