# exercise 4.5.a

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

length = 3
for i  in range(99):
    t.right(89)
    t.forward(length)
    length = length + 3

t.right(90)
wn.mainloop()
