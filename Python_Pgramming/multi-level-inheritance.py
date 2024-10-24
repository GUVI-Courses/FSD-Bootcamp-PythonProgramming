class Company:#parent class

    def __init__(self,name,location,branch):
        self.name=name
        self.location=location
        self.branch=branch
        print("constructor of company has been set...")
    
    def companyDetails(self):
        return f"\nCompany Name is {self.name}\n Company Located at {self.location}\nBranch is {self.branch}"

    
class Employee(Company): #child classs

    def __init__(self,name,location,branch,empid,employeeName,employeeRole):
        super().__init__(name,location,branch)
        self.empid=empid
        self.employeeName=employeeName
        self.employeeRole=employeeRole
        print("constructor of Employee has been set...")
    

    def employeeDetails(self):
        return f"\nEmployee Id is {self.empid}\nEmployee Name is {self.employeeName}\nEmployee Role is {self.employeeRole}"

class Manager(Employee): #sub child class

    def __init__(self, name, location, branch, empid, employeeName, employeeRole,managerName,deliveryStream):
        super().__init__(name, location, branch, empid, employeeName, employeeRole)
        self.managerName=managerName
        self.stream=deliveryStream
        print("constructor of manager has been set..")
    
    def managerDetails(self):
        return f"\nManager name is {self.managerName}\nDelivery Stream is {self.stream}"


obj1=Manager("Guvi","Noida","Delhi NRC","GUVI121212","Jayasri","ONboarding AUthor","Priyanka","Marketing")
print(obj1.companyDetails())
print(obj1.employeeDetails())
print(obj1.managerDetails())