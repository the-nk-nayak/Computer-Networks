import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 919)     # Define the server address and port
server_socket.bind(server_address)      # Bind socket with address and port

print("Server started. Listening for incoming packets...")

while True:
    # Receive a packet from a client
    data, address = server_socket.recvfrom(1024)
    print("Received from client:", data.decode())
    # Send a response back to the client
    server_socket.sendto("Server received your packet!".encode(), address)