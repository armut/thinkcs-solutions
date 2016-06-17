# exercise 7.5
import sys

def sum_upto_even(arr):
    total = 0
    for i in arr:
        if i % 2 != 0:
            total += i
        else:
            break
    return total


def test(did_pass):
    """Print the result of the test"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:   
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(sum_upto_even([1, 3, 5, 4, 6]) == 9)
test(sum_upto_even([1, 2, 5, 4, 6]) == 1)
test(sum_upto_even([1, 3, 5]) == 9)
test(sum_upto_even([2, 4, 6]) == 0)
