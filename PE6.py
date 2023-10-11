import numpy as np
sq = []
for i in range(101):
    x = i*i
    sq.append(x)
sum = 0
for i in range(101):
    sum += i
j = sum ** 2 
arr = np.array(sq)
k = 0
for i in arr:
    k += i

print(j-k) 

    

    
