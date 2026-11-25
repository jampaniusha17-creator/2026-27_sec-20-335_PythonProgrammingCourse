# Program to demonstrate string methods

# Original string
s = "  Hello Python Programming  "

print("Original String:", s)

# 1. upper()
print("Uppercase:", s.upper())

# 2. lower()
print("Lowercase:", s.lower())

# 3. strip()
print("After strip():", s.strip())

# 4. split()
text = "Hello Python Programming"
print("After split():", text.split())

# 5. join()
words = ["Hello", "Python", "Programming"]
print("After join():", " ".join(words))

# 6. replace()
print("After replace():", text.replace("Python", "Java"))

# 7. find()
print("After find():", text.find("Python"))