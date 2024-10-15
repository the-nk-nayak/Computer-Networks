import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 998)   #(Server Address, Port)
server_socket.bind(server_address)    # Bind socket with address and port

server_socket.listen(5)     # Listen for incoming connections

print("Server started. Listening for incoming connections...")

def handle_client(client_socket):       # client Activity
    while True:
                                        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
                                        # Print the received data
        print("Received from client:", data.decode())
                                        # Send a response back to the client
        client_socket.sendall("Server received your message!".encode())

def start_server():                     # Function to start the server
    while True:
                                        # Accept an incoming connection
        client_socket, address = server_socket.accept()
        print("Connected by", address)
                                        # Create a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Start the server
start_server()