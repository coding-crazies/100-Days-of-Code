# from turtle import Turtle, Screen
import turtle as t
from turtle import Screen
from random import randint, choice

timmy=t.Turtle()
t.colormode(255)

def random_color():
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255)
    rgb=(r, g, b)
    return rgb

timmy.pensize(15)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0, 90, 180, 270]
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(choice(angles))

screen=Screen()
screen.exitonclick()