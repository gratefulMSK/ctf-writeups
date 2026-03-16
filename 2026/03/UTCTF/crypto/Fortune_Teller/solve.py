
output_1 = 4176616824
output_2 = 2681459949
output_3 = 1541137174
output_4 = 3272915523


print((output_2 - output_1) % 2**32)
a = (((output_3 - output_2) % (2**32)) * pow((output_2 - output_1) % 2**32, -1, 2**32)) % 2**32
print(a)
c = (output_2 - a * output_1) % 2**32
print(c)
print((output_2 * a + c) % 2**32)
output_5 = (output_4 * a + c) % 2**32

p = "3cff226828ec3f743bb820352aff1b7021b81b623cff31767ad428672ef6"
ct = bytes.fromhex(p)
key = output_5.to_bytes(4, byteorder='big')

flag = "".join(chr(ct[i] ^ key[i % 4]) for i in range(len(ct)))

print(f"{output_5=}")
print(f"hex_key={key.hex()}")
print(f"{flag=}")