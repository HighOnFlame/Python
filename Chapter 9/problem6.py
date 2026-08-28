with open("Chapter 9/file.txt") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes python is present")
else:
    print("No Python is not present")