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


def random_walk():
    walk_right = random.randint(1, 100)
    walk_left = random.randint(1, 100)
    left_or_right = random.randint(1, 3)
    if left_or_right == 1:
        return mbappe.left(walk_left)
    else:
        return mbappe.right(walk_right)


walk = random.randint(50, 150)
print(f'walk:{walk}')
# Random Walk
for direction in range(walk):
    mbappe.width(4)
    mbappe.speed("normal")
    random_walk()
    random_color()
    mbappe.forward(20)

screen = Screen()
screen.exitonclick()
