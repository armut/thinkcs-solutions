# exercise 7.3

def sum_negatives(arr):
    total = 0
    for i in arr:
        if i < 0:
            total += i
    print("Sum of the negative numbers in this list is {0}.".format(total))


xs = [1, 2, 3, 4, -5, -9]
sum_negatives(xs)
