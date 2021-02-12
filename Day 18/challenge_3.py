from turtle import Turtle, Screen
from random import choice

timmy=Turtle()

sides=3
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(10):
    timmy.color(choice(colours))
    for j in range(sides):
        timmy.begin_fill()
        timmy.forward(100)
        timmy.right(360/sides)
        timmy.end_fill()
    sides+=1

screen=Screen()
screen.exitonclick()