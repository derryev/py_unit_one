# Eva D
# 9/21/23
# Demonstrating properties of functions by drawing 4 octagons with turtle

#imports turtle program which will be used to draw octagons
import turtle

#draws an octagon, takes parameter to make octagon a certain color when function is called
def draw_octagon(color):
    turtle.color(color)
    turtle.begin_fill()
    #loop to draw octagon
    for x in range(8):
        turtle.forward(100)
        turtle.left(45)
    turtle.end_fill()

#moves turtle to certain coordinates without writing on the paper, takes parameters for x and y coordinates
def move_pen(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

#moves pen to top left corner
move_pen(-300, 100)
#draws pink octagon
draw_octagon("pink")
#moves pen to top right corner
move_pen(200, 100)
#draws teal octagon
draw_octagon("teal")
#moves pen to bottom left corner
move_pen(-300, -350)
#draws violet octagon
draw_octagon("violet")
#moves pen to bottom right corner
move_pen(200, -350)
#draws sky blue octagon
draw_octagon("skyblue")

#keeps turtle graphics window from closing before desired
turtle.exitonclick()
