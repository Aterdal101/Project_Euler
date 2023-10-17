import numpy as np
prime_list = []
ovl = []
n = 2000000
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_numbers(n):
    prime_numbers = [num for num in range(2, n+1) if is_prime(num)]
    return prime_numbers

prime_list = generate_prime_numbers(n)

def find_sum(x):
    total_sum = 0
    for i in x:
        total_sum += i
    return total_sum

ovl = find_sum(prime_list)
print(ovl)




