#!/usr/bin/python3
import sys
import threading as th
import socket as sk
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

    
    print("-e --execute=file_to_run - executes the given file upon receiving a connection\n")

    print("-u --upload=destination -  upon receiving a connection upload a file and write to destination\n")
    print("-c --command     - initate a command shell")
    print("")
    print("")
    print("Examples: ")
    print("netcap.py -t 192.168.0.105 -p 5555 -l -c")
    print("netcap.py -t 192.169.0.105 -p 5555 -l -u=c:\\target.exe")
    print("netcap.py -t 192.168.0.105 -p 5555 -l -e=\"cat /etc/passwd\"")

def client_sender(buffer):
    client = sk.socket(sk.AF_INET, sk.SORT_STREAM)

    client.connect((target, port))

    if len(buffer):
        client.send(buffer)

    while True:

        recv_len = 1
        response = ""


        while (recv_len):
            data = client.recv(4096)
            recv_len = len(data)

            if recv_len < 4096:
                break;

            print(response)
            buffer = raw_input("")
            buffer += "\n"

            client.send(buffer)

    except:
        print("[*] Exception existing")
        client.close()

def server_loop()







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

    try:
        opts, args = getopt.getopt(sys.argv(1:), "hle:p:t:cu", ["help", "listen", "execute", "port", "target", "command", "upload"])

    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:

        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
             listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-p", "--port"):
            port = int(a)
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        else:
            assert False, "Unhandled option"


  
        if not listen and len(target) and port > 0:

            buffer = sys.stdin.read()
            client_sender(buffer)

        if listen:
            server_loop()



main()
