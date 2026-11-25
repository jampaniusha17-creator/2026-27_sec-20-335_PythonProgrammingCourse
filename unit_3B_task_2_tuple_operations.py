# Creating two tuples
tuple1 = (10, 20, 30, 40)
tuple2 = (50, 60, 70)

# 1. Tuple Concatenation
result = tuple1 + tuple2
print("Tuple Concatenation:", result)

# 2. Tuple Slicing
print("Tuple Slicing:", tuple1[1:3])
print("First Three Elements:", tuple1[:3])
print("Last Two Elements:", tuple1[-2:])

# 3. Tuple Unpacking
a, b, c, d = tuple1
print("Tuple Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)