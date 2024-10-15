import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 919)     # Define the server address and port

print("Client started. Type 'quit' to exit.")

while True:
    # Get user input
    message = input("Client: ")
    if message.lower() == 'quit':
        break
    # Send the message to the server
    client_socket.sendto(message.encode(), server_address)
    # Receive a response from the server
    data, server = client_socket.recvfrom(1024)
    print("Server:", data.decode())

# Close the socket
client_socket.close()