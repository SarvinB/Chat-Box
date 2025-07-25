# Import socket module
import socket
import threading

def recieve(server):
    while True:
        str = server.recv(1024)
        if (len(str) != 0):
            print("server: %s" %(str))
        
def send(server):
    while True:
        message = input().encode("utf-8")
        server.send(message)

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 40675

# connect to the server on local computer
s.connect(('127.0.0.1', port))

reciever = threading.Thread(target=recieve, args=(s, ))
reciever.start()
print("reciever start...")

sender = threading.Thread(target=send, args=(s, ))
sender.start()
print("sender start...")
# receive data from the server
    
    


# close the connection
# s.close()