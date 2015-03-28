__author__ = 'Moran'
import math


limit = 2000000

sieve = range(limit+1)
sieve[1] = 0
for siever in xrange(2, int(math.sqrt(limit)) + 1):
    for j in xrange(siever*2, limit+1, siever):
        sieve[j] = 0

print sum(sieve)