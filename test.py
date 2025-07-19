grade = int(input("Enter your grade percentage : "))

if grade >= 80 :
    print("Your grade is A")
elif 80 > grade and grade >= 60 :
    print("Your grade is B")
elif 60 > grade and grade >= 50 :
    print("Your grade is C")
elif 50 > grade and grade >= 40 :
    print("Your grade is D")
elif grade < 40 :
    print("Your grade is E")