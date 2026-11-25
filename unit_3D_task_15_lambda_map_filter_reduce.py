from functools import reduce

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Using lambda with reduce()
total = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", total)