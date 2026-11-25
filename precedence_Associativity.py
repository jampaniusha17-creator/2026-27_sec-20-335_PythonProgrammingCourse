# Program to demonstrate operator precedence and associativity

a = 10
b = 5
c = 2

# Operator Precedence
result1 = a + b * c
print("Operator Precedence:")
print("10 + 5 * 2 =", result1)

result2 = (a + b) * c
print("(10 + 5) * 2 =", result2)

# Operator Associativity
result3 = 10 - 5 - 2
print("\nOperator Associativity:")
print("10 - 5 - 2 =", result3)

result4 = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result4)