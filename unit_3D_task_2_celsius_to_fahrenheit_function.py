def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get temperature from the user
c = float(input("Enter temperature in Celsius: "))

# Convert and display the result
f = celsius_to_fahrenheit(c)

print("Temperature in Fahrenheit:", f)