#asciiorder
#fortychars
#selfinput
#pythontwo

chars = """#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1

"""
b = 1 / 1

mas = ""
for i in range(len(chars)):
    if i == b * b * b:
        mas += chars[i] #prints
        b += 1 / 1

print(mas)
