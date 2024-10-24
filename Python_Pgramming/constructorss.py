'''
class Person:

    def __init__(self):
        print("i am a constructor i will get called compulsory whenever you create the object")

p1=Person()
p2=Person()
p3=Person()
'''
class Employee:

    company="Guvi"

    def __init__(self,employeeName,role,salary):
        print("i am going to set the values for the object",self)
        self.name=employeeName
        self.role=role
        self.salary=salary
        print("i have set the values")

    def employeeDetails(self):
        return f"\nEmployee name is {self.name}\nEmployee Salary is {self.salary}\nEmployee Role is {self.role}"


emp1=Employee("Anees","full stack trainer",50000)
emp2=Employee("Naz","full stack mentore",150000)
emp3=Employee("AAdithyaa","UI/uX designer",90000)
print(emp1.employeeDetails())
print(emp2.employeeDetails())
print(emp3.employeeDetails())
