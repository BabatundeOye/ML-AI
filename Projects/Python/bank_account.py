

class BankAccount:
    def __init__(self,  account_number, account_type, account_name, balance= 0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.balance = balance
                    
    def account_details(self):
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Account type: {self.account_type}")
        print(f"Account name: {self.account_name}")

    def check_balance(self):
        print(f"Hello {self.account_name}, Your balance is", self.balance) 
        
    def account_type(self):
        print(f"Account type: {self.account_type}")
    def deposit(self, deposit):
        amount_deposited = float(input("Enter amount to deposit: "))
        if deposit != amount_deposited:  
            raise ValueError("invalid deposit amount")
        else:
            self.balance += amount_deposited
            print("Deposit successful, your balance is now", self.balance)
    
    def withdrawal(self, withdrawal):
        amount =float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        else:
            self.balance -= withdrawal
            print(f"Withdrawal successful, you withdrew {amount}, \n Your balance is now", self.balance)
           

Account_1 = BankAccount (345678, "Savings","Tom Dash", 59870)
Account_2 = BankAccount (123456, "Current", "Axel Quni", 50000)

print(f"{Account_1.account_name} has a balance of {Account_1.balance}")
print(f"{Account_2.account_name} has a {Account_2.account_type} account with a balance of {Account_2.balance}")


Account_1.account_details()
Account_1.deposit(500)
Account_1.check_balance()
Account_1.withdrawal(200)
Account_1.check_balance()