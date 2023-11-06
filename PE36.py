palindromicnos = []

for i in range(1000000):
    str_i = str(i)
    if str_i == str_i[::-1] and str(bin(i))[2:] == str(bin(i))[2:][::-1]:
        palindromicnos.append(i)

print(sum(palindromicnos))
