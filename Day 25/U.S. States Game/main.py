import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Guessed", prompt="What's a State's name?")
    title_answer = answer.title()

    if answer.title() == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if title_answer in all_states:
        coor_x = int(data[data.state == title_answer].x)
        coor_y = int(data[data.state == title_answer].y)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(coor_x, coor_y)
        tur.write(title_answer)
        guessed_state.append(title_answer)
