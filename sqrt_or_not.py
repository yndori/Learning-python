from math import *

a = int(input("Enter an integer number: "))

if a < 0:
    print(f"The number {a} is negative, so its square root cannot be calculated in real numbers.")
else:
    integer_root = isqrt(a)
    if integer_root * integer_root == a:
        print(f"The exact square root of {a} is {integer_root}.")
    else:
        print(f"The number {a} is not a perfect square.")