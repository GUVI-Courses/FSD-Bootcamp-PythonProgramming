class Human:
    # create data members /attributes
    human_name="anonymous"
    age=75
    category=['male','female']

    # methods
    def humanDetails(self):
        print(f"Human Name is {self.human_name} age is {self.age} categories {self.category}")

    def greet(self):
        print("Good Afternoon...",{self.human_name})

# create the objects

obj1=Human()
obj1.humanDetails()
obj1.greet()

obj2=Human()
obj2.human_name="Anees"
obj2.age=28
obj2.category=obj2.category[0]
obj2.humanDetails()

obj3=Human()
obj3.age=12
obj3.human_name="naz"
obj3.category=obj3.category[1]

print(obj3.humanDetails())

print(obj3,obj1,obj2)