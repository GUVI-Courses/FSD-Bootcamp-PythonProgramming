mydict={
    "employeeName":"Anees",
    "employeeRole":"Full stack developer",
    "since":2020,
    "salary":50000.25,
    "skills":["python","java","react","angular"],
    "interest":{"cricket","gym","teaching"},
    "isActive":True

}
# print(mydict)
# print(type(mydict))
# print(mydict.get("skills"))
# print(mydict.get("isActive"))
# print(mydict.keys())
# print(mydict.values())

mydict.update({"phoneNumber":98789878987})
mydict.update({"since":2017})
print(mydict)


mydict2=mydict.copy()
print(mydict2)

mydict2.clear()
print(mydict2)

# for key in mydict:
#     print(key,mydict.get(key))

# for i,j in mydict.items():
#     print(i,j)