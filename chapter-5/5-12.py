# exercise 5.12

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        index = i
        while index > 0 and arr[index - 1] > key:
            arr[index] = arr[index - 1]
            index = index - 1

        arr[index] = key


def is_rightangled(side1, side2, side3):
    sides = [side1, side2, side3]
    insertion_sort(sides)
    if (sides[2]**2) - (sides[0]**2 + sides[1]**2) < 0.000001:
        return True
    else:
        return False

data1 = input("Please enter the first side: ")
data2 = input("Please enter the second side: ")
data3 = input("Please enter the third side: ")

print(is_rightangled(float(data1), float(data2), float(data3)))
