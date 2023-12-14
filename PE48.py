x = [i**i for i in range(1,1001)]
x = str(sum(x))
x = x[::-1]
y = [i for i in x[0:10]]
print(''.join(y[::-1]))
