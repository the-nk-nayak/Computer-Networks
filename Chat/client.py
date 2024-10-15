import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #socket object

server_address = ('localhost', 998)         # Define server's address and port

client_socket.connect(server_address)       # Connect server

print("Connected to the server. Type 'quit' to exit.")

while True:
    message = input("Client: ")             # Get user input
    if message.lower() == 'quit':
        break
                                            # Send the message to the server
    client_socket.sendall(message.encode())
                                    # Receive a response from the server
    data = client_socket.recv(1024)
    print("Server:", data.decode())

# Close the socket
client_socket.close()