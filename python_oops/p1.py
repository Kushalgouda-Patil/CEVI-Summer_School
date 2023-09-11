class BankAccount:
    def __init__(self,name,id:int,amount:int):
        self.name=name
        self.id=id
        self.amount=amount
    def __str__(self):
        return f'Name={self.name},Amount={self.amount}'
acc1=BankAccount("Kushal",34,89)
print(acc1)


