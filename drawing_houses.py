

import turtle

def draw_house(square_side_length, Wcolor, Rcolor):
    turtle.color(Wcolor)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(square_side_length)
        turtle.right(90)
    turtle.left(60)
    turtle.end_fill()
    turtle.color(Rcolor)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(square_side_length)
        turtle.right(120)
    turtle.end_fill()
def move_pen(coord, y, rotation):
    turtle.penup()
    turtle.right(rotation)
    turtle.goto(coord, y)
    turtle.pendown()

move_pen(-300, 0, 0)

def draw_neighborhood(m, y):
    for x in range(4):
        turtle.penup()
        turtle.goto(m, y)
        turtle.pendown()
        draw_house(100, "skyblue", "violet")
        turtle.right(180)
        m = m+200

draw_neighborhood(-350, 0)

turtle.exitonclick()