
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # Encapsulation (private)

    # Abstraction: User calls this without caring how it works internally
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited.")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn.")

    # Encapsulation: controlled access to balance
    def get_balance(self):
        return self.__balance
    

# Inheritance
class SavingAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)

# Method Overriding
# Method Overloading

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    # Method overriding
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount

            print(f"{amount} withdrawn using overdraft policy.")

            self._Account__balance = new_balance

        else:
            print("Overdraft limit reached")


accounts = [
    SavingAccount("Kingsley", 1000),
    CheckingAccount("Mary", 500)
]

for acc in accounts:
    acc.withdraw(200)