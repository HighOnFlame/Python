student = {
    "name": "Monu",
    "age": 22,
    "course": "B.Tech"
}

# print(student)

# # 1. keys() - Returns all keys
# print(student.keys())

# # 2. values() - Returns all values
# print(student.values())

# # 3. items() - Returns key-value pairs
# print(student.items())

# # 4. get() - Returns value of a key
# print(student.get("name"))

# # 5. update() - Add or update elements
# student.update({"age": 23, "city": "Patna"})
# print(student)

# # 6. pop() - Remove an element using key
# student.pop("course")
# print(student)

# # 7. popitem() - Removes the last inserted item
# student.popitem()
# print( student)

# # 8. clear() - Removes all items
# copy_dict = student.copy()
# copy_dict.clear()
# print(copy_dict)

# # 9. copy() - Creates a copy
# new_student = student.copy()
# print(new_student)

# # 10. len() - Number of key-value pairs
# print(len(student))

print(student.get("name2")) #prints none
print(student["name2"]) #gives error