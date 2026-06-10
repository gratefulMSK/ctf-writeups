import string
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

c = "fegdeogdgecoeocgcgchcfcffccfca"

for key in ALPHABET:
  ans = ""
  for i in range(0, len(c), 2):
    t1 = ((ord(c[i]) - LOWERCASE_OFFSET) - (ord(key) - LOWERCASE_OFFSET) + 16) % 16
    t2 = ((ord(c[i + 1]) - LOWERCASE_OFFSET) - (ord(key) - LOWERCASE_OFFSET) + 16) % 16
    ans += chr(((t1<<4) + t2) % (1<<8)) 
  print(key, ans)
