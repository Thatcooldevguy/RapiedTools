import sys
import argparse
from tools.pip import Pip
from tools.git import Git
from tools.apt import Apt


def main():
  args = parse_prog_args()
  
  if args.ifile is not None:
    pass
  
  tool_picker(args)

def tool_picker(args): 
    if args.tool == 'pip':
      getattr(Pip(), args.method)(args.pkg)
    elif args.tool == 'apt':
      getattr(Apt(), args.method)(args.pkg)
    elif args.tool == 'git':
      getattr(Git(), args.method)(args.pkg)
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
  git_parser.add_argument('-m', choices=['clone'], dest='method', required=True , help= 'clone a repo')  
  git_parser.set_defaults(tool='git')
  
  args = cli_arg_parser.parse_args()
  
  if args.ifile is not None and args.method is not None or args.ifile is not None and args.pkg is not None:
    print('Only pass one set of arguments or a file with arguments within.')
    sys.exit(2)
  
  return args
##help code ##
















##end help comment##

if __name__ == '__main__':
  main()