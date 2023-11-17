import socket as sk

target_host = "127.0.0.1"
target_port = 80

client = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

client.sendto(b"Mary Mary\n", (target_host, target_port))

data, addr = client.recvfrom(4096)

print("{}".format(data))