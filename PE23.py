def find_abundant_numbers(limit):
    abundant_set = []
    for i in range(int(limit)):
        div = []
        for x in range(1,int(i)):
            if i%x == 0:
                div.append(x)
        if sum(div) > i:
            abundant_set.append(i)
    return abundant_set

limit = find_abundant_numbers(28123)

total_numbers = [i for i in range(28123)]

for i in limit:
    for x in limit:
        if int(i+x) in total_numbers:
            total_numbers.remove(i+x)

print(sum(total_numbers))
