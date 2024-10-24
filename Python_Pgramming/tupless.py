# tuple=immutable->cannot change the values 

mytuple=(1,2,3,4,5,6)
print(mytuple)
print(type(mytuple))
print(mytuple[2])
# mytuple[3]=100
for i in mytuple:
    print(i)

print(mytuple.index(4))