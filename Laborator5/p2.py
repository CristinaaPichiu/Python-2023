class Account:
    def __init__(self, account_number, sum = 0):
        self.account_number = account_number
        self.sum = sum

    def deposit(self, amount):
        self.sum += amount

    def withdrawal(self, amount):
        if self.sum >= amount:
            self.sum -= amount
        else:
            print("Insufficient funds")

    """ returnează o reprezentare sub formă de șir de caractere a obiectului Account
      care conține numărul de cont și soldul acestuia. """

    def __str__(self):
        return f"Account Number: {self.account_number}\nBalance: {self.sum}"


class SavingsAccount(Account):

    """ calculul dobânzii pe baza soldului și a ratei specificate."""
    def calculate_interest(self, rate):
        return self.sum * rate


class CheckingAccount(Account):
    def __init__(self, account_number, sum=0, overdraft_limit=0):
        super().__init__(account_number, sum)
        self.overdraft_limit = overdraft_limit


    """ verifică dacă retragerea depășește limita de depășire a soldului în minus
        permițând sau refuzând retragerea. """

    def withdrawal(self, amount):
        if self.sum - amount >= -self.overdraft_limit:
            self.sum -= amount
        else:
            print("Exceeds overdraft limit")


if __name__ == "__main__":
    acc1 = SavingsAccount("SA001", 1000)
    acc1.deposit(500)
    acc1.withdrawal(200)
    print(acc1)
    print("Interest:", acc1.calculate_interest(0.05))

    acc2 = CheckingAccount("CA001", 500, 1000)
    acc2.deposit(200)
    acc2.withdrawal(900)
    print(acc2)
    acc2.withdrawal(600)
