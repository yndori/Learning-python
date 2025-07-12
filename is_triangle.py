a = int(input("Enter the side a : "))
b = int(input("Enter the side b : "))
c = int(input("Enter the side c : "))

if a + b > c and a + c > b and b + c > a:
    print("It's possible to form a triangle!")

    if a == b and b == c:
        print("The triangle is equilateral.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("The triangle is a right triangle.")
    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("It's not possible to form a triangle with these side lengths.")