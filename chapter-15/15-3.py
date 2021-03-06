# exercise 15.2

class Point:
    """ Point class represents and manipulates x, y coords. """
    
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin. """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin. """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target. """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        return Point(self.x, (-1) * self.y)

    def slope_from_origin(self):
        return self.y / self.x


print(Point(3, 4).slope_from_origin())

# This method will fail when x coordinate is 0.
