# exercise 12.7

import sys

def test(did_pass):
    """ Print the result of the test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)



def myreplace(old, new, s):
    tmp = ' '.join(s.split())
    return new.join(tmp.split(old))


test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")
