# Create squares of numbers from 1 to 10 using list comprehension
squares = [x**2 for x in range(1, 11)]

# Create even numbers from 1 to 10 using list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print("Squares:", squares)
print("Even numbers:", even_numbers)