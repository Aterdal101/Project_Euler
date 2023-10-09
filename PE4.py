import numpy as np

ovl_num = []
pali = []
x = ovl_num
for i in range(998000, 10000, -1):
    ovl_num.append(i)
   
for i in x:
    if 850000<= i <= 998001:
        c = str(i)
        if str(i)[:3] == c[-1] + c[-2] + c[-3]:
            pali.append(i)

factor1 = []
factor2 =[]
p = []
for i in range(99, 1000):
    factor1.append(i)
for i in range(99, 1000):    
    factor2.append(i)

for i in pali:
    for x in factor1:
        for f in factor2:
            if i == f*x:
                p.append(i)
        
print(np.sort(p)[-1])



        