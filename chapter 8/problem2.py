# Temperature Conversion

def conversion(f):
    return 5*(f-32)/9
    

f = int(input("Enter temperature in F: "))
c=conversion(f)
print(f"{round(c,2)} C")