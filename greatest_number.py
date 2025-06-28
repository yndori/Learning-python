a = [32, 5, 12, 8, 3, 75, 2, 15]
b = 0
c = 0
i = 0

while c < len(a):
    if a[i] > b :
        b = a[i]
    i += 1
    c += 1

print(f"{b} is the greatest number in this list.")