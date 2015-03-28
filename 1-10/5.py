__author__ = 'Moran'

largest_divider = 20
factorials = {1}

for i in xrange(1, largest_divider):
    number = reduce(lambda x, y: x*y, factorials)
    if number % i != 0:
        to_remove = set()
        for factor in factorials:
            if i % factor == 0:
                to_remove.add(factor)
        factorials.add(i)
        factorials.difference_update(to_remove)

number = reduce(lambda x, y: x*y, factorials)
print number