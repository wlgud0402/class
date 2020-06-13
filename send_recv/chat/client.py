import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, TCP

client_socket.connect(('127.0.0.1', 3000))

# client_socket.sendall(bytes([234, 185 ,128]))
# client_socket.sendall("김지형".encode())

while True:
    msg = input(">>>")
    msg_bytes = msg.encode()
    client_socket.sendall(msg_bytes)

    recv_msg_bytes = client_socket.recv(9)
    recv_msg = recv_msg_bytes.decode('utf-8')

    print("상대방: {}".format(recv_msg))

client_socket.close()