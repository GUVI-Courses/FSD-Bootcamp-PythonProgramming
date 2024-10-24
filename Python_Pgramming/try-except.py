# print(2/0)
# print(1+'guvi')

try:
    num1=int(input("enter 1st num : "))
    num2=int(input("enter 2nd num : "))
    print(num1/num2)
except Exception as e:
    print("error occured",e)

else:
    print("if try block execute i will be executing the code")

finally:
    print("it is going to execute compulsory")