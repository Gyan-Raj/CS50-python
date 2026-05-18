# We genearlly avoid using "global", as it may start getting messy with time. So, we use class

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print(f"Balance : {account.balance}")
    account.deposit(120)
    account.withdraw(30)
    print(f"Balance : {account.balance}")


if __name__ == "__main__":
    main()
