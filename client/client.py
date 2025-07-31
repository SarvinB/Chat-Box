# Import socket module
import socket
import threading
import argparse

def recieve(server):
    while True:
        stri = (server.recv(1024)).decode()
        if (len(stri) != 0):
            print(stri)
        
def send(server):
    while True:
        message = input().encode("utf-8")
        server.send(message)

# Create a socket object

# parser = argparse.ArgumentParser(description = 'Getting information.')
# parser.add_argument(dest='port', metavar='p', type=int, help='port')
# parser.add_argument(dest='ip', metavar='ip', type=str, help='IP')
# args = parser.parse_args()

# Define the port on which you want to connect
port = 40404
ip = 'server'

s = socket.socket()
# connect to the server on local computer

s.connect((ip, port))

reciever = threading.Thread(target=recieve, args=(s, ))
reciever.start()
print("reciever start...")

sender = threading.Thread(target=send, args=(s, ))
sender.start()
print("sender start...")
