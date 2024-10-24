class Company:#parent class

    def __init__(self,name,location,branch):
        self.name=name
        self.location=location
        self.branch=branch
        print("constructor of company has been set")
    
    def companyDetails(self):
        return f"\nCompany Name is {self.name}\n Company Located at {self.location}\nBranch is {self.branch}"

    
class Employee(Company):

    def __init__(self,name,location,branch,empid,employeeName,employeeRole):
        # self.name=name
        # self.location=location
        # self.branch=branch
        super().__init__(name,location,branch)
        self.empid=empid
        self.employeeName=employeeName
        self.employeeRole=employeeRole
        print("constructor of Employee has been set")
    

    def employeeDetails(self):
        return f"\nEmployee Id is {self.empid}\nEmployee Name is {self.employeeName}\nEmployee Role is {self.employeeRole}"
    

emp1=Employee("Guvi","Chennai","IIT",123456,"Rakesh","Full stack developer")
print(emp1.companyDetails())
print(emp1.employeeDetails())