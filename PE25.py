F = [1,1]
def fibionacci():
  while len(str(F[-1] + F[-2])) < 1000:
    F.append(F[-1]+F[-2])
fibionacci()
print(len(F)+1) 
