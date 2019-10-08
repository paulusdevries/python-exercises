import turtle
import time


stempel = turtle.Turtle()

stempel.shape("circle")
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

for shape in shapes:
    stempel.shape(shape)
    stempel.penup()
    for i in range(5):
        if i % 2 == 0:
            stempel.pendown()
        else:
            stempel.penup()
        stempel.forward(40)
        stempel.left(360/(6*5))
        stempel.stamp()

