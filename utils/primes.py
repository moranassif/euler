__author__ = 'Moran'
import math


def is_prime(number):
    """
    Check if a number is prime
    :param number: An integer
    :return: True or False
    """
    if number == 2:
        return True
    for i in xrange(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
