__author__ = 'Moran'
from utils import is_palindrom


def main():
    result = 0
    for i in xrange(999, 99, -1):
        for j in xrange(999, 99, -1):
            number = i * j
            if is_palindrom(str(number)):
                if number > result:
                    result = number
    print result


if __name__ == "__main__":
    main()