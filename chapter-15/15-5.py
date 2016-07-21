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

    def get_line_to(self, p):
        slope = (p.y - self.y) / (p.x - self.x)
        b = self.y - slope * self.x
        return (slope, b)



def find_the_center(p, q, r, s):
    #mid-point of pq:
    mpq = Point((p.x + q.x)/2, (p.y + q.y)/2)

    #mid-point of rs:
    mrs = Point((r.x + s.x)/2, (r.y + s.y)/2)

    #gradient of pq:
    gpq = (p.y - q.y) / (p.x - q.x)

    #gradient of rs:
    grs = (r.y - s.y) / (r.x - s.x)

    #x component of the center:
    x = ( (mrs.y-mpq.y)*(gpq*grs)+(gpq*mrs.x)-(grs*mpq.x) ) / (gpq-grs)

    #y component of the center:
    y = mpq.y + (mpq.x - x) / gpq

    return Point(x, y)



p = Point(2, 1)
q = Point(0, 5)
r = Point(-1, 2)
s = Point(0, 5)

print(find_the_center(p, q, r, s))

# This method won't work when the two chords pq and rs are parallel and/or
# when their lengths are different from each other.
