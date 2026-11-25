# List of student dictionaries
students = [
    {"name": "Krishna", "marks": 85},
    {"name": "Ravi", "marks": 72},
    {"name": "Anu", "marks": 95},
    {"name": "Priya", "marks": 60}
]

# Sort by marks in ascending order
ascending = sorted(students, key=lambda s: s["marks"])

# Sort by marks in descending order
descending = sorted(students, key=lambda s: s["marks"], reverse=True)

print("Ascending order:")
for student in ascending:
    print(student)

print("\nDescending order:")
for student in descending:
    print(student)