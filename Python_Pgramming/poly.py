class Human:
    def __init__(self,name):
        self.name=name
    
    def intro(self):
        print("Hello my name is ",{self.name})

    def perform_activity(self):
        print("human activity")

class Teacher(Human):
    def perform_activity(self):
        print("teacher teach")
    
class Student(Human):
    def perform_activity(self):
        print("student learns")
    
obj1=Teacher("ark")
obj2=Student("john")

people=[obj1,obj2]

for p in people:
    p.intro ()
    p.perform_activity()