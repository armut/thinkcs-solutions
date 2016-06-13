# exercise 4.3

import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360//n)


wn = turtle.Screen()
tess = turtle.Turtle()

draw_poly(tess, 8, 50)

wn.mainloop()
