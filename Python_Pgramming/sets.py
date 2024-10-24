# # s=set()
# # s.add(1)
# # s.add(2)
# # s.add(3)
# # s.add(4)
# # print(s,type(s))

# s1={1,2,3,4,5,1,2,3,4,5,7,8,9,8,7,6}
# print(s1)
# print(s1)

# s2={10,11,18}
# s3={1,2,5,7,8,0,1,4}
# print(s3)

# print(s1.union(s2).union(s3))
# print(s1.intersection(s3))

# print(s3.pop())
# print(s3.pop())
# print(s3.pop())
# print(s3.pop())

# print(s2.remove(11))
# print(s2)

s1={1,2,3,4,5,6,7,8}
s2={'a','b','c'}
s1=s1.union(s2)
print(s1)
s3={}
for i in s1:
    if i not in s3:
        print(i)