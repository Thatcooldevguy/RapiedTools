import subprocess

class Git:
  @staticmethod
  def install(pkg):
     subprocess.run(['git', 'clone', pkg], stdout=subprocess.PIPE)
     
