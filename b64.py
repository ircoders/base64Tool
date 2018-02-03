#!/usr/bin/python

# Author = IWHH
# iraniancoders.ir 

import base64
import os
import sys
import time
import random
from colorama import Fore, Back, Style

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
    
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
    
 /$$$$$$ /$$$$$$$   /$$$$$$ iraniancoders.ir /$$                              
|_  $$_/| $$__  $$ /$$__  $$                | $$                              
  | $$  | $$  \ $$| $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$
  | $$  | $$$$$$$/| $$       /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/
  | $$  | $$__  $$| $$      | $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/|  $$$$$$ 
  | $$  | $$  \ $$| $$    $$| $$  | $$| $$  | $$| $$_____/| $$       \____  $$
 /$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$       /$$$$$$$/
|______/|__/  |__/ \______/  \______/  \_______/ \_______/|__/      |_______/ 
                  Base64 Encode & Decode V1.0                                                                                                                                                                                                       
    '''
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        
def GoodBye():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    
    g = '''
  /$$$$$$       iraniancoders.ir     /$$ /$$$$$$$                     
 /$$__  $$                          | $$| $$__  $$                    
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$| $$  \ $$ /$$   /$$  /$$$$$$ 
| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$$$$$$ | $$  | $$ /$$__  $$
| $$|_  $$| $$  \ $$| $$  \ $$| $$  | $$| $$__  $$| $$  | $$| $$$$$$$$
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$| $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$$
 \______/  \______/  \______/  \_______/|_______/  \____  $$ \_______/
                                                   /$$  | $$          
                                                  |  $$$$$$/          
              Base64 Encode & Decode v1.0          \______/           
    '''
    for N, line in enumerate(g.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        
cls()
print_logo()

def main():
        print '\t\t\t' + Fore.YELLOW + '[1]' + Fore.GREEN + ' Text To Base64'
        print '\t\t\t' + Fore.YELLOW + '[2]' + Fore.GREEN + ' Base64 to Text'
        print '\t\t\t' + Fore.YELLOW + '[3]' + Fore.GREEN + ' Exit'
        
        user_input = raw_input("Enter Your method : ")
        if user_input == "1":
            cls()
            print_logo()
            enc = raw_input("\t\t\t" + Fore.RED + "Enter Your text to encode it : ")
            cls()
            print_logo()
            encoded = base64.b64encode(enc)
            print("\t\t\t"+ Fore.YELLOW + str(enc.encode("utf-8")) + Fore.RED +  " -> " + Fore.GREEN + str(encoded))
        elif user_input == "2":
            cls()
            print_logo()
            dec = raw_input("\t\t\t" + Fore.RED + "Enter Your Encoded Text to decode it : ")
            cls()
            print_logo()
            decoded = base64.b64decode(dec)
            print("\t\t\t" + Fore.YELLOW + str(dec.encode("utf-8")) + Fore.RED + " -> " + Fore.GREEN + str(decoded))
        elif user_input == "3":
            cls()
            GoodBye()
        else:
            cls()
            GoodBye()
            
if __name__ == '__main__': main()
