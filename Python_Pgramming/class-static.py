class Employee:

    company="Guvi"

    def __init__(self,employeeName,role,salary):
    
        self.name=employeeName
        self.role=role
        self.salary=salary
      

    def employeeDetails(self):
        return f"\nCompany is {self.company}\nEmployee name is {self.name}\nEmployee Salary is {self.salary}\nEmployee Role is {self.role}"



    @staticmethod
    def greet():
        print("Good Morning")

    @classmethod
    def changeCompany(self,cls):
        self.company=cls
        print("Your company has changes ")



emp1=Employee("Anees","full stack trainer",50000)
emp2=Employee("Naz","full stack trainer",50000)
emp3=Employee("AAdi","full stack trainer",50000)
# print(emp1.employeeDetails())
# Employee.greet()
# emp1.greet()
emp1.changeCompany("Guvi Private Limited")
print(emp1.employeeDetails())
print(emp2.employeeDetails())
print(emp3.employeeDetails())