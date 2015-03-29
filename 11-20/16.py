__author__ = 'Moran'

def sum_digits(number):
    return sum([int(x) for x in str(number)])

for i in xrange(20):
    print i, 2**i, sum_digits(2**i)