# exercise 11.6

import sys

def test(did_pass):
    """ Print the result of the test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def scalar_mult(s, v):
    """ Takes a number, s, and a list, v and 
        returns the scalar multiple of v by s.
    """
    for i in range(len(v)):
        v[i] = v[i] * s
    
    return v



test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

