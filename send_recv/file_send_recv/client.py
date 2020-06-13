import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("connect to server...")
client_socket.connect(('127.0.0.1', 3000))

f = open('test.txt', 'rb')
data_bytes = f.read()

client_socket.sendall(data_bytes)

client_socket.close()