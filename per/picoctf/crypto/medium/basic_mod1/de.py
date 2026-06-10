c = "128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140 "
c = c.split()
m = ""
for i in c:
  i = int(i) % 37
  if i < 26:
    m += chr(ord("a") + i)
  elif i < 36:
    m += chr(ord("0") + i - 26)
  else:
    m += "_"

print(m)