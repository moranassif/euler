__author__ = 'Moran'

from fibonacci import fibonacci
from primes import is_prime, find_prime_factors
from palindrom import is_palindrom
import math


def divisors(number):
    """
    Finds divisors of a given number
    for 8 its 1,2,4,8
    :param number: A natural number
    :return: A list of divisors
    """
    divisors = set()
    for i in xrange(1, int(math.sqrt(number))+1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number/i)
    return divisors