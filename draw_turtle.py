from turtle import *
def square(height, select_color , angle):
    """This function returns a square with a selected height , color and angle"""
    color(select_color)
    seth(angle)
    c = 0
    while c <4:
        forward(height)
        right(90)
        c = c +1

    up()

def triangle(height, select_color , angle):
    """This function returns a triangle with a selected height , color and angle"""
    color(select_color)
    seth(angle)
    c = 0
    while c <3:
        forward(height)
        right(120)
        c = c +1

    up()


print(square.__doc__)


i = 0
while i < 10:
    down() 
    square(25, "red" , 90)
    up()
    forward(30)
    down()
    triangle(50, "blue" , 90)
    up
    forward(55)
    down() 
    square(25, "red" , 90)
    up()
    forward(30)
    down()
    triangle(75, "blue" , 90)
    up
    forward(80)
    i = i +1
a = input()
