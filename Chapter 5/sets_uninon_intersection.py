s1 = {3,4,7,88}
s2 = {6,8,9,88,7}

print(s1.union(s2))  #{3, 4, 6, 7, 8, 9, 88}
print(s1.intersection(s2))  #{88, 7}

print(s1-s2)  #{3, 4}