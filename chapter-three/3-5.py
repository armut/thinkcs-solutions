# exercise 3.5

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# each number on a new line:
for x in xs:
    print(x)

print()

# each number and its square on a new line:
for x in xs:
    print(x, " square: ", x*x)

print()

# loop for adding the numbers:
total = 0;
for x in xs:
    total = total + x
    
print("Total is: ", total)
print()

# loop for multiplying the numbers:
product = 1;
for x in xs:
    product = product * x

print("The product is: ", product)
