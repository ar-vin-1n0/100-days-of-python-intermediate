from turtle import Screen,Turtle
import pandas as pd


screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.bgpic(image)

t = Turtle()
t.hideturtle()

def writer(x,y,name):
    t.pensize(1)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(name,align="center",font=("U.S. States Game",8,"normal"))

data = pd.read_csv("50_states.csv")

state_names = data.state.to_list()

correctly_guessed = []

correct_guess = 0

while correct_guess < 50:

    user_answer = str(screen.textinput(title=f"{correct_guess}/50 correct guesses",prompt="What is your guess?")).title()

    if user_answer == "Exit":
        states_to_learn = [state for state in state_names if state not in correctly_guessed]
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv",index=False)
        break

    if user_answer in state_names and  user_answer not in correctly_guessed:
        correct_guess += 1
        x = data[data.state == user_answer].x.iloc[0]
        y = data[data.state == user_answer].y.iloc[0]
        writer(x,y,user_answer)
        correctly_guessed.append(user_answer)



