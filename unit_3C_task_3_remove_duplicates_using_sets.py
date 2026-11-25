# Create a list with duplicate elements
my_list = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:", my_list)

# Convert the list into a set to remove duplicates
unique_set = set(my_list)

# Convert the set back into a list
unique_list = list(unique_set)

print("List after removing duplicates:", unique_list)