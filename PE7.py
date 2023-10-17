x = 10001 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
count = 0
num = 2
while count < x:
    if is_prime(num):
        count += 1
    num += 1
xth_prime = num - 1
print(xth_prime)