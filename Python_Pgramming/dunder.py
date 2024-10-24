class Employee:
    no_of_leaves=14
    def __init__(self,name,salary,role,phone):
        self.name=name
        self.salary=salary
        self.role=role
        self.phone=phone

    
    # def __str__(self):
    #     return f"\nEmployee Name is {self.name}\nSalary is {self.salary}\nRole is {self.role}\nPhone number is {self.phone}\n this is str"

    def __str__(self):
        return f"{self.name} {self.role}"
    
    # def __repr__(self):
    #     return f"{self.salary} {self.role}"
    
    def __add__(emp1,emp2):
        return emp1.salary+emp2.salary
    
    def __mul__(emp1,emp2):
        return emp1.salary*emp2.salary
    
    def __truediv__(emp1,emp2):
        return emp1.salary/emp2.salary
    
    def __floordiv__(emp1,emp2):
        return emp1.salary//emp2.salary

    
obj1=Employee("rohan",150000,"FSD",987456210)
obj2=Employee("rohit",150000,"FSD",987456210)
print(obj1)
print(obj1+obj2)
print(obj1*obj2)
print(obj1/obj2)
print(obj1//obj2)