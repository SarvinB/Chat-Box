# first of all import the socket library
import socket
import threading

def recieve(client1, client2):
    while True:
        str = client1.recv(1024)
        if (len(str) != 0):
            client2.send(str)
        
# def send(client1, client2):
#     while True:
#         message = input().encode("utf-8")
#         client.send(message)
    

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 40674 but it can be anything
port = 40675

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)    
print ("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
# Establish connection with client.
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

# sender1 = threading.Thread(target=send, args=(c1, c2))
# sender1.start()
# print("sender1 start...")

# sender2 = threading.Thread(target=send, args=(c2, ))
# sender2.start()
# print("sender1 start...")

# while True:

    # send a thank you message to the client.

    
    # Close the connection with the client
    # c.close()