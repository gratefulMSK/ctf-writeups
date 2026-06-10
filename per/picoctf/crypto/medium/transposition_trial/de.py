c = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"
m = ""
for i in range(0, len(c), 3):
  m += c[i + 2]
  m += c[i : i + 2]
print(m)