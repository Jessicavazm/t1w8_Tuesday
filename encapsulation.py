class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit (self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit Successful! New balance: {self.__balance}"
        else:
            return "Invalid transaction"
        
    def withdrawn(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
            return f"Withdrawn successful! New balance: {self.__balance}"
        else:
            return "Invalid withdraw amount or insufficient funds."
        
    def check_balance(self):
        return f"Account balance is {self.__balance}"
    
# Create a bank account for Jess with a initial balance of 1000
jess_account = BankAccount("Jess", 1000)

luke_account = BankAccount("Jess", 500)
# Check balance
print(jess_account.check_balance())

# Deposit money
print(jess_account.deposit(500))

# Withdrawn money
print(jess_account.withdrawn(250))

# Experiment try to withdrawn more money than the amount in balance
print(jess_account.withdrawn(2000))

# Experiment, adding to jess_account balance without deposit, only changing the balance variable
jess_account.__balance = -2000
# Since I have encapsulated the __balance variable, now if you change it from outside it won't work. 
print(jess_account.check_balance())