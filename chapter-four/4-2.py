# exercise 4.2

import turtle

def draw_square(t, sz):
    """Draws a square with turtle t with size sz of each edge"""
    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)

    t.right(135)
    t.penup()
    t.forward(14)
    t.left(135)


wn = turtle.Screen()
turtl = turtle.Turtle()

size = 20
for i in range(5):
    draw_square(turtl, size)
    size = size + 20


wn.mainloop()
