def is_sum(n):
  return n == sum(int(digit)**5 for digit in str(n))
def total():
  total = 0
  for i in range(2, 354294): #354294 is the upper bound for this problem
    if is_sum(i):
      total += i
  return total
print(total())
