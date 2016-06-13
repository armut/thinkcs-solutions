# exercise 3.7

import turtle

wn = turtle.Screen()
pirate = turtle.Turtle()
pirate.shape("turtle")

data = [160, -43, 270, -97, -43, 200, -940, 17, -86]
total_turn = 0
for i in data:
    pirate.left(i)
    pirate.forward(100)
    total_turn = total_turn + i

print("Pirate's heading is now: ", total_turn)
wn.mainloop()
