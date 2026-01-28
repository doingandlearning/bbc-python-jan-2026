class BankAccount:
    def __init__(self, owner, starting_balance=0):
        if not isinstance(owner, str) or owner.strip() == "":
            raise ValueError("Owner name must be a non-empty string.")

        if not isinstance(starting_balance, (int, float)) or isinstance(starting_balance, bool):
            raise TypeError("Starting balance must be a number.")

        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative.")

        self.owner = owner.strip()
        self.balance = float(starting_balance)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Deposit amount must be a number.")

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += float(amount)
        return self.balance

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Withdrawal amount must be a number.")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= float(amount)
        return self.balance

    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Other account must be a BankAccount.")

        self.withdraw(amount)
        other_account.deposit(amount)
        return self.balance, other_account.balance

