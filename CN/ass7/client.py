# client.py (TCP File Transfer - Client)
import socket

host = '127.0.0.1'  # Server IP
port = 65432        # Same port as used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Open the file to send
with open('hello.txt', 'r') as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

print("[+] File sent successfully.")
client_socket.close()
