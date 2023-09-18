import socket

QUEUE_SIZE = 5
PORT = 5000
HOST = '127.0.0.1'

"""Creates a socket"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(QUEUE_SIZE)
print("server listening")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}, {client_socket = }")
    client_socket.send(bytes("Welcome to the server!", "utf-8"))
    client_socket.close()
