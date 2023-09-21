# Eva D
# 9/21/23
# Demonstrating Properties of functions

# remember to use comments!
import turtle

#draws an octagon and takes parameter to make octagon a certain color when function is called
def draw_octagon(color, side_length):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(side_length)
        turtle.left(45)
    turtle.end_fill()

#moves turtle to new x and y coordinates without writing on the paper
def move_pen(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

move_pen(-300, 100)
draw_octagon("pink")
move_pen(200, 100)
draw_octagon("teal")
move_pen(-300, -350)
draw_octagon("violet")
move_pen(200, -350)
draw_octagon("skyblue")

turtle.exitonclick()
