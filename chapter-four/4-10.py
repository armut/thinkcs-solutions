# exercise 4.10

import turtle

def draw_star(t, l):
    """Draw a star with turtle t and length l for each edge"""
    for x in range(5):
        t.forward(l)
        t.right(144)

wn = turtle.Screen()
star = turtle.Turtle()
star.penup()
star.forward(-200)
star.pendown()

for n in range(5):
    draw_star(star, 80)
    star.penup()
    star.forward(350)
    star.right(144)
    star.pendown()

wn.mainloop()
