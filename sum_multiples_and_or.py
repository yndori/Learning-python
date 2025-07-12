a = int(input("Enter the first boundary : "))
b = int(input("Enter the second boundary : "))
n=a
m=b
c = 0
d = 0

while a != b :
    if a % 3 == 0 and a % 5 == 0:
        c += a
    a += 1

print("The sum of the multiple of" , a , "and" , b , "is" , c)

while n != m :
    if n % 3 == 0 or n % 5 == 0:
        d += n
    n += 1

print("The sum of the multiple of" , a , "or" , b , "is" , d)