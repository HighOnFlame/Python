s = {1,55,6,6932,3,4,4,5,6,7,999,"Monu"}

# sets are unordered and unindexed

s.add(678)
print(s,type(s))  #<class 'set'>



# 2. remove() - Remove an element (gives error if not found)
s.remove(55)
print( s)

# 3. discard() - Remove an element (no error if not found)
s.discard(999)
print(s)

# 4. pop() - Removes a random element
removed = s.pop()
print(removed)
print(s)

# 5. copy() - Create a copy
new_set = s.copy()
print(new_set)

# 6. update() - Add multiple elements
s.update({200, 300, "Rahul"})
print(s)

# 7. clear() - Remove all elements from copied set
new_set.clear()
print(new_set)

# 8. len() - Number of elements
print(len(s))