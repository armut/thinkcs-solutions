# exercise 7.2

def sum_even(arr):
    total_sum = 0
    for i in arr:
        if i % 2 == 0:
            total_sum += i
    print("Sum of the even numbers in this list is {0}.".format(total_sum))


xs = [2, 4, 6, 3, 7, 9, 10]
sum_even(xs)
