read_file = open('style.PNG', 'rb')

write_file = open('copy3.PNG', 'wb')

while True:
    data_bytes = read_file.read(1024)
    if not data_bytes:
        break
    print("write bytes... {}".format(len(data_bytes)))
    write_file.write(data_bytes)

read_file.close()
write_file.close()