import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #TCP socket

server_address = ('localhost', 919)       #Server Connect
client_socket.connect(server_address)

                                        # Receive the date and time from the server
message = client_socket.recv(1024)
print("Received from server:", message.decode())

client_socket.close()           # Close the connection