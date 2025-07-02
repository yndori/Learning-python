a = []
b = input("Enter a new value to be added to the list. If you're done write 'enter' : ")

while b.lower() != "enter" :
    a.append(b)
    b = input("Enter a new value to be added to the list. If you're done write 'enter' : ")

print(a)