import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, TCP
server_socket.bind(('0.0.0.0', 3000))
server_socket.listen()

print("클라이언트 접속을 기다리는중...")
conn_socket, address = server_socket.accept() # input()
print("클라이언트 {} 가 접속했습니다.".format(address))

while True:
    recv_msg_bytes = conn_socket.recv(9)
    recv_msg = recv_msg_bytes.decode('utf-8')
    print("상대방: {}".format(recv_msg))

    msg = input(">>>")
    msg_bytes = msg.encode()
    conn_socket.sendall(msg_bytes)

conn_socket.close()
server_socket.close()