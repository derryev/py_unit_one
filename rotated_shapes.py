#rotated_shapes.py
#Eva D
#Sept 18 2023
#rotates shapes in turtle

import turtle
turtle.speed(0)

def square_loop(side_length, color):
    turtle.color(color)
    #number of rotations
    for x in range (18):
        turtle.left(20)
        #square loop
        for x in range (4):
            turtle.forward(side_length)
            turtle.left(90)

def draw_diamond(side_length, color):
    turtle.color(color)
    for x in range (2):
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.left(120)
def draw_corner(side_length, color):
    turtle.color(color)
    for x in range (1):
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.left(120)

#write pen movement more quickly
def move_pen(rotation, distance):
    turtle.penup()
    turtle.left(rotation)
    turtle.forward(distance)
    turtle.pendown()

def draw_illusion(side_length, color):
turtle.left(90)
for x in range(6):
    draw_diamond(side_length, color)
    turtle.goto(0,0)
    turtle.left(60)
turtle.goto(0,0)
move_pen(330, 87)
turtle.right(330)
turtle.left(60)
for x in range(6):
    draw_corner(50,"skyblue")
    turtle.right(120)



turtle.exitonclick()