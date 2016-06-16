# exercise 7.15

import sys

def num_even_digits(n):
    count = 0

    if n == 0:
        return 1
    else:
        n = abs(n)

    while n != 0:
        if n % 2 == 0:
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


test(num_even_digits(123456) == 3)
test(num_even_digits(2468) == 4)
test(num_even_digits(1357) == 0)
test(num_even_digits(0) == 1)
        
