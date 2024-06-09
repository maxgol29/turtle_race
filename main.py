from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "purple", "green", "yellow", "orange"]
coordination = [-100, -70, -40, -10, 20, 50]
all_turtles = []
is_race_on = False

if user_bet:
    is_race_on = True


def turtles(color, y):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y)
    return turtle


for i in range(6):
    all_turtles.append(turtles(color=colors[i], y=coordination[i]))


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!!! The {winning_color} turtle won the race!")
            else:
                print(f"You lost :( The {winning_color} turtle won the race!")
        turtle.forward(randint(0, 10))

screen.exitonclick()
