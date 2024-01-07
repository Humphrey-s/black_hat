#!/usr/bin/env python3
import socket
import os
Ip = __import__("ip_header").Ip
ICMP = __import__("ip_header").ICMP
host = input("Enter host to listen on : ")

def main():

    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

    sniffer.bind((host, 0))

    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            #read a packet
            raw_buffer = sniffer.recvfrom(65535)[0]
            #create an ip header from the first 20 bytes
            ip_header = Ip(raw_buffer[0:20])

            if ip_header.protocol == "ICMP":
                print("Protocol: {} {} -> {}".format(ip_header.protocol, ip_header.src_address, ip_header.dst_address))

                print("Version: {}".format(ip_header.ver))
                print('Header Length: {} TTL: {}'.format(ip_header.ihl, ip_header.ttl))

                offset = ip_header.ihl * 4
                
                buf = raw_buffer[offset:offset + 8]

                icmp_header = ICMP(buf)

                print("ICMP -> Type: {} Code {}\n".format(icmp_header.type, icmp_header.code))
            else:
                print("Protocol: {} {} -> {}".format(ip_header.protocol, ip_header.src_address, ip_header.dst_address))

    except KeyboardInterrupt:

        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
if __name__ == "__main__":

    main()
