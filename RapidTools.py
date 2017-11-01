#!/usr/bin/python
##inport things
import sys
import subprocess
import time 
from goto import with_goto
##done inporting##
@with_goto
label .begin
try:
  print (30 * '-')
  f = open('acci.txt', 'r') # 'r' = read
  lines = f.read()
  print lines,
  f.close()
  print("\nVer 0.1.0")
  print ("1. Install Basic tools")
  print ("2. Install adv tools ")
  print ("3. Check apt-get update")
  choice = raw_input('Enter your choice [1-3] : ')
  choice = int(choice)
  if choice == 1:
    print("please wait...")
    time.sleep(5) 
    subprocess.call('sudo apt-get install gcc+'  )
    subprocess.call('sudo apt-get install openssl')
    subprocess.call('sudo apt-get install cowpatty')
    subprocess.call('sudo apt-get install make')
  elif choice == 2:
        print ("no packges in this menu! yet...")
  elif choice == 3:
     subprocess.call('sudo apt-get update')      
  else:  
        print ("ERROR: submenu not found")
      goto .begin
#handel errors#
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:
   print "not a menu!"

    