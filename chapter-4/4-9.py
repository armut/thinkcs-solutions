# exercise 4.9

import turtle

def draw_star(t, l):
    """Draw a star with turtle t and length l for each edge"""
    t.left(36)
    for x in range(5):
        t.left(144)
        t.forward(l)

wn = turtle.Screen()
star = turtle.Turtle()
star.hideturtle()

draw_star(star, 100)

wn.mainloop()
