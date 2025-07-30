import socket
import threading
import argparse
import json

def recieve(client1, client2):
    while True:
        str = client1.recv(1024)
        if (len(str) != 0):
            client2.send(str)
            
# def establish_connection (clients):
#     while True
    
parser = argparse.ArgumentParser(description = 'Getting information.')
parser.add_argument(dest='port', metavar='p', type=int, help='port')
args = parser.parse_args()

port = args.port

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)    
print ("socket is listening")
c1, addr = s.accept()
print ('Got connection from', addr )

c2, addr = s.accept()
print ('Got connection from', addr )

reciever1 = threading.Thread(target=recieve, args=(c1, c2, ))
reciever1.start()
print("reciever1 start...")

reciever2 = threading.Thread(target=recieve, args=(c2, c1, ))
reciever2.start()
print("reciever2 start...")
