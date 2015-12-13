import itertools
place = 1000000 - 1

str = "0123456789"

for i, s in enumerate(itertools.permutations(str)):
    if i == place:
        print("".join(s))