divisors_sum = [-i for i in range(10000)]

for i in range(1, 10000):
    for j in range(i, 10000, i):
        divisors_sum[j] += i
        if j == 220:
            print("Adding {}".format(i))

amicable_sum = 0

for idx, div_sum in enumerate(divisors_sum):
    if div_sum < 10000:
        if divisors_sum[div_sum] == idx and idx != div_sum:
            print("Found {} and {}".format(idx, div_sum))
            amicable_sum += idx

print("amicable sum: {}".format(amicable_sum))
print(divisors_sum[220])
print(divisors_sum[284])