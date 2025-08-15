import math

def surfCircle(R):
    """This function returns the Area of a circle of radius R"""
    area = math.pi * R**2
    return area

print(surfCircle(__doc__))
R = int(input("Enter the radius R : "))
print(f"The radius of the circle is : {surfCircle(R):.2f}")