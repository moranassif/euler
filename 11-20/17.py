__author__ = 'Moran'

words = {1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine",
         10: "ten",
         11: "eleven",
         12: "twelve",
         13: "thirteen",
         14: "fourteen",
         15: "fifteen",
         16: "sixteen",
         17: "seventeen",
         18: "eighteen",
         19: "nineteen",
         20: "twenty",
         30: "thirty",
         40: "forty",
         50: "fifty",
         60: "sixty",
         70: "seventy",
         80: "eighty",
         90: "ninety"}

numbers = []
for i in xrange(1000):
    number = ""
    ones = i % 10
    tenths = (i / 10) % 10
    hundreds = (i / 100) % 10
    if hundreds > 0:
        number += words[hundreds] + " hundred"
    if tenths:
        if hundreds:
            number += " and "
        if tenths == 1:
            number += words[i % 100]
        else:
            number += words[10 * tenths]
    if ones and not tenths == 1:
        if tenths or hundreds:
            number += " "
        if hundreds and not tenths:
            number += "and "
        number += words[ones]
    print number
    numbers.append(number)

phrase = "".join(numbers).replace(" ", "") + "onethousand"
print phrase
print len(phrase)