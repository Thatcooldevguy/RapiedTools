#!/usr/bin/python
##inport things
import sys
import time 
import os
##done inporting##

try:
  print (30 * '-')
  f = open('acci.txt', 'r') # 'r' = read
  lines = f.read()
  print lines,
  f.close()
  print("\nVer 0.0.1a")
  print ("1. Install Basic tools")
  print ("2. Install adv tools ")
  print ("3. Check apt-get update")
  choice = raw_input('Enter your choice [1-3] : ')
  choice = int(choice)
  if choice == 1:
    print("please wait...")
    time.sleep(5) 
    os.system('sudo apt-get install gcc+'  )
    os.system('sudo apt-get install openssl')
    os.system('sudo apt-get install cowsay')
    os.system('sudo apt-get install make')
  elif choice == 2:
        print ("no packges in this menu! yet...")
  elif choice == 3:
      os.system('sudo apt-get update')      
  else:  
        print ("ERROR: submenu not found")

#handel errors#
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:
   print "not a menu!"

    