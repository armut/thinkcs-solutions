# exercise 7.7

def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.000001:
            return better
        approx = better


print(sqrt(25))
