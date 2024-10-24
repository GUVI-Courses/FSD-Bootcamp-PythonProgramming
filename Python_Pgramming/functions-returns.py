def business_one(p1,p2,p3):
    total=p1+p2+p3
    interest=10000
    finalamount=total+interest
    return finalamount


def business_two(p1,p2,p3):
    total=p1+p2+p3
    interest=20000
    finalamount=total+interest
    return finalamount


def business_three(p1,p2,p3):
    total=p1+p2+p3
    interest=30000
    finalamount=total+interest
    return finalamount

 
b1=business_one(15000,10000,5000)
b2=business_two(15000,10000,5000)
b3=business_three(15000,10000,5000)
print("Total profit",b1+b2+b3)