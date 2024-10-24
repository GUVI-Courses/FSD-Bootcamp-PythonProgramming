# class Data:
#     # public
#     name="guvi"
#     _email="guvi@gmail.com" #protected
#     __password="guvi***" #private

# obj=Data()
# print(obj.name)
# print(obj._email)
# print(obj._Data__password)


class BankAccount:

    def __init__(self,accountNumber,balance):
        self._accountNumber=accountNumber #protected varaible _accountNumber
        self.__balance=balance #Private varaible __balance


    #getter method for balance
    def getBalance(self):
        return self.__balance
    
    #setter method for balance with validation

    def setBalance(self,newBalance):
        if(newBalance>=0):
            self.__balance=newBalance


    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    
    # public method withdraw the amount
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        
        else:
            print("Insuffient Balance..........")


account=BankAccount(4154442154,25000)
print(account.getBalance())
account.deposit(5000)
print(account.getBalance())
account.withdraw(7000)
print(account.getBalance())

print(account._accountNumber)
print(account._BankAccount__balance)