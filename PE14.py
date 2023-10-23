def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

max_length = 0
starting_number = 0

for i in range(1, 1000000):
    chain_length = collatz(i)
    if chain_length > max_length:
        max_length = chain_length
        starting_number = i

print(starting_number)
