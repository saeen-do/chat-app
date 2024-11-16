#!/usr/bin/python3

import socket
import threading

def send_msg():
    while True:
        msg = input().encode()
        try:
            sckt.send(msg)
        except BrokenPipeError:
            print("Connection closed.")
            break

def recv_msg():
    while True:
        received = sckt.recv(1024)
        if not received:  # Check for a closed connection
            print("Connection closed.")
            break
        print(received.decode())

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting...")
while True:
    try:
        sckt.connect(("127.0.0.1", 8888))
        break
    except ConnectionRefusedError:
        continue
print("Connected")

t1 = threading.Thread(target=send_msg)
t1.start()
recv_msg()
