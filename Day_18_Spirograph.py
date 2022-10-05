from turtle import Turtle, Screen
import random

mbappe = Turtle()
mbappe.shape("turtle")
mbappe.color("blue")


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return mbappe.pencolor(r, g, b)


screen = Screen()
screen.colormode(255)


# Spirograph
rad = 100
for i in range(1, 361, 5):
    random_color()
    mbappe.speed(8)
    mbappe.circle(rad)
    mbappe.left(i)

screen = Screen()
screen.exitonclick()
