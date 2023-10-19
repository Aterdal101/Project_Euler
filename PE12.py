import sympy 
from sympy import divisors
import numpy as np

triangle_num = []

factors=[]

n = 50000

for i in range(1, n+1):
  triangle_num.append(int(i*((i+1)/2)))

for i in triangle_num:
  x = divisors(i)
  if len(x) > 500:
    factors.append(i)
 
np.sort(factors)
print(factors[0])
  
