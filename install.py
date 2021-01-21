#!/usr/bin/env python3

from subprocess import run
from sys import exit


print("""\033[1;37;41m[!] Don't quit while the packages exit [!]
[!] You need python3 and pip3 installed for this [!]""")

print("\033[m")

run(["sudo", "pip3", "install", "scapy"])
run(["sudo", "pip3", "install", "scapy_http"])

print()

while True:
    command = input("[+] Do you want to run the script?(y/n) : ")
    
    if command.lower() == 'y' or command.lower() == "yes":
        run(["sudo", "python3", "tusker_interface.py"])
    
    elif command.lower() == 'n' or command.lower() == "no":
        exit()
        
    else: 
        print("\033[1;31m[!] Enter valid commands!!! [!]")
        continue
