class A():
    def show(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(A):
    def showC(self):
        print("C")

class D(B,C):
    def showD(self):
        print("D")


objd=D()
objd.show()
objd.showB()
objd.showC()
objd.showD()