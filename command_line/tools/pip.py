class Pip:
  def __init__(self, ofile: str = None, verbose: bool = False):
    self.ofile = ofile
    self.verbose = verbose
    
  def install(self, package):
    pass
  
  def remove(self, package):
    pass
  
  def show(self, package):
    pass
    
def handle(args):
  Pip_ins = Pip(ofile=args.ofile, verbose=args.verbose)
  pass

def outer_func(func):
  def inner_func():
    return func()
  if self.verbose:
    self.logging.INFO('Func returned bla.')
  return inner_func(func)
