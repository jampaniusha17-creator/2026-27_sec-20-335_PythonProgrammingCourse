try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter an integer.")
else:
    print("Square =", num * num)
finally:
    print("Program finished")