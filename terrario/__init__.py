import sys
import argparse
from .commands import init, validate, prune

def run():
    parser = argparse.ArgumentParser(
        description='Terraform auxiliary tool',
        prog='terrario',
    )
    subparsers = parser.add_subparsers(
        metavar='command',
        dest='command',
    )
    
    init_parser = subparsers.add_parser('init', help='init help')
    init_parser.add_argument('name', help='new project name')

    validate_parser = subparsers.add_parser('validate', help='validate help')
    validate_parser.add_argument('-e', '--env', help='env to validate')
    
    prune_parser = subparsers.add_parser('prune', help='prune help')
    
    arguments = parser.parse_args(sys.argv[1:])
    if arguments.command == 'init':
        init(arguments)
    elif arguments.command == 'validate':
        validate(arguments)
    elif arguments.command == 'prune':
        prune(arguments)

