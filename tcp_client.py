#!/usr/bin/python3
import socket as sk

target_host = "localhost"
target_port = 9999

client = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"Hello")

response = client.recv(4096)
