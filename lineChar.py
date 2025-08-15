from turtle import *
def lineChar(n,Char):
    """This function returns n times the string"""
    result = ""
    i = 0
    while i < n:
        result += Char + "\n"
        i += 1
    return result
    
print(lineChar.__doc__)
print(lineChar(int(input("Enter the number of sentences : ")),input("Enter your sentence : ")))