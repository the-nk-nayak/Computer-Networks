import socket
import threading

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 919)

# Bind the socket to the address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server started. Listening for incoming connections...")

# Function to handle client connections
def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        # Print the received data
        print("Received from client:", data.decode())
        # Send a response back to the client
        client_socket.sendall("Server received your message!".encode())

# Function to start the server
def start_server():
    while True:
        # Accept an incoming connection
        client_socket, address = server_socket.accept()
        print("Connected by", address)
        # Create a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Start the server
start_server()