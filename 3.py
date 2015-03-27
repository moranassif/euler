__author__ = 'Moran'
import math
from utils import is_prime

def find_prime_factors(number):
    """
    Finds the prime factorials of a number by stupid iteration
    :param number: A number of factor
    :return: A list of factorials
    """
    factorials = []
    for candidate in xrange(2, int(math.sqrt(number) + 1)):
        if number % candidate == 0:
            if is_prime(candidate):
                factorials.append(candidate)
            number /= candidate
    return factorials


print find_prime_factors(600851475143)