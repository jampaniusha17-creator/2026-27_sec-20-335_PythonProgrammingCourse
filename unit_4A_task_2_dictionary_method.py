# Sample dictionary
student = {
    "name": "Krishna",
    "age": 20,
    "course": "Python"
}

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# get()
print("Name:", student.get("name"))

# update()
student.update({"age": 21, "city": "Guntur"})
print("After update:", student)

# pop()
removed = student.pop("course")
print("Removed course:", removed)
print("After pop:", student)