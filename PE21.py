def divisors_sum(number):
  divisors_sum = 0
  for i in range(1, number):
      if number % i == 0:
          divisors_sum += i
  return divisors_sum

C = []

for a in range(2, 10000):
  b = divisors_sum(a)
  if a != b and b < 10000 and a == divisors_sum(b):
    C.append(a)
print(sum(C))
