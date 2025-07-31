import socket
import threading
import argparse
import json

def send_to_all(message, client):
    for c in clients:
        if ( c != client):
            c.send(message)

def recieve(client, addr):
    while True:
        message = client.recv(1024)
        if (len(message) != 0):
            message = str(addr) + ': ' + message.decode()
            send_to_all(message.encode("utf-8"), client)
            
# def establish_connection (clients):
#     while True
    
# parser = argparse.ArgumentParser(description = 'Getting information.')
# parser.add_argument(dest='port', metavar='p', type=int, help='port')
# args = parser.parse_args()

port = 40404

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
clients = []
addrs = []

print ("socket is listening")

while (True):
    s.listen(5)    
    c, addr = s.accept()
    print ('Got connection from', addr)
    clients.append(c)
    addrs.append(addr[1])
    threading.Thread(target=recieve, args=(c, addr[1])).start()

