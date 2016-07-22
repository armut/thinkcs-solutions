# exercise 16.5

from rectangle import *

def detect_collision(r1, r2):
    if (r1.corner.x + r1.width >= r2.corner.x and
        r1.corner.x <= r2.corner.x + r2.width and
        r1.corner.y + r1.height >= r2.corner.y and
        r1.corner.y <= r2.corner.y + r2.height):
        
        return True
    else:
        return False



rect1 = Rectangle(Point(0, 0), 10, 10)
rect2 = Rectangle(Point(9, 10), 5, 7)

print(detect_collision(rect1, rect2))
        
