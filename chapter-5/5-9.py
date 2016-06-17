# exercise 5.9

import turtle

def draw_bar(t, height):
    """Get turtle t to draw one bar, of height."""
    t.begin_fill()
    t.pendown()
    t.left(90)
    t.forward(height)

    if height >= 0:
        t.write(" " + str(height))
    else:
        t.right(180)
        t.penup()
        t.forward(15)
        t.pendown()
        t.write(" " + str(height))
        t.penup()
        t.forward(-15)
        t.pendown()
        t.left(180)

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

turtl = turtle.Turtle()
turtl.pensize(3)

xs = [48, 117, -200, 240, 160, 260, 220]

for v in xs:
    if v >= 200:
       turtl.color("black", "red")
    elif v >= 100 and v < 200:
        turtl.color("black", "yellow")
    elif v < 100:
        turtl.color("black", "green")
    draw_bar(turtl, v)


wn.mainloop()
