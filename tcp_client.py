import socket as sk

target_host = "localhost"
target_port = 9999

client = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"Hi Humphrey\nAM Mary")

response = client.recv(4096)

print(response)