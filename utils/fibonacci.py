__author__ = 'Moran'


def fibonacci(max_num):
    """
    A generator for the fibonacci series 1,2,3,5...
    :param max_num: The maximum number that can be returned
    :return: Numbers of the series
    """
    numbers = [1, 2]
    pos = 1
    while numbers[-1] < max_num:
        if pos < 3:
            yield numbers[pos-1]
        else:
            numbers = [numbers[-1], sum(numbers)]
            yield numbers[-1]
        pos += 1