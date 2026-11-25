# Demonstrate different string formatting methods

name = "Usha"
age = 20
marks = 95.5

# 1. Using format() method
print("Using format() method:")
print("My name is {} and my age is {}.".format(name, age))
print("I scored {:.1f} marks.".format(marks))

# 2. Using f-strings
print("\nUsing f-strings:")
print(f"My name is {name} and my age is {age}.")
print(f"I scored {marks:.1f} marks.")

# 3. Using % operator
print("\nUsing % operator:")
print("My name is %s and my age is %d." % (name, age))
print("I scored %.1f marks." % marks)