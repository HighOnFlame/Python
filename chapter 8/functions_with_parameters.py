def greet(name,ending):
    
    print("Have a good day, " + name)
    print(ending)
    
greet("Monu", "Thank you")
greet("Sanjan", "Thank you")
greet("Aditi", "Thanks")


def greet2(name,ending):
    
    print("Have a good day, " + name)
    print(ending)
    return "done"

a = greet2("Monu", "Thank you")
print(a)
