# exercise 4.4

import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360//n)

    t.left(18)


wn = turtle.Screen()
turtl = turtle.Turtle()

for i in range(20):
    draw_poly(turtl, 4, 75)


wn.mainloop()
