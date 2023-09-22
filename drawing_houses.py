

import turtle

def draw_house(square_side_length, color):
    for x in range(4):
        turtle.forward(square_side_length)
        turtle.right(90)
    turtle.left(60)
    for x in range(2):
        turtle.forward(square_side_length)
        turtle.right(120)


draw_house(300,  "black")


turtle.exitonclick()