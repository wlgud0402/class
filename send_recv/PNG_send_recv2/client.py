import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("connect to server...")
client_socket.connect(('127.0.0.1', 3000))

f = open('style.PNG', 'rb')

while True:
    data_bytes = f.read(1024)
    if not data_bytes:
        break
    print("send to server bytes: [ {} ]".format(len(data_bytes)))
    client_socket.sendall(data_bytes)


client_socket.close()