__author__ = 'Moran'


def is_palindrom(string):
    """
    Check if a string is a palindrom (like 9009)
    :param string: A string
    :return: Is a palindrom
    """
    if len(string) < 2:
        return True
    if string[0] == string[-1]:
        return is_palindrom(string[1:-1])
    else:
        return False