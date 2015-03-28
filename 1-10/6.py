__author__ = 'Moran'

num_of_numbers = 100

sum_of_squares = sum(x**2 for x in xrange(1, num_of_numbers+1))
print sum_of_squares
square_of_sum = sum(x for x in xrange(1, num_of_numbers+1))**2
print square_of_sum

print square_of_sum - sum_of_squares
