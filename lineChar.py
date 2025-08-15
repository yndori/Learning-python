from turtle import *
def lineChar(n,Char):
    """This function return n times the string"""
    i = 0
    while i < n:
        print(Char)
        i += 1
    
print(lineChar.__doc__)
lineChar(int(input("Enter the number of sentences : ")),input("Enter your sentence : "))