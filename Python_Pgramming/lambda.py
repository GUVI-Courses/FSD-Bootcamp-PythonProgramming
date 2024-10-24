def add(a,b):
    return a+b

output=add(15,12)
print(output)

add=lambda x,y:x+y
print(add(15,25))

add=lambda x,y,z,u:x+y+z+u
print(add(15,25,5,5))

minus=lambda x,y:x-y
div = lambda x,y:x/y
mod=lambda x,y:x%y
mult= lambda a,b,c:a*b*c
print(minus(15,25))
print(div(15,25))
print(mod(15,25))
print(mult(15,25,2))