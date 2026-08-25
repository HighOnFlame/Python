friends = ["Monu", "Ranjan", "Aditi"]

print("Original:", friends)

friends.append("Rahul")          # Add at end
print("append():", friends)

friends.insert(1, "Priya")       # Insert at index
print("insert():", friends)

friends.remove("Ranjan")         # Remove by value
print("remove():", friends)

friends.pop()                    # Remove last element
print("pop():", friends)

friends.reverse()                # Reverse list
print("reverse():", friends)

friends.sort()                   # Sort alphabetically
print("sort():", friends)

print("Index of Monu:", friends.index("Monu"))
print("Count of Monu:", friends.count("Monu"))
print("Length:", len(friends))

copy_list = friends.copy()       # Copy list
print("Copied List:", copy_list)

copy_list.clear()                # Empty the copied list
print("After clear():", copy_list)