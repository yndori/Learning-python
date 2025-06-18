radians = float(input("Enter the number of radian : "))

degrees = radians *  180/3.14
minutes = degrees * 60
seconds = minutes * 60

print(radians , "radians is equal to:" , round(degrees , 3) , "degrees ," , round(minutes , 3) , "minutes ," , round(seconds, 3) , "seconds")