from turtle import Turtle, Screen
import random

mbappe = Turtle()
mbappe.shape("turtle")
mbappe.color("blue")
mbappe.shapesize(2, 2)

#draw square
for direction in range(4):
    mbappe.forward(100)
    mbappe.left(90)