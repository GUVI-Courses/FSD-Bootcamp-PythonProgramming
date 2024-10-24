from abc import ABC,abstractmethod

# abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimter(self):
        print("i want to find the area of perimeter")

    def greet(self):
        print("Good Morning....")


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimter(self):
        # return super().perimter()
        return 2*3.14*self.radius


obj=Circle(5)
print(obj.greet())
print(obj.area())
print(obj.perimter())