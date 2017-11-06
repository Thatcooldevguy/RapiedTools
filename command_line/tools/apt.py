import subprocess

class Apt:
  @staticmethod
  def install(pkg):
     subprocess.run(['apt', 'get-install', pkg], stdout=subprocess.PIPE)
  
  @staticmethod
  def uninstall(pkg):
    subprocess.run(['apt', 'get-uninstall', pkg], stdout=subprocess.PIPE)
     