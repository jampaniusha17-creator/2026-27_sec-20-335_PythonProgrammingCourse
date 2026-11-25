# Merge two dictionaries using update() without changing the original

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Create a copy of the first dictionary
merged_dict = dict1.copy()

# Merge the second dictionary into the copy
merged_dict.update(dict2)

print("Original Dictionary 1:", dict1)
print("Original Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)