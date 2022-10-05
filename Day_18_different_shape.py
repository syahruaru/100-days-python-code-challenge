from turtle import Turtle, Screen
import random

mbappe = Turtle()
mbappe.shape("turtle")
mbappe.color("blue")
mbappe.shapesize(2, 2)

def random_color():
    R = random.randint(1,255)
    G = random.randint(1,255)
    B = random.randint(1,255)
    return mbappe.pencolor(R,G,B)

screen = Screen()
screen.colormode(255)

for i in range(3,11):
    random_color()
    for direction in range(i):
        mbappe.right(360/i)
        mbappe.forward(100)

screen = Screen()
screen.exitonclick()


# for direction in range(3):
#     random_color()
#     mbappe.right(120)
#     mbappe.forward(100)
# for direction in range(4):
#     random_color()
#     mbappe.right(90)
#     mbappe.forward(100)
# for direction in range(5):
#     mbappe.right(72)
#     mbappe.forward(100)
# for direction in range(6):
#     mbappe.right(60)
#     mbappe.forward(100)
# for direction in range(7):
#     mbappe.right(51.4)
#     mbappe.forward(100)
# for direction in range(8):
#     mbappe.right(45)
#     mbappe.forward(100)
# for direction in range(9):
#     mbappe.right(40)
#     mbappe.forward(100)
# for direction in range(10):
#     mbappe.right(36)
#     mbappe.forward(100)