# exercise 7.8

def print_multiples(n, high):
    for i in range(1, high+1):
        print(n * i, end="\t")
    print()


def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, high)


print_mult_table(9)
