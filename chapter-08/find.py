def find(strng, ch, start=0, end=None):
    """
        Find and return the index of ch in string.
        Return -1 if ch does not occur in string.
    """
    ix = 0
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


def find2(strng, ch, start):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


print(find("Compsci", "p"))
print(find("Compsci", "x"))
print(find2("banana", "a", 2))
