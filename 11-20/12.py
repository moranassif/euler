__author__ = 'Moran'
from utils import divisors

num_of_divisors = 500
even_idx = 2
odd_idx = 1
now_odd = True


while True:
    even_divisors = divisors(even_idx/2)
    odd_divisors = divisors(odd_idx)
    idx_divisors = {x*y for x in even_divisors for y in odd_divisors}
    if len(idx_divisors) > num_of_divisors:
        print odd_idx * even_idx / 2, idx_divisors
        break
    if now_odd:
        odd_idx += 2
    else:
        even_idx += 2
    now_odd = not now_odd
