#!/usr/bin/python

## define things##
from goto import goto, comefrom, label
##end define##
label .startofcode

print (30 * '-')
f = open('acci.txt', 'r') # 'r' = read
lines = f.read()
print lines,
f.close()
print("\nVer 0.1.0")
print ("1. Install Basic tools")
print ("2. Install adv tools ")
print ("3. Check apt-get update")

 
## Get input ###
choice = raw_input('Enter your choice [1-3] : ')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Test OK")
elif choice == 2:
        print ("Test OK")
elif choice == 3:
        print ("Test OK")
else:    ## default ##
        print ("ERROR: submenu not found at ln 19-23")

    
    
goto .startofcode

 