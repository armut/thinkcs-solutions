# exercise 5.10

def find_hypot(side1, side2):
    hypot = ((side1 * side1) + (side2 * side2)) ** 0.5
    return hypot


data1 = input("Please enter the first side: ")
data2 = input("Please enter the second side: ")

print(find_hypot(int(data1), int(data2)))
