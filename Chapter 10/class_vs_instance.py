class Employee:
    name="Monu"       #This is a class attribute
    Age= 23
    Salary = 100000
    
Rohit = Employee()
Rohit.name = "Sunny"  #This is an instance attribute
print(Rohit.name,Rohit.Salary,Rohit.Age)


# Here name is both declared as class and instance attribute, Instance Attribute take preferenece over class attribute

