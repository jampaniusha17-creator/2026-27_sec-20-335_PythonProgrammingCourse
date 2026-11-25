# Nested dictionary to store student details

students = {
    101: {"name": "Krishna", "marks": 85},
    102: {"name": "Radha", "marks": 90},
    103: {"name": "Arjun", "marks": 78}
}

# Print student names and marks
for roll_no, details in students.items():
    print("Roll No:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()