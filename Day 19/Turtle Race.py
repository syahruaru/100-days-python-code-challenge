from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ['red', 'brown', 'black', 'blue', 'green', 'yellow']
y_cor = [-90, -60, -30, 0, 30, 60, 90]
turtles = []
race_on = False


for i in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_cor[i])
    turtles.append(new_turtle)

if user_bet:
    race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                screen.title("YOU WIN CONGRATS!")
                screen.bgcolor('green')
            else:
                screen.title("You lose, Sorry")
                screen.bgcolor('red')

        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
screen.exitonclick()
