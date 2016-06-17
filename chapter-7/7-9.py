# exercise 7.9

def print_triangular_numbers(n):
    for i in range(1, n+1):
        tri = 0
        for j in range(1, i+1):
            tri += j    
        print(i,"\t",tri)

print_triangular_numbers(5)
