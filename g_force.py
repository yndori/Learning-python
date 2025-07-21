m1 = 10000
m2 = 10000
d = 0.05
r = 2
n = 0

while n <= 10:
    gravitational_force = round(6.67e-11 * (m1*m2) / d**2 , 3)
    print(f"d = {d} m : the gravitational force is equal to {gravitational_force} N")
    d = d*r
    n += 1