# exercise 7.14

import sys

def num_digits(n):
    count = 0

    if n == 0:
        return 1
    else:
        n = abs(n)

    while n != 0:
        count += 1
        n = n//10

    return count


def test(did_pass):
    """Print the result of the test"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(num_digits(0) == 1)
test(num_digits(-12345) == 5)
