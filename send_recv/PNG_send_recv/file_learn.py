f = open('style.PNG', 'rb')

buffer = b''
while True:
    data_bytes = f.read(1024)
    print(len(data_bytes))
    if not data_bytes:
        break
    buffer += data_bytes

f = open('copy.txt', 'wb')
f.write(buffer)
f.close()