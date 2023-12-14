import math
x = int(input("Enter grid size: "))
routes = math.comb(2*x, x)
print(routes)
