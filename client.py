import socket

SERVER_PORT = 5000
HOST = '127.0.0.1'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((HOST, SERVER_PORT))
msg = bytes()
while True:
    try:
        msg = server_socket.recv(8)
    except socket.timeout:
        print("Timed out waiting for server")
        break
    msg += msg
    if len(msg) <= 0:
        break

print(msg.decode('utf-8'))
