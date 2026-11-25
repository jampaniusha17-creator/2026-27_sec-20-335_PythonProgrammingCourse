def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Get input from the user
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

# Function call
area, perimeter = rectangle(length, breadth)

# Display the results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)