import sys
import argparse
from tools import pip
from tools import apt
from tools import git


def main():
  args = parse_prog_args()
  
  if args.ifile is not None:
    pass
  
  tool_picker(args)

def tool_picker(args):
    if args.tool == 'pip':
      pip.handle(args)
    elif args.tool == 'apt':
      apt.handle(args)
    elif args.tool == 'git':
      git.handle(args)
    else:
      print('How did you manage this?!', args.tool)
      sys.exit(2)
  
def parse_prog_args():
  """
  This function will take a list of command line arguments given by the user
  and will format them such that the program can use them in decision making
  for what functions to use on the given input.for
  
  Params: None
  Return: argparse.Namespace() instance
  """
  cli_arg_parser = argparse.ArgumentParser(description='Process command line arguments.')
  cli_arg_parser.set_defaults(method=None, pkg=None, verbose=False, ifile=None, ofile=None)
  
  tool_parser = cli_arg_parser.add_subparsers(title='tool')
  pip_parser = tool_parser.add_parser('pip')
  pip_parser.add_argument('-m', choices=['install', 'remove', 'show'], dest='method', required=True)
  pip_parser.add_argument('pkg')
  pip_parser.set_defaults(tool='pip')

  apt_parser = tool_parser.add_parser('apt')
  apt_parser.add_argument('-m', choices=['install', 'remove'], dest='method', required=True)
  apt_parser.add_argument('pkg')
  apt_parser.set_defaults(tool='apt')
  
  git_parser = tool_parser.add_parser('git')
  git_parser.add_argument('-m', choices=['clone'], dest='method', required=True)
  git_parser.add_argument('pkg')
  git_parser.set_defaults(tool='git')
  
  cli_arg_parser.add_argument('-v', action='store_true', dest='verbose')
  cli_arg_parser.add_argument('-if', dest='ifile')
  cli_arg_parser.add_argument('-of', dest='ofile')
  
  args = cli_arg_parser.parse_args()
  
  if args.ifile is not None and args.method is not None or args.ifile is not None and args.pkg is not None:
    print('Only pass one set of arguments or a file with arguments within.')
    sys.exit(2)
  
  return args

if __name__ == '__main__':
  main()