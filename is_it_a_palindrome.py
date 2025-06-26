a = input("Enter a word :")
b = len(a)
c = ""

while b > 0:
    c += a[b-1]
    b -= 1

if a == c:
    print(f"The word '{a}' is a palindrome")
else:
    print(f"The word '{a}' is not a palindrome")