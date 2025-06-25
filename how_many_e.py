a = "Welcome everyone"
b = 0
c = 0
while b < len(a):
    if a[b].lower() == "e":
        c += 1

    b += 1

print("This sentence contain" , c , "'e'")