name = input("Enter your name : ")
genre = input("Enter 'M' (Male) or 'F' (Female) : ")

if genre.lower() == "m" :
    print("Welcome Mister",name)
elif genre.lower() == "f":
    print("Welcome Madam",name)