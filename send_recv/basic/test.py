import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.2', 3000))

print("서버에 접속했습니다.")

f = open('clo.png', 'rb')

while True:
  byte_data = f.read(1024)
  if not byte_data:
    break
  print("send [ {} ] bytes...".format(len(byte_data)))
  time.sleep(0.5)
  client_socket.sendall(byte_data)

client_socket.close()