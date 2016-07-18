# exercise 11.8

import sys

def test(did_pass):
    """ Print the result of the test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def cross_product(u, v):
    x = (u[1] * v[2]) - (u[2] * v[1])
    y = (u[2] * v[0]) - (u[0] * v[2])
    z = (u[0] * v[1]) - (u[1] * v[0])

    return [x, y, z]


test(cross_product([2, 3, 4], [5, 6, 7]) == [-3, 6, -3])
test(cross_product([5, 7, 2], [2, 7, 5]) == [21, -21, 21])

