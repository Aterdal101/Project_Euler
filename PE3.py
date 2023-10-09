def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    if n > 1:
        return n

# Example usage
number = 600851475143
largest_factor = largest_prime_factor(number)
print(largest_factor)