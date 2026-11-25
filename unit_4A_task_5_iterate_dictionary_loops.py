# Subject marks dictionary
marks = {
    "Python": 95,
    "Java": 88,
    "C": 90,
    "Maths": 85
}

# Print keys
print("Keys:")
for key in marks.keys():
    print(key)

# Print values
print("\nValues:")
for value in marks.values():
    print(value)

# Print items (key-value pairs)
print("\nItems:")
for key, value in marks.items():
    print(key, ":", value)