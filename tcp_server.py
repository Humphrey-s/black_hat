import socket as sk
import threading as th

ip = "0.0.0.0"
port = 9999

server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server.bind((ip, port))

print("[*] listening on {}:{}".format(ip, port))

server.listen(5)

def handle_client(client):

    request = client.recv(1024)

    print("Received: ", request)
    client.send(b"ACK!")
    client.close()

while True:

    client, addr = server.accept()

    print("[*] accepted connection from: {}", addr)
    client_handler = th.Thread(target=handle_client, args=(client,))
    client_handler.start()