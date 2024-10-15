import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 919)

# Connect to the server
client_socket.connect(server_address)

print("Connected to the server. Type 'quit' to exit.")

while True:
    # Get user input
    message = input("Client: ")
    if message.lower() == 'quit':
        break
    # Send the message to the server
    client_socket.sendall(message.encode())
    # Receive a response from the server
    data = client_socket.recv(1024)
    print("Server:", data.decode())

# Close the socket
client_socket.close()