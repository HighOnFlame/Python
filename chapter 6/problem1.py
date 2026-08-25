a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
d = int(input("Enter number 4 : "))

if(a>b and a>c and a>d):
    print("num 1 is greatest")

if(b>a and b>c and b>d):
    print("num 2 is greatest")
    
if(c>a and c>b and c>d):
    print("num 3 is greatest")
else:
    print("num 4 is greatest")