def f(n):
    """ Find the first positive integer between 101 and less
        than n that is divisible by 21
    """
    for i in range(101, n):
        if (i % 21 == 0):
            return i


print(f(110))
print(f(1000000000))
