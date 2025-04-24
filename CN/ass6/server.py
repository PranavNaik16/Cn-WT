

import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reserve a port
port = 12345


server_socket.bind(('', port))


server_socket.listen(5)
print(f"Server is listening on port {port}...")


while True:
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")
    
    client_socket.send(b'Thank you for connecting')
    
    client_socket.close()
