# split
'''
data="Guvi is the best training platform"
words=data.split()
print(words)

data="Guvi is the best learning platform\nI am the mentor at guvi\ni am from bangalore"
words=data.split('\n')
print(words)
'''
# Joins
'''
words=["welcome","to","full","stack","developer","bootcamp","2024"]
delimiter=" "
sentence=delimiter.join(words)
print(sentence)

name="rohanshetty"
domain="gmail.com"
email='@'.join([name,domain])
print(email)
'''

'''
a=[1,2,3,4,5,6,7,8]
b=[2,3,4,6,8,9,0]
res=list(filter((lambda x:x not in b),a))
res=list(filter((lambda x:x  in b),a))
print(res)


def is_even(num):
    return num%2==0

numbers=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(is_even,numbers))
print(res)

numbers=[1,2,3,4,5,6,7,8,9,10]
res=set(filter(is_even,numbers))
print(res)
'''
'''
numbers=[1,2,3,4,5,6]
res=list(map((lambda x:x**5),numbers))
print(res)

def square(a):
    return a*a

def cube(a):
    return a*a*a

function=[square,cube]
numbers=[2,4,6,8]

for i in numbers:
    res=list(map((lambda x:x(i)),function))
    print(res)
'''

from functools import reduce
x=[1,2,3,4,5,6] #->iterable

# res=reduce((function),iterable)
res=reduce((lambda x,y:x*y),x)
print(res)

# x=[1,2,3,4,5,6]
# x=[2,3,4,5,6]
# x=[6,4,5,6]
# x=[24,5,6]
# x=[120,6]
# x=[720]