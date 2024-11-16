#!/usr/bin/python3

import socket
import threading

def send_msg():
    while True:
        msg = input().encode()
        client.send(msg)

def recv_msg():
    while True:
        received = client.recv(1024)
        if not received:  # Check for a closed connection
            print("Connection closed.")
            break
        print(received.decode())

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sckt.bind(("127.0.0.1", 8888))
print("Listening...")
sckt.listen(1)
client, addr = sckt.accept()  # Corrected this line
print("Connected to:", addr)

t1 = threading.Thread(target=send_msg)
t1.start()
recv_msg()
