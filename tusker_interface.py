#!/usr/bin/env python3

import scapy.all as scapy, time, subprocess, sys

try:
    subprocess.run(["sudo", "sysctl", "net.ipv4.ip_forward=1"])


    subprocess.run(["clear"])
    time.sleep(1)

    def help():
        print()
        print("\033[1;34m="*60)
        print("""
\t\t    \033[1;31mScript Opions:\n
\033[1;33m\t[ 1 ]\033[1;32m Arp Spoofing Attack (spoof)
\033[1;33m\t[ 2 ]\033[1;32m HTTP/HTTPS Login Sniffer (sniff)
\033[1;33m\t[ 3 ]\033[1;32m Exit Tusker Interface (quit/exit)\n
\033[1;33m\t[-h, --help]\033[1;32m To View This Help Message (help)
\033[1;33m\t[cls, clear]\033[1;32m Clears the screen\n""")
        print("\033[1;34m="*60)
        print()

    print("""\033[1;31m
   ______            __                          
  /_  __/__ __ ___  / /__ ___  ____              
   / /  / // /(_-< /  '_// -_)/ __/              
  /_/   \_,_//___//_/\_\ \__//_/__               
       (_)___  / /_ ___  ____ / _/___ _ ____ ___ 
      / // _ \/ __// -_)/ __// _// _ `// __// -_)
     /_//_//_/\__/ \__//_/  /_/  \_,_/ \__/ \__/
                                  
                            \033[1;33mProgram by \033[1;32mmage-master                          
""")


    help()

    while True:
        print("\033[1;32m")
        
        command = input("\033[1;31mtusker_shell>\033[1;37m  ")
    
        if command.lower() == "-h" or command.lower() == "--help" or command.lower() == "help":
            print()
            help()
            
        elif command == "1" or command.lower() == "spoof":
            print("\033[1;33m\n[+] Executing Arp Spoofing [+]")
            subprocess.run(["sudo", "python3", "arp_spoofer.py"])
        
        elif command == "2" or command.lower() == "sniff":
            print("\033[1;33m\n[+] Executing HTTP/HTTPS Login Sniffer [+]")
            subprocess.run(["sudo", "python3", "sniffer.py"])
    
        elif command == "3" or command.lower() == "quit" or command.lower() == "exit":
            print("\033[1;31m[!] Quitting [!]")
        
            break
        
        elif command.lower() == "cls" or command.lower() == "clear":
            subprocess.run(["clear"])
            continue
            
        else: 
            print("\033[1;36m\n[-] Please re-run the program with valid arguments [-]")
            continue
        
        
except(KeyboardInterrupt):
    print("\033[1;33m\n\nCTRL C Deteced... Quitting")



subprocess.run(["sudo", "sysctl", "net.ipv4.ip_forward=0"], stdout=subprocess.PIPE)

print("\n\033[5;32m[+] Program by mage-master [+]\n\033[m")

sys.exit()
 


