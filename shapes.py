# shapes.py
# Eva D
# Sep 15, 2023
# draws a circle, square, pentagon, and triangle with turtle

import turtle

turtle.speed(0)
# made functions with all the for loops so that I could draw more shapes quickly
# if I wanted to, modeled after Bryan's square for loop function
def draw_square(side_length, color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(side_length)
        turtle.left(90)
    turtle.end_fill()

# 120 works because this triangle is made up of 3 60 angles and 180-60 is 120, so the
# outside rotation needs to be 120 each time
def draw_triangle(side_length, color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()

def draw_pentagon(side_length, color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(5):
        turtle.forward(side_length)
        turtle.left(72)
    turtle.end_fill()

def draw_circle(side_length, color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(36):
        turtle.forward(side_length)
        turtle.left(10)
    turtle.end_fill()

def draw_spiral(side_length, color):
    turtle.color(color)
    for x in range(40):
        turtle.forward(side_length)
        side_length = side_length - 2.5
        turtle.left(90)
    turtle.end_fill()

def draw_octagon(color):
    for x in range (8):
        turtle.forward(50)
        turtle.left(45)


# quicker way to move pen
def move_pen(rotation, distance):
    turtle.penup()
    turtle.left(rotation)
    turtle.forward(distance)
    turtle.pendown()


# moving pen and drawing square
move_pen(0,-300)
draw_square(60, "teal")

# moving pen and drawing pentagon
move_pen(0,150)
draw_pentagon(50, "pink")

# moving pen and drawing triangle
move_pen(0,150)
draw_triangle(60, "purple")

# moving pen and drawing circle
move_pen(0,150)
draw_circle(6,"skyblue")

move_pen(90, 250)
move_pen(90, 400)

#draw_spiral(100, "violet")
draw_octagon("blue")

turtle.exitonclick()


