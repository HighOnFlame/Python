f = open("Chapter 9/file.txt")
data = f.read()
print(data)
f.close()

# This can be written using with statement without need of close function in file

with open("Chapter 9/file.txt") as f:
        print(f.read())
    