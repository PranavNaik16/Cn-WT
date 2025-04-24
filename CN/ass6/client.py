# client.py
import socket

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 12345))

# Receive data from server
message = client_socket.recv(1024).decode()

print("Message from server:", message)

# Close the connection
client_socket.close()
