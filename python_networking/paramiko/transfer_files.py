#!/usr/bin/env python3
import paramiko
from getpass import getpass
import os

host = input("Enter host : ")
username = input("Enter username: ")
password = getpass("Enter password : ")

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for i in range(0, 4):
    try:
        client.connect(host, username=username, password=password)
        a = i
    except paramiko.ssh_exception.AuthenticationException:

        password = getpass("Please Enter the correct password: ")
        a = -1

    if a != -1:
        break

    if a == -1 and i == 3:
        print("Connection failed")


b = input("Send file[input 1]/ Download file [input 2] : ")


if b == "1":
    
    file = input("Enter path to filename : ")

    if os.path.exists(file):

        sftp = client.open_sftp()

        sftp.put(file, file)

        sftp.close()

    else:
        print("file not found")

elif b == "2":

    for d in range(0, 3):
        
        filename = input("Enter path to filename : ")
        sftp = client.open_sftp()
        try:
            sftp.get(filename, filename)
            a = d
        except FileNotFoundError:
            print("File not found")
            a = -1

        if a != -1:
            break;

        if a == -1 and d == 2:
            print("Connection time out")

        sftp.close()

else:
    pass

client.close()
