c = "104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42 "
c = map(int, c.split())
m = ""

for i in c:
  i %= 41
  print(i)
  i = pow(i, -1, 41)
  print(i)

  if i < 27:
    m += chr(ord("a") + i - 1)
  elif i < 37:
    m += chr(ord("0") + i - 27)
  else:
    m += "_"

print(m)