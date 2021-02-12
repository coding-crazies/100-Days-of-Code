import turtle as t
from random import choice

timmy = t.Turtle()
t.colormode(255)
timmy.penup()
timmy.hideturtle()
color_list = [(125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85),
              (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52),
              (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), (173, 153, 159),
              (212, 183, 176), (151, 114, 119), (177, 198, 203), (206, 184, 190), (37, 73, 84), (45, 74, 63),
              (48, 66, 80)]

timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()
