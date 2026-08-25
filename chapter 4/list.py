friends = ["Monu"," Ranjan"," Singh", "Sanjana", 18, 88,11,6]
print(friends)

#lists are mutable
friends[1]="Aditi"
print(friends)

#we can add and remove elements in lists using append and remove function
friends[0] = "Rahul"   # Modify
friends.append("Priya")  # Add at the end of list
friends.remove(88)     # Remove

print(friends)
print(friends[1:4])


l1 = [2,3,56,33,5,22]
# l1.sort()
print(l1)
# l1.reverse()
l1.insert(3,3336)
print(l1)