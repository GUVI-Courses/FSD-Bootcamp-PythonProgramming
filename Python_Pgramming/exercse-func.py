# 1)write a 4 functionsa)to find the area of circleb) to find the area of rectanglec)to find the area of squared)find the area of triangletake the inputs from the user for all 4 operation 

def circle():
    radius=int(input("Enter the radius:\n"))
    pi=3.14
    print("The Area of the circle is ",pi*radius*radius)

def rectangle():
    length=int(input("Enter the length:\n"))
    breadth=int(input("Enter the breadth:\n"))
    print("The Area of the Rectangle is ",length*breadth)

def square():
    side=int(input("Enter the Side:\n"))
    print("The Area of the Square is ",side*side)

def triangle():
    base=int(input("Enter the base:\n"))
    height=int(input("Enter the height:\n"))
    print("The area of the triangle is ",0.5*base*height)


def area():
    print("Enter 1: to call area of the circle")
    print("Enter 2: to call area of the Rectangle")
    print("Enter 3: to call area of the Square")
    print("Enter 4: to call area of the triangle")
    n=int(input("Enter the function number which you want to call:\n"))

    if n==1:
        circle()
    elif n==2:
        rectangle()
    elif n==3:
        square()
    elif n==4:
        triangle()
    else:
        area()


area()