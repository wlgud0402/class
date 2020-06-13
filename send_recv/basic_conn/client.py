import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, TCP
client_socket.connect(('127.0.0.1', 3000))

# client_socket.sendall(bytes([234, 185 ,128]))
client_socket.sendall("김지형".encode())

client_socket.close()