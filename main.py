import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_states = data["state"]
all_states = data.state.to_list()
# print(data)

guessed_states = []
game_is_on = True
while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50 correct", prompt="What's another state's?")
    cap_answer = answer_state.capitalize()
    for state in all_states:
        if cap_answer == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("missing_states.csv")
            break
        if cap_answer == state:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            x_loc = int(data[data.state == cap_answer].x)
            y_loc = int(data[data.state == cap_answer].y)
            t.goto(x_loc,y_loc)
            t.write(cap_answer )
            guessed_states.append(cap_answer)














screen.exitonclick()