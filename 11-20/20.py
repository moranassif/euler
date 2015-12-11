import math

num = 100

fact = math.factorial(num)

sumer = 0
while fact > 0:
    sumer += fact % 10
    fact //= 10

print("sum is {}".format(sumer))