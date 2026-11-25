
# Program to calculate Compound Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

amount = principal * (1 + rate / 100) ** time

compound_interest = amount - principal

print("Compound Interest =", compound_interest)
print("Total Amount =", amount)
