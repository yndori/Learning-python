a = [32, 5, 12, 8, 3, 75, 2, 15]
even = []
odd = []
c = 0
i = 0

while c < len(a):
    if a[i] % 2 == 0 :
        even.append(a[i])
    else:
        odd.append(a[i])
    
    i += 1
    c += 1

print(*even ,  "are even numbers.")
print(*odd , "are odd numbers.")