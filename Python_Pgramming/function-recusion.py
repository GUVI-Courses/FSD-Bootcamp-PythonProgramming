n=int(input("enter the number to find the factorial.."))
def factorial(n):
    if n==1 or n==0:
        return 1
    print(n)
    return n*factorial(n-1)

result=factorial(n)
print(f"Factorial of {n} is {result}")
















# 3! 3*2*1 
# 5! 5*4*3*2*1