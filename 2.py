__author__ = 'Moran'


from utils import fibonacci

f = fibonacci(4e6)
total_sum = 0
for x in f:
    if x % 2 == 0:
        total_sum += x

print total_sum