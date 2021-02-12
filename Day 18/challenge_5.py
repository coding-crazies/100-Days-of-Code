import turtle
from random import randint
from turtle import Screen

timmy=turtle.Turtle()
turtle.colormode(255)

def random_color():
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255)
    rgb=(r, g, b)
    return rgb

timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)

draw_spirograph(1)

screen=Screen()
screen.exitonclick()