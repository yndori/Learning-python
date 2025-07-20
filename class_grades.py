#First we will calculate the number of grades
grades = []
a = int(input("Enter your students' grades : "))

while a > 0 :
    grades.append(a)
    a = int(input("Enter your students' grades : "))
    highest_grades =max(grades)
    lowest_grades = min(grades)
    mean_grades = sum(grades) / len(grades)
    print("The number of grades is :",len(grades))
    print(f"The mean grade is : {mean_grades}")
    print(f"{highest_grades} is the highest grade in this list.")
    print(f"{lowest_grades} is the lowest grade in this list.")
