# for i in range(100):
#     print(i)

# for i in range(1,101):
#     print(i)

# for i in range(15,21):
#     print(i)

# for i in range(0,101,5):
#     print(i)

# for i in range(-10,0):
#     print(i)

# for i in range(-10):
#     print(i)

'''

take a input from user.

2 x 1= 2
..
..
2 x 10 =20

'''
# n=int(input("Enter the table number to print\n"))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)

# i=1
# while(i<=5):
#     print(i)
#     i=i+1

i=1
while(i<=5):
    print(i)
    if(i==3):
        break
    i=i+1

i=0
while(i<=5):
    i=i+1
    if(i==3):
        continue
    print(i)