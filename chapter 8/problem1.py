# Write a program using a function to find the greatest of three numbers

def greatest():
    a = int(input("Enter Number 1 : "))
    b = int(input("Enter Number 2 : "))
    c = int(input("Enter Number 3 : "))
    
    if(a>b and a>c):
        print(f"{a} is greatest")
    elif(b>a and b>c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")


greatest()
