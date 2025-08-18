from turtle import *
from random import *
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

def star5(height, select_color , angle):
    """This function returns a star with a selected height , color and angle"""
    color(select_color)
    seth(angle)
    c = 0
    while c <5:
        forward(height)
        right(144)
        c = c +1

    up()

i = 0
while i < 10:
    down() 
    square(25, "red" , 0)
    up()
    forward(30)
    down()
    triangle(50, "blue" , 0)
    up()
    forward(55)
    i = i +1
a = input()

height = 25
i = 0
while i < 9:
    gap = height + 5
    down()
    star5(height, "pink" , 0)
    up()
    forward(gap)
    height = randint(25 , 50)
    i = i +1
a = input()