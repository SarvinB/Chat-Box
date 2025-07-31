## Without Docker
Run server with one arugment port and clients with two argument host and port of server

## With doucker

```bash
# Run it in Path where client folder is
docker build -t chat-room-client:1.0 client 

# Run it in Path where server folder is
docker build -t chat-room-server:1.0 server

# Make Network for comminucating between server and clients
docker network create chat-room-net

# For more client just change name of container
docker run -it --name client1 --network chat-room-net chat-room-client:1.0

# Make and run server container
docker run -d --name server --network chat-room-net -p 40405:40404 chat-room-server:1.0 
