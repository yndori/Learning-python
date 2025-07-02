from math import *

#l = length in m ; g = gravitational constant in m³ kg⁻¹ s⁻² ; T = period

l = int(input("Enter the length : "))
g = 9.8

T = round((2*pi)*sqrt(l/g), 3)

print("The period of the simple pendulum of length",l,"m is",T,"s")