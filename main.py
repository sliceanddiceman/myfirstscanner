# first port scanner

import socket

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.settimeout(5)

host = input("Enter the IP address: ")
port = int(input("Enter port: "))


def portscanner(port):
    if S.connect_ex((host, port)):
        print("Closed")
    else:
        print("Open")


portscanner(port)
