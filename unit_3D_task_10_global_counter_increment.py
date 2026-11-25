# Global counter
counter = 0

def increment_counter():
    global counter
    counter += 1
    print("Counter:", counter)

# Function calls
increment_counter()
increment_counter()
increment_counter()
increment_counter()
increment_counter()