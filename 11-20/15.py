__author__ = 'Moran'

size = 20

paths = {}

def number_of_routes_to(x, y):
    if x == 0 or y == 0:
        return 1
    if (x,y) in paths:
        return paths[(x,y)]
    curr_paths = number_of_routes_to(x, y-1) + number_of_routes_to(x-1, y)
    paths[(x,y)] = curr_paths
    return curr_paths

print number_of_routes_to(size, size)