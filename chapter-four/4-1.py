# exercise 4.1

import turtle

def draw_square(t, sz):
    """Draws a square with turtle t with size sz of each edge"""
    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)

    t.penup()
    t.forward(sz + sz)


wn = turtle.Screen()
turtl = turtle.Turtle()

for i in range(5):
    draw_square(turtl,20)

wn.mainloop()
