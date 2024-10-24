'''

class Calculator:
    # def add(self,a,b):
    #     return a+b
    
    # def add(self,a,b,c):

    #     return a+b+c
    

    # def add(self,a,b,c,d):
    #     return a+b+c+d
    def add(self,*args):
        res=0
        for n in args:
            res+=n
        return res

obj1=Calculator()
print(obj1.add(2,2,2,2))
print(obj1.add(2,2,2))
print(obj1.add(2,2,2,2,22,2,23,4,5,6,677,77,322)) '''


# overiding
class Animal:
    def speak(self):
        print("Animal doesnt speak")
    
class Dog(Animal):
    def speak(self):
        print("dog barks")
    
class Cat(Animal):
    # def speak(self):
    #     print("cat meows")
    pass
    
obj=Cat()
obj.speak()