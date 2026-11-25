num = int(input("Enter a number: "))

print("Multiplication table using for loop:")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    num = int(input("Enter a number: "))

print("Multiplication table using while loop:")

i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1