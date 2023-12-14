C = set()
for a in range(2,101):
  for b in range(2,101):
    C.add(a**b)
print(len(C))
