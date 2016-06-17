# exercise 5.7

import turtle

def draw_bar(t, height):
    """Get turtle t to draw one bar, of height."""
    t.begin_fill()
    t.pendown()
    t.left(90)
    t.forward(height)
    t.write(" " + str(height))
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
turtl.color("blue","red")
turtl.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for v in xs:
    draw_bar(turtl, v)


wn.mainloop()
