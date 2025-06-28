t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []
c = 0
i = 0

while c < len(t2):
    t3.append(t2[i])
    t3.append(t1[i])
    i += 1
    c += 1

print(t3)