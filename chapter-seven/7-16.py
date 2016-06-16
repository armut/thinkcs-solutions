# exercise 7.16

import sys

def sum_of_squares(xs):
    result = 0
    for i in xs:
        result += i*i
    return result


def test(did_pass):
    """Print the result of the test"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([ ]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)
