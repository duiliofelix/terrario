import os
from terrario.exceptions import NotGitProjectException

def gotoGitRoot(base_dir = '.'):
    abs = os.path.abspath(base_dir)
    if abs == '/':
        raise NotGitProjectException()

    paths = os.listdir(abs)
   
    if '.git' in paths:
        os.chdir(abs)
    else:
        gotoGitRoot(os.path.join(abs, '..'))

def isInGitProject(base_dir = '.'):
    abs = os.path.abspath(base_dir)
    if abs == '/':
        return False

    paths = os.listdir(abs)
   
    if '.git' in paths:
        return True
    else:
        isInGitProject(os.path.join(abs, '..'))

