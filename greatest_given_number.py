def maximum(n1,n2,n3):
    """Thhis function returns the greatest number between n1,n2,n3"""
    result = max(n1,n2,n3)
    return result

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
n3 = int(input("Enter n3 : "))
print(f"The largest number is {maximum(n1,n2,n3)}")