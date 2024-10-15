import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #TCP socket

server_address = ('localhost', 919)       # Bind socket with address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server started. Waiting for connection...")

while True:
    # Accept an incoming connection
    connection, address = server_socket.accept()
    print("Connected by", address)

    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Send the date and time to the client
    message = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    connection.sendall(message.encode())

    # Close the connection
    connection.close()