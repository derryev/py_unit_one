import turtle

def draw_square(side_length, color):
    turtle.color(color)
    turtle.begin_fill()

    for x in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

#120 works because this triangle is made up of 3 60 angles and 180-60 is 120, so the outside rotation needs to be 120 each time
def draw_triangle(side_length, color):
    turtle.color(color)
    turtle.begin_fill()
#figure out later
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

def move_pen(rotation, distance):
    turtle.penup()
    turtle.left(rotation)
    turtle.forward(distance)
    turtle.pendown()

move_pen(0,-300)

draw_square(50, "teal")




#moving to a new location and drawing a pentagon
move_pen(0,150)
draw_pentagon(50, "pink")

#moving to a new location and drawing a triangle
move_pen(0,150)
draw_triangle(50, "purple")

move_pen(270,100)


turtle.exitonclick()