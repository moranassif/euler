limit = 28123
divisors_sum = [-i+1 for i in range(limit)]

for i in range(2, limit):
    for j in range(i, limit, i):
        divisors_sum[j] += i

abundant_numbers = set()
for idx, div_sum in enumerate(divisors_sum):
    if div_sum > idx != 0:
        abundant_numbers.add(idx)

print(abundant_numbers)
print(len(abundant_numbers))

non_abundant_sum = 0
for num in range(limit+1):
    found = False
    for abundant_number in abundant_numbers:
        if num - abundant_number in abundant_numbers:
            found = True
            break
    if not found:
        non_abundant_sum += num
        print("Not found for {}".format(num))

print("Non abundant sum: {}".format(non_abundant_sum))
