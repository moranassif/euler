import math

Phi = (1 + math.sqrt(5)) / 2

number_of_digits = 1000

def fibonacci_digits(index):
    return math.ceil(index * math.log(Phi, 10) - math.log(5, 10)/2)

def binary_search(range_start, range_end):
    mid_place = sum([range_start, range_end]) // 2
    mid_digits = fibonacci_digits(mid_place)
    if mid_digits == number_of_digits:
        return mid_place
    elif mid_digits > number_of_digits:
        return binary_search(range_start, mid_place)
    elif mid_digits < number_of_digits:
        return binary_search(mid_place, range_end)
    else:
        raise RuntimeError("Something is bad. range_start: {}, range_end: {}, mid_place: {}, mid_num: {}".format(range_start, range_end, mid_place, mid_num))
stam = fibonacci_digits(1000)

place_with_good_digits = binary_search(0, 1e6)
digits = fibonacci_digits(place_with_good_digits)

while digits >= number_of_digits:
    place_with_good_digits -= 1
    digits = fibonacci_digits(place_with_good_digits)

print("The Index is {}".format(place_with_good_digits + 1))