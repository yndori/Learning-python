a = "zorglub"
b = len(a)
c = ""

while b > 0:
    c += a[b-1]
    b -= 1

print("The reverse of" , a , "is" , c)

