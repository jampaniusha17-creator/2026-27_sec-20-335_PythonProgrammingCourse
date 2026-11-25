def find_sum(*args):
    total = sum(args)
    return total

# Calling the function with different numbers of arguments
print("Sum of 1, 2, 3:", find_sum(1, 2, 3))
print("Sum of 10, 20, 30, 40:", find_sum(10, 20, 30, 40))
print("Sum of 5, 15:", find_sum(5, 15))