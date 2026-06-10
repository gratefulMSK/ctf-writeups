flag = 'picoCTF{Iamhuman!}'
a = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
a = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽'
b = []
for i in a:
  b.append(chr(ord(i) >> 8))
  b.append(chr(ord(i) % (1<<8)))
c = ''.join(b)

print(c)
  