class BankAccount:
    def __init__(self, accountNumber, name, balance = 0.0):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Imported {amount} euro.")
        else:
            print("The sum for import must be positive.")
    def Withdrawal(self, amount):
        if amount <= 0:
            print("The sum for towing must be positive.")
        elif amount > self.balance:
            print("Insufficient funds in the account.")
        else:
            self.balance -= amount
            print(f"Towed {amount} euro.")
    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Withheld fee: {fee:.2f} euro.")
    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.balance:.2f} €")
newAccount = BankAccount(2178514584, "Mariq", 2700)
newAccount.Withdrawal(300)
newAccount.Deposit(200)
newAccount.display()