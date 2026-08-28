# Greet only those names whose names start with S

l = ["Monu", "Shubham", "Ankit", "Rajeev", "Ravi"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")