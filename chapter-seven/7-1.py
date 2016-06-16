# exercise 7.1

def count_odd(arr):
    total = 0
    for i in arr:
        if i % 2 != 0:
            total += 1
    print("There are {0} odd numbers in this list.".format(total))


xs = [1, 3, 4, 7, 9, 10]
count_odd(xs)
