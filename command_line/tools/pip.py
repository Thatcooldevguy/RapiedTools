import subprocess

class Pip:
  @staticmethod   
  def install(pkg):
     subprocess.run(['pip', 'install', pkg], stdout=subprocess.PIPE)
  
  @staticmethod
  def remove(pkg):
     subprocess.run(['pip', 'uninstall', pkg], stdout=subprocess.PIPE)
  
  @staticmethod
  def show(pkg):
     subprocess.run(['pip', 'show', pkg], stdout=subprocess.PIPE)
