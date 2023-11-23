my_list = []

# Add elements to the list
my_list.append("Sam")
my_list.append("Rafi")
my_list.append('Rabbi')
my_list.append("Fiyaz")
my_list.append("Niloy")

# Print the original list
print("Original list:", my_list)

# Access elements using index
print("Element at index 1:", my_list[1])

# Check if an element exists in the list
if "Rafi" in my_list:
    print("Rafi is present in the list")

# Remove an element from the list
my_list.remove("Sam")

# Print the modified list
print("Modified list:", my_list)
