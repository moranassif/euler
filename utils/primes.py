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


def find_prime_factors(number):
    """
    Finds the prime factorials of a number by stupid iteration
    :param number: A number of factor
    :return: A list of factorials
    """
    factorials = {number} if is_prime(number) else set()
    for candidate in xrange(2, int(math.sqrt(number) + 1)):
        if number % candidate == 0:
            if is_prime(candidate):
                factorials.add(candidate)
                factorials.update(find_prime_factors(number/candidate))
            number /= candidate
    return factorials
