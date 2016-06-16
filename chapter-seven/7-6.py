# exercise 7.6
import sys

def whereis_sam(arr):
    total_words = 0
    for w in arr:
        total_words += 1
        if w == "sam":
            break
    return total_words


def test(did_pass):
    """Print the result of the test"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)



test(whereis_sam(["ham", "merry", "pippin", "sam", "frodo"]) == 4)
test(whereis_sam(["ham", "merry", "pippin", "frodo"]) == 4)
test(whereis_sam(["sam", "merry", "gandalf"]) == 1)
