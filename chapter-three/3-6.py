# exercise 3.6

import turtle

wn = turtle.Screen()
tri = turtle.Turtle()
tri.shape("turtle")

# triangle
tri.penup()
tri.forward(-175)
tri.pendown()
for i in [0,1,2]:
    tri.forward(50)
    tri.left(120)

# square
tri.penup()
tri.forward(100)
tri.pendown()
for i in [0,1,2,3]:
    tri.forward(50)
    tri.left(90)

# hexagon
tri.penup()
tri.forward(100)
tri.pendown()
for i in [0,1,2,3,4,5]:
    tri.forward(28)
    tri.left(60)

# octagon
tri.penup()
tri.forward(100)
tri.pendown()
for i in [0,1,2,3,4,5,6,7]:
    tri.forward(21)
    tri.left(45)

wn.mainloop()
