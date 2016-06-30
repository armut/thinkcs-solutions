# exercise 4.6

import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360//n)

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)



wn = turtle.Screen()
tess = turtle.Turtle()

draw_equitriangle(tess, 50)

wn.mainloop()
    
