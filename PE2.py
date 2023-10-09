#Project Euler 2
F = [1,1]
C = []
x=0
def fib():
    while F[-1] < 4000000:
        F.append(F[-1]+F[-2]) 
        if F[-1] + F[-2] > 4000000:
            break  
fib()
for i in F:
    if i%2 == 0:
        C.append(i)
for a in C:
    x += a
print(x)
