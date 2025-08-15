def volBox(x1,x2,x3):
    """This function returns The volume of a boxe with given dimensions x1 , x2 , x3"""
    volume = x1 * x2 * x3
    return volume

print(volBox.__doc__)

x1 = int(input("Enter x1 : "))
x2 = int(input("Enter x2 : "))
x3 = int(input("Enter x3 : "))
print(f"The volume is {volBox(x1,x2,x3):.2f} cm³3")