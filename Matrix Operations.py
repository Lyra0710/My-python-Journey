# Matrix Operations
import random
matrix1 = []
matrix2 = []
#----------------------------------------------------------------------------------------------------------------------
# Functions are defined here
# function to create a matrix
def matrix_create():
    matrix = []
    for i in range(2):
        rows = []
        for j in range(2):
            n = int(random.randint(1, 10))
            rows.append(n)
        matrix.append(rows)
    return matrix

# function to print matrix
def print_m(matrix):
    for row in matrix:
        print(row)

# function to add
def add(matrix1, matrix2):
    result = []
    for i in range(2):
        rows = []
        for j in range(2):
            x = matrix1[i][j] + matrix2[i][j]
            rows.append(x)
        result.append(rows)
    return result


# Function to multiply
"""The loop variable k is used to access the elements of both matrices, the element at the
 i-th row and k-th column of the first matrix is multiplied with the element at the k-th row and j-th column of the second matrix. T
 he product of these two elements is calculated in the line product = matrix1[i][k] * matrix2[k][j] and then added to the variable product_sum. 
 The variable product_sum is used to keep track of the sum of products of all the elements being multiplied during the current iteration of the outer loops."""
def mul(matrix1, matrix2):
    result = []
    for i in range(2):
        rows = []
        for j in range(2):
            product_sum = 0
            for k in range(2):
                product = matrix1[i][k] * matrix2[k][j]
                product_sum += product
            rows.append(product_sum)
        result.append(rows)
    return result

# function to find the transpose of a matrix
def transpose_m(matrix):
    result = []
    for i in range(2):
        rows = []
        for j in range(2):
            x = matrix[j][i]
            rows.append(x)
        result.append(rows)
    return result


#----------------------------------------------------------------------------------------------------------------------
# Displaying the matrices
print("The first matrix is: ")
matrix1 = matrix_create()
print_m(matrix1)
print("The second matrix is: ")
matrix2 = matrix_create()
print_m(matrix2)

# Selecting the operation
print("Select an operation to perform: ", end='')
op = input()

# To perform operations
r = []
if op == "add":
    r = add(matrix1, matrix2)
    print("The resultant matrix is: ")
    print_m(r)
elif op == "multiply":
    r = mul(matrix1, matrix2)
    print("The resultant matrix is: ")
    print_m(r)
else:
    print("Which matrix do you want to find the transpose of?: ", end='')
    inp = input()
    if inp == "matrix1":
        r = transpose_m(matrix1)
        print("The resultant matrix is: ")
        print_m(r)
    else:
        r = transpose_m(matrix2)
        print("The resultant matrix is: ")
        print_m(r)