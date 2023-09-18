#star.py
#Eva D
#september 18 2023
#draws a star
import turtle

def draw_star(side_length, color):
    turtle.color(color)
    for x in range(5):
        turtle.forward(side_length)
        turtle.left(144)

draw_star(100, "pink")


turtle.exitonclick()