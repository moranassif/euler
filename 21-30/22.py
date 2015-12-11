names_data = open("p022_names.txt", "r").read()
names = names_data.split(",")
names = sorted([name.replace('"', "") for name in names])

print(names)


def calc_alph_value(name):
    return sum([ord(s) - ord("A") + 1 for s in name])


val_sum = 0
for idx, name in enumerate(names):
    val_sum += (idx + 1) * calc_alph_value(name)

print("The sum is {}".format(val_sum))