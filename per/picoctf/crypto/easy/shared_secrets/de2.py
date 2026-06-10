enc = 0x2a333935190e1c213e320529693928692e056b38393c6b633b6327

byt = enc.to_bytes((enc.bit_length() + 7) // 8, byteorder='big')

for i in range(256):
    mas = "".join([chr(x ^ i) for x in byt])
    if mas[0] == 'p':
        print(mas)
