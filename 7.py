__author__ = 'Moran'

from utils import is_prime

prime_number_place = 10001
prime_number = None
idx = 2
number = 3

while not prime_number:
    if is_prime(number):
        if idx == prime_number_place:
            print number
            break
        else:
            idx += 1
    number += 2