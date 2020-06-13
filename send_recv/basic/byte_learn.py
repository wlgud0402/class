char = "A"  # 65   01000001   0x41
number = 65 # 65   01000001   0x41

# 0xFF  => 255 

# print(char, ord(char))
# print(number, chr(number))

# print(bytes(10))
# print(bytes([0, 1, 2, 128, 255]))
# print(bytes([0,1,2,65]))

print(bytes([234, 185, 128]))
print(bytes([234, 185, 128]).decode('utf-8'))

print("김지형")
print("김지형".encode())