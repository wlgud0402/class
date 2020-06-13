import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, TCP
server_socket.bind(('0.0.0.0', 3000))
server_socket.listen()

print("클라이언트 접속을 기다리는중...")
conn_socket, address = server_socket.accept()
print("클라이언트 {} 가 접속했습니다.".format(address))

data = conn_socket.recv(9)
print(data.decode('utf-8'))

conn_socket.close()
server_socket.close()