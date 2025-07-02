from math import *

a = int(input(("Enter the length of the first side :")))
b = int(input(("Enter the length of the second side :")))
c = int(input(("Enter the length of the third side :")))

perimeter = a + b + c

# d represent the half-perimeter

d = perimeter/2

area = sqrt(d*(d-a)*(d-b)*(d-c))

print("The perimeter of the triange is",perimeter,"cm and the area is",round(area,3),"cm²")