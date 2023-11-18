#!/usr/bin/python3
import sys
import threading as th
import socket
import getopt
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():

    print("HNP Net Tool\n")

    print("Usage: netcap.py -t target_host -p port\n")
    print("-l --listen  -listen on [host]:[port] for incoming connections\n")

    
    print("-e --execute-file_to_run - executes the given file upon receiving a connection\n")

    print("-c --command     - initate a command shell")
    print("")
    print("")
    print("Examples: ")
    print("netcap.py -t 192.168.0.105 -p 5555 -l -c")
    print("netcap.py -t 192.169.0.105 -p 5555 -l -u=c:\\target.exe")
    print("netcap.py -t 192.168.0.105 -p 5555 -l -e=\"cat /etc/passwd\"")

def main():

    global listen
    global command
    global upload
    global execute
    global target
    global upload_destination
    global port

    if not len(sys.argv[1:]):
        usage()
main()
