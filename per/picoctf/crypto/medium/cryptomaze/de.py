init = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
tap = [63, 61, 60, 58]

for _ in range(1000):
  t = 0
  for k in tap:
    t ^= init[k - 1]
  for i in range(len(init) - 2, -1, -1):
    init[i + 1] = init[i]
  init[0] = t
  print("".join(str(k) for k in init))
  