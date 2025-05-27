# main program
import math
one=two=three=four=five=six=seven=eight=nine=0
for i in range(1, 10001): # 10,000 numbers generatated!
    # generate random integers from 1 to 10
    tendice = math.trunc(random(i) * 10 + 1)
    one += check(1, tendice)
    two += check(2, tendice)
    three += check(3, tendice)
    four  += check(4, tendice)
    five += check(5, tendice)
    six += check(6, tendice)
    seven += check(7, tendice)
    eight += check(8, tendice)
    nine += check(9, tendice)
print("Frequency:")
print(" 1    2    3    4    5    6    7    8    9")
print("%4d %4d %4d %4d %4d %4d %4d %4d %4d" % (one, two, three, four, five, six, seven, eight, nine))
