__author__ = 'Moran'

pythagorean_triplet_val = 1000


for i in xrange(1, pythagorean_triplet_val):
    for j in xrange(1, i):
        k = pythagorean_triplet_val - i - j
        if i**2+j**2 == k**2:
            print i,j,k, i*j*k
