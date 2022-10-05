from turtle import Turtle, Screen
import random


mbappe = Turtle()
mbappe.shape("classic")
mbappe.color("blue")

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40),
              (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112),
              (16, 54, 243), (240, 16, 16)]

sum_color = len(color_list)
random_color = random.randint(0, len(color_list))


def color_from_list():
    r = color_list[random.randint(0, sum_color - 1)][0]
    g = color_list[random.randint(0, sum_color - 1)][1]
    b = color_list[random.randint(0, sum_color - 1)][2]
    colors_RGB = (r, g, b)

    return colors_RGB


screen = Screen()
screen.colormode(255)


mbappe.penup()
mbappe.setpos(-200, -200)
mbappe.speed("fastest")


for y in range(-150, 301, 50):

    for color in range(10):
        mbappe.penup()
        mbappe.forward(50)
        mbappe.dot(20, color_from_list())
        mbappe.pendown()
    mbappe.penup()
    mbappe.goto(-200, y)


screen = Screen()
screen.exitonclick()

# to get color from image
# import colorgram
#
# colors = colorgram.extract('image.jpg', 41)
# print(colors)
# first_color = colors[0]
# print(first_color)
# rgb = first_color.rgb
# print(rgb)
# red = rgb[0]
# print(red)
# red = rgb.r
# print(red)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     rgb_colors.append(new_tuple)
# print(rgb_colors)
