class Employee:
    name="Monu"       #This is a class attribute
    Age= 23
    Salary = 100000
    
    def getinfo(self):
        print(f"The name is {self.name} and the age is {self.Age}")
        
    @staticmethod           #decorator to mark greet as a static method
    def greet():
        print("Good Morning")
    
Rohit = Employee()
Rohit.name = "Sunny"  #This is an instance attribute
# print(Rohit.name,Rohit.Salary,Rohit.Age)
Rohit.greet()
Rohit.getinfo()  #Both are same
Employee.getinfo(Rohit) #Both are same




# Here name is both declared as class and instance attribute, Instance Attribute take preferenece over class attribute

