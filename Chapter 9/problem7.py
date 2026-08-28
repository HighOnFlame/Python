

with open("Chapter 9/file.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line.lower()):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No Python is not present")