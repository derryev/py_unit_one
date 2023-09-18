#rotated_shapes.py
#Eva D
#Sept 18 2023
#rotates shapes in turtle

import turtle
turtle.speed(6)

def square_loop(side_length, color):
    turtle.color(color)
    #number of rotations
    for x in range (18):
        turtle.left(20)
        #square loop
        for x in range (4):
            turtle.forward(side_length)
            turtle.left(90)

#write pen movement more quickly
def move_pen(rotation, distance):
    turtle.penup()
    turtle.left(rotation)
    turtle.forward(distance)
    turtle.pendown()

move_pen(0,-300)
turtle.left(90)
for x in range(2):
    for x in range (2):
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.left(60)
    turtle.right(120)
    for x in range(2):
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.left(60)
    turtle.right(120)
    for x in range(1):
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.left(60)





turtle.exitonclick()