# exercise 11.5

import sys

def test(did_pass):
    """ Print the result of the test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


 
def add_vectors(u, v):
    """ Takes two lists of numbers of the same length,
        and returns a new list containing the sums of
        the corresponding elements of each.
    """
    result = u
    for i in range(len(u)):
        result[i] = u[i] + v[i]

    return result


 
test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
