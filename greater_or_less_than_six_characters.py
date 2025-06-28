a = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
greater = []
less = []
c = 0
i = 0

while c < len(a):
    if len(a[i]) >= 6 :
        greater.append(a[i])
    else:
        less.append(a[i])
    
    i += 1
    c += 1

print(*greater ,  "have 6 or more characters.")
print(*less , "have less than 6 characters.")