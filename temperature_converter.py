print("1 - Celsus to Fahrenheit")
print("2 - Fahrenheit to Celsus")
Choice = int(input("Enter your choice :"))

if Choice == 1:
    Celsus = float(input("Enter the number of Celsus : "))

    Fahrenheit = (Celsus * 9/5) + 32

    print(Celsus , "degree celsus is equal to:" , round(Fahrenheit , 2) , "degree Fahrenheit")
elif Choice == 2:
    Fahrenheit = float(input("Enter the number of Fahrenheit : "))

    Celsus = (Fahrenheit - 32) * 5/9

    print(Fahrenheit , "degree fahrenheit is equal to:" , round(Celsus , 2) , "degree Celsus")