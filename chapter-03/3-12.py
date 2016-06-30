# exercise 3.12

import turtle

wn = turtle.Screen()
dot = turtle.Turtle()
dot.shape("turtle")
dot.pensize(3)
dot.penup()

for i in range(12):
    dot.forward(80)
    dot.pendown()
    dot.forward(20)
    dot.penup()
    dot.stamp()
    dot.forward(-100)
    dot.left(30)

wn.mainloop()

    
