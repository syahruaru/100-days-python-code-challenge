from turtle import Turtle, Screen
import random

mbappe = Turtle()
mbappe.shape("turtle")
mbappe.color("blue")
mbappe.shapesize(2, 2)

#draw square dash line
for _ in range(4):
    for _ in range(4):
        mbappe.pendown()
        mbappe.forward(15)
        mbappe.penup()
        mbappe.forward(15)
    mbappe.left(90)
#draw dash line forward
for _ in range(10):
    mbappe.pendown()
    mbappe.forward(15)
    mbappe.penup()
    mbappe.forward(15)