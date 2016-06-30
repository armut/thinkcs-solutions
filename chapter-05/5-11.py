# exercise 5.11

def is_rightangled(side1, side2, longest_side):
    if (longest_side**2) - (side1**2 + side2**2) < 0.000001:
        return True
    else:
        return False

data1 = input("Please enter the first side: ")
data2 = input("Please enter the second side: ")
data3 = input("Please enter the longest side: ")

print(is_rightangled(float(data1), float(data2), float(data3)))
