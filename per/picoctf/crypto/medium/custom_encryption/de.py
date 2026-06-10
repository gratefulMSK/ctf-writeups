from random import randint
import sys

a = 95
b = 21
c = [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
g = 31
p = 97

keytxt = "trudeau"

for a in range(p - 10, p):
  for b in range(g - 10, g):
    if not (a == 95 and b == 21):
      continue
    key = pow(pow(g, a, p), b, p)
    semimas = ""
    ok = True
    for i in c:
      if i % 311 or i % key:
        ok = False
        break
      else:
        semimas += (chr(int(i / 311 / key)))
    if not ok:
      continue
    mas = ""
    for i in range(len(semimas) - 1, -1, -1):
      mas += chr(ord(semimas[i]) ^ ord(keytxt[i % len(keytxt)]))
    print(mas)
    

