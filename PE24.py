from itertools import permutations
x = (input().split())
perms = [i for i in permutations(x)]
perms = sorted(perms)
y = int(input())-1
print(''.join(perms[y]))
