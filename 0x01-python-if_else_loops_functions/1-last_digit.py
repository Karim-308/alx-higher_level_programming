#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
x = num_str[-1]
no =int(x)
if no > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,no))
elif no == 0:
    print("Last digit of {} is {} and is 0".format(number,no))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,no))
