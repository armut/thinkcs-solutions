# exercise 11.4

this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

# this is not that in the first test because lists are mutable and
# don't refer to the same object. In test 2 after the 6th line, the two lists
# refer to the same object, so the result is true.
