# exercise 16.1

from point import Point

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h. """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas. """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas. """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def flip(self):
        self.width, self.height = self.height, self.width

    def contains(self, pnt):
        if pnt.x >= self.corner.x and pnt.x < self.corner.x + self.width:
            if pnt.y >= self.corner.y and pnt.y < self.corner.y + self.height:
                return True
        return False
            
