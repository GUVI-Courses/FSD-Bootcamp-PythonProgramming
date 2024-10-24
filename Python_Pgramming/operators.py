'''
a=10
a+=20 #a=a+20 #a=10+20
print(a)

# a=30
a/=10 #a=a/10 a=30/10
print(a)

# a=3
a**=3 #a=a**3 a=3*3*3 if a=5 a=5*5*5
print(a)

x=2
y=x**5 #2*2*2*2*2
print(y)

o=10
p=30
print(o%p) #10/30 
print(p%o) #30/10= remainder=0 quotient=3
print(33%10) #33/10= remainder=3 quotient=3
'''
# comparison operators
# print(12<20)
# print(12>20)

# a=10
# b=10
# c='10'
# print(a==b)
# print(a==c)

# v=10
# print(c!=v)

# And-or-not
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# or
print("or\n")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

a=10
b=20
c=30
d=40
print("\n")
print(a<=b and c>=d) #F
# print(True and False)
print(a<=b and c<=d) #T

print("\n")
print("or",a<=b or c>=d) #T
# print(True or False)
print("or",a<=b or c<=d) #T
print("or",a>b or c>d)

# not
print(not True) 
print(not False)
print("Identity operator")
# is and is not
print(2 is 3)
print(2 is not 3)

print("membership opeartor")
a=[1,2,3]
print(1 in a)
print(20 not in a)

# bitwise
print(1 | 1)
print(1 & 1) 
print(1 & 0) 
print(1 & 1 & 1& 0)
print(1 | 0 | 0 | 0 | 0)