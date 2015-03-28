__author__ = 'Moran'

limit = int(1e6)


def colatz_series_len(number):
    series_len = 1
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        series_len += 1
    return series_len

max_len = 0
max_num = 0
for i in xrange(1, limit, 2):
    length = colatz_series_len(i)
    if length > max_len:
        max_len = length
        max_num = i

print max_len, max_num