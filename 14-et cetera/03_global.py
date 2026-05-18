# Code is same as 02_global.py except that we added "global balance" in the deposit and withdraw functions

balance = 0


def main():
    print("Balance:", balance)
    deposit(120)
    withdraw(30)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance

    balance -= n


if __name__ == "__main__":
    main()
