# 1. write a class of BankAccount with deposit and withdraw methods.

class BankAccount:

    def __init__(self,accountnumber:int,balance:int):
        self.an = accountnumber
        self.balance = balance

    def deposit(self,amount:int)->int:
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount:int)->int:
        self.balance -= amount
        return self.balance
    
    def get_balance(self)->int:
        return self.balance
    
Bank = BankAccount(1234,1000)
print(Bank.withdraw(800))
