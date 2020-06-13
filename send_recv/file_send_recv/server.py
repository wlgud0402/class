import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 3000))
server_socket.listen()

print("waiting for client...")
conn_socket, address = server_socket.accept()
print("hello {}".format(address))

recv_bytes = conn_socket.recv(100)

f = open('recv.txt', 'wb')
f.write(recv_bytes)
f.close()

conn_socket.close()