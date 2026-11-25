# Read two numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform arithmetic operations
print("Addition (+) =", a + b)
print("Subtraction (-) =", a - b)
print("Multiplication (*) =", a * b)

if b != 0:
    print("Division (/) =", a / b)
    print("Floor Division (//) =", a // b)
    print("Modulus (%) =", a % b)
else:
    print("Division (/) = Not possible")
    print("Floor Division (//) = Not possible")
    print("Modulus (%) = Not possible")

print("Exponentiation (**) =", a ** b)