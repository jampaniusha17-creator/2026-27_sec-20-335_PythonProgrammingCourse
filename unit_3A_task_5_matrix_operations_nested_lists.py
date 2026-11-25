# Matrix Operations using Nested Lists

# Read matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Read first matrix
print("Enter elements of first matrix:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    A.append(row)

# Read second matrix
print("Enter elements of second matrix:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    B.append(row)

# Display first matrix
print("\nFirst Matrix:")
for row in A:
    print(row)

# Display second matrix
print("\nSecond Matrix:")
for row in B:
    print(row)

# Matrix Addition
print("\nMatrix Addition:")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] + B[i][j], end=" ")
    print()

# Matrix Subtraction
print("\nMatrix Subtraction:")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] - B[i][j], end=" ")
    print()

# Matrix Multiplication
if rows == cols:
    print("\nMatrix Multiplication:")
    for i in range(rows):
        for j in range(cols):
            total = 0
            for k in range(cols):
                total += A[i][k] * B[k][j]
            print(total, end=" ")
        print()
else:
    print("\nMultiplication requires compatible dimensions.")

# Transpose of first matrix
print("\nTranspose of First Matrix:")
for j in range(cols):
    for i in range(rows):
        print(A[i][j], end=" ")
    print()