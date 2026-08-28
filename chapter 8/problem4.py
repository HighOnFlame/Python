#sum of first n natural numbers

def sumofn(n):
    if(n==1):
        return 1
    return n+sumofn(n-1)
    
    
n = int(input("Enter value of n : "))
print(f"Sum of n is :  {sumofn(n)}")


# another way to print
print(sumofn(4))